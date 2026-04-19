import { Router } from "express";
<<<<<<< HEAD
import { authMiddleware } from "../middleware/auth.js";
import { citationLimiter } from "../middleware/rateLimiter.js";
import { suggestCitations } from "../controllers/citation.controller.js";
import { validateBody } from "../middleware/validate.js";
import { aiTextRequestSchema } from "../schemas/ai.schemas.js";

const router = Router();
router.post("/suggest", authMiddleware, citationLimiter, validateBody(aiTextRequestSchema), suggestCitations);
export default router;
=======
import { authMiddleware } from "../middleware/auth";
import { citationLimiter } from "../middleware/rateLimiter";
import { suggestCitations } from "../controllers/citation.controller";

const router = Router();

router.post("/suggest", authMiddleware, citationLimiter, suggestCitations);

export default router;
>>>>>>> ai-service-fix
