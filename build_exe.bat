@echo off
REM Script pour créer un fichier .exe à partir du script Python
REM Utilise PyInstaller pour compiler le script

echo ========================================
echo Compilation du script en fichier .exe
echo ========================================
echo.

REM Vérifier si PyInstaller est installé
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller n'est pas installe. Installation en cours...
    pip install pyinstaller
    if errorlevel 1 (
        echo Erreur lors de l'installation de PyInstaller.
        pause
        exit /b 1
    )
)

echo.
echo Compilation en cours...
echo.

REM Créer le .exe avec PyInstaller
REM Options:
REM --onefile : Créer un seul fichier .exe
REM --noconsole : Ne pas afficher la console (optionnel, commenté pour voir les logs)
REM --name : Nom du fichier .exe
REM --icon : Icône (optionnel, à ajouter si vous avez une icône .ico)

pyinstaller --onefile --name mouse_mover --clean mouse_mover.py

if errorlevel 1 (
    echo.
    echo Erreur lors de la compilation.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Compilation terminee avec succes!
echo ========================================
echo.
echo Le fichier .exe se trouve dans le dossier: dist\
echo.
echo Vous pouvez maintenant utiliser mouse_mover.exe
echo.
pause

