import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// The base path is "./" (relative) by default so the same build works on:
//   - a project site:  https://USER.github.io/REPO/
//   - a user site:     https://USER.github.io/
//   - any static host or sub-folder
// Hash-based routing (#/path) means no server rewrites are needed.
// Override with VITE_BASE_PATH (e.g. "/pakistan-legal-guide/") if you prefer absolute paths.
export default defineConfig(() => ({
  base: process.env.VITE_BASE_PATH || './',
  plugins: [react()],
  build: {
    outDir: 'dist',
    sourcemap: false,
  },
  test: {
    environment: 'node',
    include: ['src/**/*.test.ts'],
  },
}))
