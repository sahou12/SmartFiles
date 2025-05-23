import tkinter as tk
from tkinter import simpledialog, messagebox
import os

from classification.app_classement import grouper_et_trier_fichiers, deplacer_fichiers_par_categorie
from recherche.recherche import recherche_mot_cle
from commentaires.gestion_utilisateurs import ajouter_commentaire

DOSSIER_CIBLE = "test_docs"

def rechercher():
    mot = simpledialog.askstring("🔍 Recherche", "Mot-clé à rechercher :")
    if mot:
        fichiers = recherche_mot_cle(DOSSIER_CIBLE, mot)
        if fichiers:
            resultats = "\n".join(fichiers)
            messagebox.showinfo("📄 Résultats", resultats)
        else:
            messagebox.showinfo("😕 Aucun résultat", "Aucun fichier trouvé.")

def classer():
    if os.path.isdir(DOSSIER_CIBLE):
        resultats = grouper_et_trier_fichiers(DOSSIER_CIBLE)
        deplacer_fichiers_par_categorie(resultats, DOSSIER_CIBLE)
        messagebox.showinfo("✅ Succès", "Les fichiers ont été classés.")
    else:
        messagebox.showerror("Erreur", f"Dossier introuvable : {DOSSIER_CIBLE}")

def commenter():
    utilisateur = simpledialog.askstring("👤 Utilisateur", "Nom de l'utilisateur :")
    fichier = simpledialog.askstring("📄 Fichier", "Nom du fichier :")
    commentaire = simpledialog.askstring("💬 Commentaire", "Votre commentaire :")

    if utilisateur and fichier and commentaire:
        ajouter_commentaire(utilisateur, fichier, commentaire)
        messagebox.showinfo("✅ Commentaire ajouté", "Le commentaire a été enregistré.")

# === Interface graphique ===
fenetre = tk.Tk()
fenetre.title("🧠 Application intelligente de fichiers")
fenetre.geometry("400x300")

tk.Label(fenetre, text="Que souhaitez-vous faire ?", font=("Arial", 14)).pack(pady=20)

tk.Button(fenetre, text="🔍 Rechercher un fichier", command=rechercher, width=30).pack(pady=5)
tk.Button(fenetre, text="🧠 Classer automatiquement", command=classer, width=30).pack(pady=5)
tk.Button(fenetre, text="🗒️ Ajouter un commentaire", command=commenter, width=30).pack(pady=5)
tk.Button(fenetre, text="🚪 Quitter", command=fenetre.quit, width=30).pack(pady=20)

fenetre.mainloop()
