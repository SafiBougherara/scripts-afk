# Script de simulation d'activité

Un script Python qui simule des mouvements de souris et/ou des frappes de touches pour maintenir l'activité de votre ordinateur. Utile pour éviter que votre système passe en veille ou pour maintenir votre statut "actif" sur certaines applications.

## 📋 Fonctionnalités

- **Simulation de mouvement de souris** : Déplace la souris de manière subtile et aléatoire
- **Simulation de frappes de touches** : Appuie sur des touches aléatoires (z, q, s, d)
- **Trois modes d'utilisation** :
  1. Mouvement de souris seulement
  2. Mouvement de souris + touches aléatoires
  3. Touches aléatoires seulement
- **Durée configurable** : Fonctionne pendant 1 heure, avec possibilité de renouvellement
- **Barre de progression verte** : Affiche une barre de progression visuelle avec le temps restant
- **Timeout automatique** : Si aucune réponse n'est donnée dans la minute qui suit la demande de renouvellement, le script s'arrête automatiquement

## 🔧 Prérequis

- **Python 3.6 ou supérieur**
- **pip** (gestionnaire de paquets Python)

## 📦 Installation

### 1. Cloner ou télécharger le projet

Naviguez vers le répertoire du projet dans votre terminal :

```bash
cd scripts-autre
```

### 2. Créer un environnement virtuel (recommandé)

Créer un environnement virtuel permet d'isoler les dépendances du projet :

**Sur Windows :**
```bash
python -m venv venv
```

**Sur Linux/Mac :**
```bash
python3 -m venv venv
```

### 3. Activer l'environnement virtuel

**Sur Windows :**
```bash
venv\Scripts\activate
```

**Sur Linux/Mac :**
```bash
source venv/bin/activate
```

Une fois activé, vous devriez voir `(venv)` au début de votre ligne de commande.

### 4. Installer les dépendances

Installez les packages nécessaires avec pip :

```bash
pip install -r requirements.txt
```

Cela installera automatiquement `pyautogui` (version 0.9.54 ou supérieure).

## 🚀 Utilisation

### Lancer le script

Une fois l'environnement virtuel activé et les dépendances installées, lancez le script :

```bash
python mouse_mover.py
```

### Sélection du mode

Au démarrage, le script vous demandera de choisir un mode :

```
Choisissez un mode:
  1 - Mouvement de souris seulement
  2 - Mouvement de souris + touches z/q/s/d aléatoires
  3 - Touches z/q/s/d aléatoires seulement

Votre choix (1, 2 ou 3):
```

Tapez `1`, `2` ou `3` selon le mode souhaité, puis appuyez sur Entrée.

### Fonctionnement

- Le script fonctionne pendant **1 heure** (3600 secondes)
- Les actions (mouvement de souris ou frappe de touches) se produisent à intervalles aléatoires entre **4 et 7 secondes**
- Une **barre de progression verte** affiche le temps restant en temps réel
- Vous pouvez arrêter le script à tout moment avec **Ctrl+C**

### Renouvellement

Après 1 heure, le script vous demandera si vous souhaitez continuer :

```
Voulez-vous renouveler pour une autre heure? (OUI/NON):
```

- Répondez **OUI** (ou **O**, **YES**, **Y**) pour continuer pour une autre heure
- Répondez **NON** (ou n'importe quelle autre réponse) pour arrêter
- Si vous ne répondez pas dans **60 secondes**, le script s'arrête automatiquement

## 📝 Désactiver l'environnement virtuel

Quand vous avez terminé, vous pouvez désactiver l'environnement virtuel :

```bash
deactivate
```

## 📦 Créer un fichier .exe (Windows)

Si vous souhaitez créer un fichier exécutable Windows (.exe) pour pouvoir lancer le script sans avoir Python installé, vous pouvez utiliser **PyInstaller**.

### Méthode 1 : Utiliser le script batch (recommandé)

Un script batch est fourni pour faciliter la compilation :

**Sur Windows :**
```bash
build_exe.bat
```

**Sur Linux/Mac :**
```bash
chmod +x build_exe.sh
./build_exe.sh
```

Le script installera automatiquement PyInstaller s'il n'est pas déjà installé, puis compilera le script.

### Méthode 2 : Compilation manuelle

1. **Installer PyInstaller** :

```bash
pip install pyinstaller
```

2. **Créer le fichier .exe** :

```bash
pyinstaller --onefile --name mouse_mover --clean mouse_mover.py
```

3. **Trouver le fichier .exe** :

Le fichier `mouse_mover.exe` sera créé dans le dossier `dist/`.

### Options de compilation

- `--onefile` : Crée un seul fichier .exe (plus pratique pour la distribution)
- `--name mouse_mover` : Définit le nom du fichier exécutable
- `--clean` : Nettoie les fichiers temporaires avant la compilation
- `--noconsole` : Masque la console (optionnel, à ajouter si vous ne voulez pas voir la fenêtre de terminal)

**Exemple avec console masquée :**
```bash
pyinstaller --onefile --noconsole --name mouse_mover --clean mouse_mover.py
```

### Changer l'icône du .exe

Pour personnaliser l'icône de votre fichier .exe :

1. **Obtenir ou créer un fichier .ico** :
   - Trouvez une icône sur internet (format .ico)
   - Ou convertissez une image (PNG, JPG) en .ico en utilisant un convertisseur en ligne (par exemple : [convertio.co](https://convertio.co/png-ico/))

2. **Placer le fichier .ico dans le dossier du projet** :
   - Renommez-le `icon.ico` ou `mouse_mover.ico`
   - Placez-le dans le même dossier que `mouse_mover.py`

3. **Recompiler le .exe** :
   - Le script `build_exe.bat` détectera automatiquement le fichier .ico et l'utilisera
   - Ou manuellement : `pyinstaller --onefile --name mouse_mover --icon icon.ico --clean mouse_mover.py`

**Note** : Le fichier .ico doit être au format Windows (icône) et peut contenir plusieurs tailles (16x16, 32x32, 48x48, 256x256 pixels) pour une meilleure qualité.

### Note importante

Le fichier .exe créé sera assez volumineux (environ 10-20 MB) car il inclut Python et toutes les dépendances nécessaires. C'est normal et nécessaire pour que le .exe fonctionne sur des machines sans Python installé.

## ⚠️ Notes importantes

1. **Interruption du script** : Vous pouvez arrêter le script à tout moment avec `Ctrl+C`

2. **Sécurité** : Le script utilise `pyautogui` pour simuler des mouvements de souris et des frappes de touches. Assurez-vous de ne pas avoir d'autres applications sensibles ouvertes pendant l'exécution.

3. **Touches simulées** : En mode 2 ou 3, le script appuie sur les touches `z`, `q`, `s`, `d`. Assurez-vous qu'aucune application sensible ne reçoit ces entrées.

4. **Performance** : Le script consomme très peu de ressources CPU et RAM.

5. **Compatibilité** : Le script fonctionne sur Windows, Linux et macOS.

## 📄 Structure du projet

```
scripts-autre/
├── mouse_mover.py      # Script principal
├── requirements.txt    # Dépendances Python
├── README.md          # Documentation (ce fichier)
├── build_exe.bat      # Script batch pour créer le .exe (Windows)
├── build_exe.sh        # Script shell pour créer le .exe (Linux/Mac)
├── venv/              # Environnement virtuel (créé après installation)
└── dist/              # Dossier contenant le .exe (créé après compilation)
```

## 🐛 Dépannage

### Erreur : "ModuleNotFoundError: No module named 'pyautogui'"

**Solution** : Assurez-vous que :
- L'environnement virtuel est activé (vous voyez `(venv)` dans votre terminal)
- Les dépendances sont installées : `pip install -r requirements.txt`

### Erreur : "pyautogui.FailSafeException"

**Solution** : Cette erreur ne devrait pas se produire car le failsafe est désactivé dans le script. Si cela arrive, vérifiez que vous utilisez la dernière version du script.

### Le script ne bouge pas la souris

**Solution** : Vérifiez que :
- Vous avez sélectionné le mode 1 ou 2 (pas le mode 3)
- Aucun autre programme ne bloque les mouvements de souris
- Vous avez les permissions nécessaires sur votre système

## 📝 Licence

Ce script est fourni tel quel, sans garantie. Utilisez-le à vos propres risques.

## 🤝 Contribution

Les suggestions d'amélioration sont les bienvenues !

---

**Note** : Ce script est destiné à des fins éducatives et de test. Utilisez-le de manière responsable et conformément aux politiques de votre organisation.

