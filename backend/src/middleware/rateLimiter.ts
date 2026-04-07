import { Request, Response, NextFunction } from "express";
import redis from "../config/redis.js";

function createRateLimiter(limit: number, windowSeconds: number) {
  return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    const userId = (req as Request & { userId?: string }).userId;
    const identity = userId || req.ip || req.socket.remoteAddress || "unknown";
    const key = `rate:${req.baseUrl}${req.path}:${identity}`;

    try {
      const count = await redis.incr(key);
      if (count === 1) await redis.expire(key, windowSeconds);

      if (count > limit) {
        res.status(429).json({
          success: false,
          error: { code: "RATE_LIMITED", message: "Rate limit exceeded. Please try again later." },
        });
        return;
      }
    } catch {
      // fail-open
    }

    next();
  };
}

const SECONDS_PER_DAY = 24 * 60 * 60;
const SECONDS_PER_HOUR = 60 * 60;

// IMPORTANT: keep these named exports for your routes
export const citationLimiter = createRateLimiter(20, SECONDS_PER_DAY);
export const plagiarismLimiter = createRateLimiter(10, SECONDS_PER_HOUR);

// optional generic export if you use it elsewhere
export { createRateLimiter };