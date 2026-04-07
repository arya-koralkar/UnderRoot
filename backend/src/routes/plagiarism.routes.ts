import { Router } from "express";
import { authMiddleware } from "../middleware/auth.js";
import { plagiarismLimiter } from "../middleware/rateLimiter.js";
import { checkPlagiarism } from "../controllers/plagiarism.controller.js";
import { validateBody } from "../middleware/validate.js";
import { aiTextRequestSchema } from "../schemas/ai.schemas.js";

const router = Router();
router.post("/check", authMiddleware, plagiarismLimiter, validateBody(aiTextRequestSchema), checkPlagiarism);
export default router;