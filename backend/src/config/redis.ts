<<<<<<< HEAD
import { config } from "./env.js";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const Redis = require("ioredis");
const redis = new Redis(config.redisUrl);

redis.on("connect", () => console.log("✅ Redis connected"));
redis.on("error", (err: Error) => console.error("❌ Redis error:", err));

export default redis;
=======
import Redis from "ioredis";
import { config } from "./env";

const redis = new Redis(config.redisUrl);

redis.on("connect", () => console.log("✅ Redis connected"));
redis.on("error", (err) => console.error("❌ Redis error:", err));

export default redis;
>>>>>>> ai-service-fix
