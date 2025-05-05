import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/process': 'http://127.0.0.1:5000',
      '/ping': 'http://127.0.0.1:5000'
    }
  }
})
