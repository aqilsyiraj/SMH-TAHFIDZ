$ErrorActionPreference = "Stop"
Set-Location "C:\Users\iniha\Documents\Codex\2026-06-02\files-mentioned-by-the-user-bab"
& ".\.venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000 --noreload *> ".\work\runserver.log"
