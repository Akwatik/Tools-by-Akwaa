import subprocess
import tkinter as tk
from tkinter import ttk

def lister_profils_wifi():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Erreur lors de la récupération des profils : {e}"

def obtenir_mot_de_passe(nom_reseau):
    try:
        result = subprocess.run(["netsh", "wlan", "show", "profile", nom_reseau, "key=clear"], capture_output=True, text=True)
        # Chercher la ligne contenant "Key Content"
        for ligne in result.stdout.splitlines():
            if "Key Content" in ligne:
                return ligne.split(":")[1].strip()
        return "Mot de passe non trouvé"
    except Exception as e:
        return f"Erreur lors de la récupération du mot de passe : {e}"

def afficher_profils_wifi():
    result = lister_profils_wifi()
    texte_affichage.delete(1.0, tk.END) 
    for ligne in result.splitlines():
        if "Tous les profils utilisateurs" in ligne:
            nom_reseau = ligne.split(":")[1].strip()
            mot_de_passe = obtenir_mot_de_passe(nom_reseau)
            texte_affichage.insert(tk.END, f"Réseau : {nom_reseau}\nMot de passe : {mot_de_passe}\n\n")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Profils Wi-Fi et mots de passe")
fenetre.geometry("600x400")

# Titre stylé
titre = ttk.Label(fenetre, text="Liste des réseaux Wi-Fi enregistrés", font=("Helvetica", 16, "bold"))
titre.pack(pady=10)

# Bouton pour afficher les profils Wi-Fi
btn_profils = ttk.Button(fenetre, text="Afficher les réseaux et mots de passe", command=afficher_profils_wifi)
btn_profils.pack(pady=10)

texte_affichage = tk.Text(fenetre, wrap=tk.WORD, height=15, width=70)
texte_affichage.pack(pady=10)

# Lancer l'application
fenetre.mainloop()