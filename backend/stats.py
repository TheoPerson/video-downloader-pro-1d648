import sqlite3
import time
from pathlib import Path

from .config import settings

class StatsManager:
    def __init__(self):
        self.db_path = settings.download_path / "stats.db"
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS stats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    job_id TEXT UNIQUE,
                    url TEXT,
                    quality TEXT,
                    format TEXT,
                    codec TEXT,
                    enhance BOOLEAN,
                    success BOOLEAN,
                    file_size INTEGER,
                    duration_seconds INTEGER,
                    created_at INTEGER
                )
            ''')
            conn.commit()

    def record_job(self, job_dict: dict):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT OR REPLACE INTO stats 
                    (job_id, url, quality, format, codec, enhance, success, file_size, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    job_dict.get("id"),
                    job_dict.get("url"),
                    job_dict.get("quality"),
                    job_dict.get("format", "mp4"),
                    job_dict.get("codec", "h264"),
                    1 if job_dict.get("enhance") else 0,
                    1 if job_dict.get("state") == "ready" else 0,
                    job_dict.get("file_size", 0),
                    int(job_dict.get("created_at", time.time()))
                ))
                conn.commit()
        except Exception as e:
            print(f"Stats Error: {e}")

    def get_summary(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                
                # Total jobs
                cur.execute("SELECT COUNT(*) as count FROM stats")
                total_jobs = cur.fetchone()["count"]
                
                # Successful jobs
                cur.execute("SELECT COUNT(*) as count FROM stats WHERE success = 1")
                successful_jobs = cur.fetchone()["count"]
                
                # Total data processed
                cur.execute("SELECT SUM(file_size) as total_bytes FROM stats WHERE success = 1")
                total_bytes = cur.fetchone()["total_bytes"] or 0
                
                # Formats
                cur.execute("SELECT format, COUNT(*) as count FROM stats GROUP BY format")
                formats = {row["format"]: row["count"] for row in cur.fetchall()}
                
                # Enhancements
                cur.execute("SELECT COUNT(*) as count FROM stats WHERE enhance = 1")
                enhanced_count = cur.fetchone()["count"]
                
                return {
                    "total_jobs": total_jobs,
                    "successful_jobs": successful_jobs,
                    "total_bytes": total_bytes,
                    "formats": formats,
                    "enhanced_count": enhanced_count
                }
        except Exception as e:
            print(f"Stats Error: {e}")
            return {}

stats_manager = StatsManager()
