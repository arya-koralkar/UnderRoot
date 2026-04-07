import axios from "axios";

export type ApiSuccess<T> = {
  success: true;
  data: T;
  meta?: { cached?: boolean };
};

export type ApiError = {
  success: false;
  error: { code: string; message: string };
};

export type ApiResponse<T> = ApiSuccess<T> | ApiError;

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:4000",
});

api.interceptors.request.use((config) => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("underroot_token");
    if (token) config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const citationAPI = {
  suggest: (text: string, projectId?: string) =>
    api.post<ApiResponse<{ citations?: unknown[] }>>("/api/citations/suggest", { text, projectId }),
};

export const plagiarismAPI = {
  check: (text: string, projectId?: string) =>
    api.post<ApiResponse<unknown>>("/api/plagiarism/check", { text, projectId }),
};

export default api;