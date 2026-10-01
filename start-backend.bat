@echo off
setlocal
title Video Downloader Pro - Backend Server

echo ==============================================
echo  Video Downloader Pro - Backend Server Start
echo ==============================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Virtual environment not found. Please run 'uv venv' and 'uv pip install -r pyproject.toml' first.
    pause
    exit /b 1
)

echo [INFO] Starting FastAPI Backend on port 8001...
start "FastAPI Backend" cmd /c ".\.venv\Scripts\python.exe -m uvicorn backend.app:app --host 127.0.0.1 --port 8001"

echo [INFO] Waiting 3 seconds for server to start...
timeout /t 3 /nobreak >nul

echo [INFO] Starting Cloudflare Quick Tunnel...
echo.
echo =========================================================
echo  IMPORTANT: Look for the URL ending in trycloudflare.com
echo  Copy that URL and paste it into the "Backend Settings"
echo  of the public demo website to connect it!
echo =========================================================
echo.

npx -y cloudflared tunnel --url http://127.0.0.1:8001

pause
