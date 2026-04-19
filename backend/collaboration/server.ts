import { Server } from "@hocuspocus/server";
import jwt from "jsonwebtoken";
<<<<<<< HEAD
import { config } from "../src/config/env.js";
=======
import { config } from "../src/config/env";
>>>>>>> ai-service-fix

const server = Server.configure({
  port: config.collabPort,

  async onAuthenticate({ token }) {
<<<<<<< HEAD
    if (!token) throw new Error("Missing authentication token");
=======
    if (!token) {
      throw new Error("Missing authentication token");
    }
>>>>>>> ai-service-fix
    try {
      const payload = jwt.verify(token, config.jwtSecret) as { userId: string };
      return { userId: payload.userId };
    } catch {
      throw new Error("Invalid or expired token");
    }
  },

<<<<<<< HEAD
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
=======
  async onConnect({ documentName }) {
    console.log(`📄 Document connected: ${documentName}`);
>>>>>>> ai-service-fix
  },
});

server.listen().then(() => {
  console.log(`🤝 UnderRoot Collaboration server running on port ${config.collabPort}`);
<<<<<<< HEAD
});
=======
});
>>>>>>> ai-service-fix
