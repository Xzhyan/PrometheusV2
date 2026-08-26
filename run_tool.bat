@echo off
@chcp 65001 > NUL

@REM Ativa o .venv e inicia a tool
.venv\Scripts\activate && python src\main.py

@REM Após finalizar a tool fecha a janela do cmd
exit