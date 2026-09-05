@echo off
@chcp 65001 > nul
.venv\Scripts\activate && python src\main.py
exit /b