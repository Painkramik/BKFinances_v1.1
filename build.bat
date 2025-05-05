@echo off
echo Compilation de BKFinances v1.1...

REM Compilation sans icône
pyinstaller --onefile --windowed bkfinances.py

echo.
echo Compilation terminée !
echo Le fichier BKFinances.exe se trouve dans le dossier "dist"
pause
