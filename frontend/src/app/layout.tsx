import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "UnderRoot — AI-Powered Research Writing",
  description:
    "Real-time collaborative research paper writing with AI citation suggestions and plagiarism detection.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
