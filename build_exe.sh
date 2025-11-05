#!/bin/bash
# Script pour créer un fichier .exe à partir du script Python
# Utilise PyInstaller pour compiler le script

echo "========================================"
echo "Compilation du script en fichier .exe"
echo "========================================"
echo ""

# Vérifier si PyInstaller est installé
python3 -c "import PyInstaller" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "PyInstaller n'est pas installé. Installation en cours..."
    pip3 install pyinstaller
    if [ $? -ne 0 ]; then
        echo "Erreur lors de l'installation de PyInstaller."
        exit 1
    fi
fi

echo ""
echo "Compilation en cours..."
echo ""

# Vérifier si un fichier .ico existe
ICON_FILE=""
if [ -f "icon.ico" ]; then
    ICON_FILE="--icon icon.ico"
    echo "Icône trouvée: icon.ico"
elif [ -f "mouse_mover.ico" ]; then
    ICON_FILE="--icon mouse_mover.ico"
    echo "Icône trouvée: mouse_mover.ico"
else
    echo "Aucune icône trouvée. Utilisation de l'icône par défaut."
    echo "Pour ajouter une icône, placez un fichier icon.ico ou mouse_mover.ico dans ce dossier."
fi

echo ""

# Créer le .exe avec PyInstaller
# Options:
# --onefile : Créer un seul fichier .exe
# --name : Nom du fichier .exe
# --clean : Nettoyer les fichiers temporaires
# --icon : Icône (optionnel)
# Utilisation de "python3 -m PyInstaller" pour éviter les problèmes de PATH

python3 -m PyInstaller --onefile --name mouse_mover --clean $ICON_FILE mouse_mover.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Erreur lors de la compilation."
    exit 1
fi

echo ""
echo "========================================"
echo "Compilation terminée avec succès!"
echo "========================================"
echo ""
echo "Le fichier .exe se trouve dans le dossier: dist/"
echo ""
echo "Vous pouvez maintenant utiliser mouse_mover.exe"
echo ""

