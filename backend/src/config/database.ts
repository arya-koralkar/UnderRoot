import { Pool } from "pg";
import mongoose from "mongoose";
<<<<<<< HEAD
import { config } from "./env.js";
=======
import { config } from "./env";
>>>>>>> ai-service-fix

export const pgPool = new Pool({ connectionString: config.databaseUrl });

pgPool.on("connect", () => console.log("✅ PostgreSQL connected"));
pgPool.on("error", (err) => console.error("❌ PostgreSQL error:", err));

export async function connectMongo() {
  try {
    await mongoose.connect(config.mongodbUrl);
    console.log("✅ MongoDB connected");
  } catch (err) {
    console.error("❌ MongoDB connection error:", err);
  }
}
