<p align="center">
  <img src="assets/banner.svg" alt="Video Downloader Pro" width="100%">
</p>

<h1 align="center">Video Downloader Pro</h1>

<p align="center">
  <strong>A premium, self-hosted media utility optimized for iOS Safari.</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#installation">Installation</a> •
  <a href="#tech-stack">Tech Stack</a>
</p>

---

## 📱 The Mobile-First Download Experience

Most web-based video downloaders suffer on iOS: Safari intercepts `video/mp4` files and forces them into an inline player, making actual file saving a nightmare.

**Video Downloader Pro** solves this fundamentally. By proxying the media through a custom FastAPI backend, streams are re-encoded and served with `application/octet-stream` and `X-Content-Type-Options: nosniff`. 

The result? **A native "Do you want to download..." prompt on iOS Safari**, saving the video directly to your Files app, even over 5G.

## ✨ Features

- **Public UI Demo & BYOB Architecture:** The UI can be hosted statically, allowing users to "Bring Your Own Backend" by plugging in their local server URL.
- **Smart Formatting:** 1-Click MKV/MP4 selection and forced HEVC (H.265) compression.
- **Magic Enhance:** FFmpeg algorithms applied instantly to boost audio clarity (loudnorm) and video sharpness (unsharp mask).
- **Download History:** LocalStorage-based download history to manage past files.
- **Stats Dashboard:** Built-in SQLite tracking for project managers to monitor usage metrics and success rates.
- **Silky UX**: Rebuilt from the ground up with Framer Motion, glassmorphism, and Lucide icons.
- **Format Merging**: Extracts 1080p/4K video streams and seamlessly remuxes them with high-quality audio using local FFmpeg.

## 🏗 Architecture

- **Frontend**: Next.js 16 (App Router), React, Tailwind CSS, Framer Motion.
- **Backend**: Python 3.12, FastAPI, yt-dlp, FFmpeg, SQLite.
- **Data Flow**: `URL Paste` → `FastAPI Analysis` → `React Preview` → `yt-dlp Engine` → `FFmpeg Remux` → `Native OS Download`.

## 🚀 Live Demo & How to Run

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FTheoPerson%2Fvideo-downloader-pro&root-directory=frontend)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/TheoPerson/video-downloader-pro&dir=frontend)

Because the backend relies on heavy binaries (`ffmpeg`, `ffprobe`), the best way to experience the app is to run the backend locally while using the public web UI!

### 1. Run the Backend Server
On your Windows PC, double-click the `start-backend.bat` script, or run:
```bash
.\start-backend.bat
```
*This script will automatically start the FastAPI server and spin up a secure Cloudflare Tunnel, giving you a temporary public URL for your backend.*

### 2. Connect the UI
Open the public frontend (or run it locally via `cd frontend && npm run dev`). 
Click **"Backend Settings"** in the footer, paste the Cloudflare Tunnel URL you got from step 1, and you're good to go!

---

## 💻 Manual Developer Setup

### Local Development (Windows / macOS / Linux)

1. **Clone & Setup Backend**
```bash
uv venv
uv pip install -e ".[dev]"
uv run uvicorn backend.app:app --host 0.0.0.0 --port 8001
```

2. **Setup Frontend**
```bash
cd frontend
npm install
npm run dev
```

3. **Visit** `http://localhost:3000`

### Docker (Production)

```bash
docker compose up -d --build
```

---
*Built for authorized personal use. Please respect content copyrights.*
