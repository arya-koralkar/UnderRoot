import { Server } from "@hocuspocus/server";
import jwt from "jsonwebtoken";
import { config } from "../src/config/env.js";

const server = Server.configure({
  port: config.collabPort,

  async onAuthenticate({ token }) {
    if (!token) throw new Error("Missing authentication token");
    try {
      const payload = jwt.verify(token, config.jwtSecret) as { userId: string };
      return { userId: payload.userId };
    } catch {
      throw new Error("Invalid or expired token");
    }
  },

  async onConnect({ documentName, context }) {
    if (!documentName?.trim()) throw new Error("Invalid document name");
    console.log(
      JSON.stringify({
        event: "collab_connect",
        documentName,
        userId: (context as { userId?: string })?.userId ?? null,
        ts: new Date().toISOString(),
      })
    );
  },
});

server.listen().then(() => {
  console.log(`🤝 UnderRoot Collaboration server running on port ${config.collabPort}`);
});