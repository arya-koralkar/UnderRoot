import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import { config } from "./config/env.js";
import { connectMongo } from "./config/database.js";
import citationRoutes from "./routes/citation.routes.js";
import plagiarismRoutes from "./routes/plagiarism.routes.js";

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json({ limit: "10mb" }));

// Health check
app.get("/health", (_req, res) => {
  res.json({ status: "ok", service: "underroot-backend" });
});

// Routes
app.use("/api/citations", citationRoutes);
app.use("/api/plagiarism", plagiarismRoutes);

async function start() {
  await connectMongo();
  app.listen(config.port, () => {
    console.log(`🚀 UnderRoot Backend running on port ${config.port}`);
  });
}

start().catch(console.error);

export default app;