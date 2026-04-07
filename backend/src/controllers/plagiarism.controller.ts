import { Request, Response } from "express";
import axios, { AxiosError } from "axios";
import crypto from "crypto";
import { cacheService } from "../services/redis.service.js";
import { config } from "../config/env.js";

const CACHE_TTL = 3600; // 1 hour

type ApiSuccess<T> = {
  success: true;
  data: T;
  meta?: { cached?: boolean };
};

type ApiError = {
  success: false;
  error: { code: string; message: string };
};

function buildCacheKey(text: string, projectId?: string) {
  const hash = crypto
    .createHash("sha256")
    .update(`${projectId ?? "no-project"}:${text}`)
    .digest("hex");
  return cacheService.generateKey("plagiarism", hash);
}

export async function checkPlagiarism(req: Request, res: Response): Promise<void> {
  try {
    const { text, projectId } = req.body as { text?: string; projectId?: string };

    if (!text || !text.trim()) {
      const response: ApiError = {
        success: false,
        error: { code: "VALIDATION_ERROR", message: "text is required" },
      };
      res.status(400).json(response);
      return;
    }

    const cacheKey = buildCacheKey(text, projectId);
    const cached = await cacheService.get(cacheKey);
    if (cached) {
      const response: ApiSuccess<unknown> = {
        success: true,
        data: cached,
        meta: { cached: true },
      };
      res.json(response);
      return;
    }

    const aiResponse = await axios.post(
      `${config.aiServiceUrl}/api/plagiarism/check`,
      { text, project_id: projectId },
      { timeout: 12000 }
    );

    await cacheService.set(cacheKey, aiResponse.data, CACHE_TTL);

    const response: ApiSuccess<unknown> = {
      success: true,
      data: aiResponse.data,
      meta: { cached: false },
    };
    res.json(response);
  } catch (err) {
    const e = err as AxiosError;
    const isTimeout = e.code === "ECONNABORTED";
    const status = isTimeout ? 504 : 502;

    const response: ApiError = {
      success: false,
      error: {
        code: isTimeout ? "AI_TIMEOUT" : "AI_SERVICE_ERROR",
        message: isTimeout
          ? "AI service timed out. Please try again."
          : "Failed to check plagiarism",
      },
    };

    console.error("Plagiarism controller error:", err);
    res.status(status).json(response);
  }
}