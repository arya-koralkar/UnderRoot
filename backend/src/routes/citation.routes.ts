import { Router } from "express";
import { authMiddleware } from "../middleware/auth.js";
import { citationLimiter } from "../middleware/rateLimiter.js";
import { suggestCitations } from "../controllers/citation.controller.js";
import { validateBody } from "../middleware/validate.js";
import { aiTextRequestSchema } from "../schemas/ai.schemas.js";

const router = Router();
router.post("/suggest", authMiddleware, citationLimiter, validateBody(aiTextRequestSchema), suggestCitations);
export default router;