import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Minimal Vite config for the POC frontend skeleton (SPEC-02).
export default defineConfig({
  plugins: [react()],
});
