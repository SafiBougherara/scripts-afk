#!/usr/bin/env python3
"""
Script pour simuler des mouvements de souris afin de maintenir l'activité.
Le script bouge la souris pendant 1 heure, puis demande si on veut continuer.
"""

import pyautogui
import time
import threading
import sys
import random

# Désactiver la sécurité de pyautogui (pour éviter les erreurs si la souris sort de l'écran)
pyautogui.FAILSAFE = False

# Variable globale pour stocker la réponse de l'utilisateur
user_response = None

def get_user_input_with_timeout(prompt, timeout_seconds=60):
    """Demande une entrée utilisateur avec un timeout."""
    global user_response
    
    user_response = None
    input_received = threading.Event()
    
    def input_thread():
        global user_response
        try:
            result = input(prompt).strip().upper()
            user_response = result
            input_received.set()
        except:
            pass
    
    # Démarrer le thread pour l'input
    thread = threading.Thread(target=input_thread)
    thread.daemon = True
    thread.start()
    
    # Attendre soit la réponse, soit le timeout
    if not input_received.wait(timeout=timeout_seconds):
        # Timeout atteint
        print("\nPas de réponse dans la minute. Arrêt du script.")
        return "NON"
    
    if user_response in ["OUI", "O", "YES", "Y"]:
        return "OUI"
    else:
        return "NON"

def move_mouse_subtle():
    """Bouge la souris de manière subtile."""
    try:
        # Bouger la souris de quelques pixels de manière aléatoire mais subtile
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        
        # Bouger vers la nouvelle position de manière fluide
        pyautogui.moveRel(offset_x, offset_y, duration=0.1)
        
        return True
    except Exception as e:
        print(f"Erreur lors du mouvement de la souris: {e}")
        return False

def press_random_keys():
    """Appuie sur une touche aléatoire parmi z, q, s, d."""
    try:
        keys = ['z', 'q', 's', 'd']
        key = random.choice(keys)
        pyautogui.press(key)
        return True
    except Exception as e:
        print(f"Erreur lors de l'appui sur une touche: {e}")
        return False

def print_progress_bar(elapsed, total_duration, bar_length=50):
    """Affiche une barre de progression verte avec le temps restant."""
    progress = elapsed / total_duration
    filled_length = int(bar_length * progress)
    
    # Codes couleur ANSI pour vert
    GREEN = '\033[92m'
    RESET = '\033[0m'
    
    # Barre de progression
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    # Calculer le temps restant
    remaining = total_duration - elapsed
    remaining_minutes = int(remaining // 60)
    remaining_seconds = int(remaining % 60)
    
    # Format: [████████████░░░░░░░░] 45:30 restant
    progress_text = f"\r[{GREEN}{bar}{RESET}] {remaining_minutes:02d}:{remaining_seconds:02d} restant"
    sys.stdout.write(progress_text)
    sys.stdout.flush()

def select_mode():
    """Affiche un menu et demande à l'utilisateur de choisir un mode."""
    print("=" * 60)
    print("Script de simulation d'activité")
    print("=" * 60)
    print("\nChoisissez un mode:")
    print("  1 - Mouvement de souris seulement")
    print("  2 - Mouvement de souris + touches z/q/s/d aléatoires")
    print("  3 - Touches z/q/s/d aléatoires seulement")
    print()
    
    while True:
        try:
            choice = input("Votre choix (1, 2 ou 3): ").strip()
            if choice in ['1', '2', '3']:
                return int(choice)
            else:
                print("Veuillez entrer 1, 2 ou 3.")
        except (EOFError, KeyboardInterrupt):
            print("\n\nScript interrompu par l'utilisateur.")
            sys.exit(0)

def main():
    # Sélection du mode
    mode = select_mode()
    
    # Définir le nom du mode pour l'affichage
    mode_names = {
        1: "Mouvement de souris seulement",
        2: "Mouvement de souris + touches z/q/s/d aléatoires",
        3: "Touches z/q/s/d aléatoires seulement"
    }
    
    print(f"\nMode sélectionné: {mode_names[mode]}")
    print("Le script va fonctionner pendant 1 heure.")
    print("Vous pouvez l'arrêter à tout moment avec Ctrl+C.\n")
    
    # Durée totale: 1 heure = 3600 secondes
    total_duration = 3600  # 1 heure en secondes
    start_time = time.time()
    last_movement_time = start_time
    last_key_press_time = start_time
    last_progress_update = start_time
    next_movement_interval = random.uniform(4, 7)  # Premier intervalle de mouvement
    next_key_interval = random.uniform(4, 7)  # Premier intervalle pour les touches
    
    # Afficher la barre de progression initiale
    print_progress_bar(0, total_duration)
    
    while True:
        current_time = time.time()
        elapsed = current_time - start_time
        
        # Vérifier si on a atteint 1 heure
        if elapsed >= total_duration:
            # Afficher la barre complète avant de demander le renouvellement
            print_progress_bar(total_duration, total_duration)
            print("\n" + "=" * 60)
            print("Une heure s'est écoulée!")
            print("=" * 60)
            
            # Demander si on veut continuer
            response = get_user_input_with_timeout(
                "\nVoulez-vous renouveler pour une autre heure? (OUI/NON): ",
                timeout_seconds=60
            )
            
            if response == "OUI":
                print("\nRenouvellement accepté. Continuation pour une autre heure...\n")
                start_time = time.time()  # Réinitialiser le timer
                last_movement_time = start_time
                last_key_press_time = start_time
                last_progress_update = start_time
                next_movement_interval = random.uniform(4, 7)  # Nouvel intervalle
                next_key_interval = random.uniform(4, 7)  # Nouvel intervalle pour les touches
                print_progress_bar(0, total_duration)  # Réinitialiser la barre
                continue
            else:
                print("\nArrêt du script.")
                break
        
        # Mode 1: Mouvement de souris seulement
        # Mode 2: Mouvement de souris + touches
        if mode in [1, 2]:
            time_since_last_movement = current_time - last_movement_time
            if time_since_last_movement >= next_movement_interval:
                move_mouse_subtle()
                last_movement_time = time.time()
                next_movement_interval = random.uniform(4, 7)  # Prochain intervalle aléatoire
        
        # Mode 2: Mouvement de souris + touches
        # Mode 3: Touches seulement
        if mode in [2, 3]:
            time_since_last_key = current_time - last_key_press_time
            if time_since_last_key >= next_key_interval:
                press_random_keys()
                last_key_press_time = time.time()
                next_key_interval = random.uniform(4, 7)  # Prochain intervalle aléatoire
        
        # Mettre à jour la barre de progression toutes les secondes
        time_since_last_progress = current_time - last_progress_update
        if time_since_last_progress >= 1:  # Mise à jour chaque seconde
            print_progress_bar(elapsed, total_duration)
            last_progress_update = current_time
        
        # Petite pause pour éviter de surcharger le CPU
        time.sleep(0.1)  # Réduire à 0.1 seconde pour une mise à jour plus fluide

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScript interrompu par l'utilisateur.")
        sys.exit(0)

