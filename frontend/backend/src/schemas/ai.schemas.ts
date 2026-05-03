import { z } from "zod";

export const aiTextRequestSchema = z.object({
  text: z.string().trim().min(20, "text must be at least 20 chars"),
  projectId: z.string().optional(),
});