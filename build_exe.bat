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

REM Vérifier si un fichier .ico existe
set ICON_FILE=
if exist "icon.ico" (
    set ICON_FILE=--icon icon.ico
    echo Icône trouvée: icon.ico
) else if exist "mouse_mover.ico" (
    set ICON_FILE=--icon mouse_mover.ico
    echo Icône trouvée: mouse_mover.ico
) else (
    echo Aucune icône trouvée. Utilisation de l'icône par défaut.
    echo Pour ajouter une icône, placez un fichier icon.ico ou mouse_mover.ico dans ce dossier.
)

echo.

REM Créer le .exe avec PyInstaller
REM Options:
REM --onefile : Créer un seul fichier .exe
REM --noconsole : Ne pas afficher la console (optionnel, commenté pour voir les logs)
REM --name : Nom du fichier .exe
REM --icon : Icône (optionnel, à ajouter si vous avez une icône .ico)
REM Utilisation de "python -m PyInstaller" pour éviter les problèmes de PATH

python -m PyInstaller --onefile --name mouse_mover --clean %ICON_FILE% mouse_mover.py

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

