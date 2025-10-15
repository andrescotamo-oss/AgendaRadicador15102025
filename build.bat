@echo off
SET SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
pyinstaller --clean build.spec
echo EXE: dist\AgendaRadicador.exe
pause
