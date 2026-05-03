import axios from "axios";
import { config } from "../config/env.js";

const client = axios.create({
  baseURL: config.aiServiceUrl,
  timeout: 8000,
});

async function withRetry<T>(fn: () => Promise<T>, retries = 2): Promise<T> {
  let lastErr: unknown;
  for (let i = 0; i <= retries; i++) {
    try {
      return await fn();
    } catch (err) {
      lastErr = err;
      if (i < retries) await new Promise((r) => setTimeout(r, 250 * (i + 1)));
    }
  }
  throw lastErr;
}

export const aiClient = {
  suggestCitations: (text: string, projectId?: string) =>
    withRetry(() =>
      client.post("/api/citations/suggest", { text, project_id: projectId }).then((r) => r.data)
    ),
  checkPlagiarism: (text: string, projectId?: string) =>
    withRetry(() =>
      client.post("/api/plagiarism/check", { text, project_id: projectId }).then((r) => r.data)
    ),
};