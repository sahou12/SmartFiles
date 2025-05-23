import os
import shutil
from .classifieur_ai import predire_categorie
from pdfminer.high_level import extract_text as extract_text_pdf
from docx import Document  # pip install python-docx

def lire_contenu_fichier(chemin_fichier):
    _, extension = os.path.splitext(chemin_fichier)
    extension = extension[1:].lower()
    try:
        if extension == "txt":
            with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read(500).lower()
        elif extension == "pdf":
            return extract_text_pdf(chemin_fichier, maxpages=1).lower()
        elif extension == "docx":
            try:
                document = Document(chemin_fichier)
                texte_docx = ""
                for paragraph in document.paragraphs:
                    texte_docx += paragraph.text + "\n"
                return texte_docx[:500].lower()
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier DOCX {chemin_fichier}: {e}")
                return None
        else:
            return None
    except Exception as e:
        print(f"Erreur lors de la lecture de {chemin_fichier}: {e}")
        return None
def grouper_et_trier_fichiers(dossier):
    resultats_tri = {}

    for nom_fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, nom_fichier)
        if os.path.isfile(chemin_complet):
            _, extension = os.path.splitext(nom_fichier)
            extension = extension[1:].lower()
            categorie_predite = None

            if extension in ["jpg", "jpeg", "png", "gif"]:
                categorie = "Images"
            elif extension in ["mp4", "avi", "mov"]:
                categorie = "Vidéos"
            elif extension in ["mp3", "wav", "aac"]:
                categorie = "Audio"
            elif extension in ["txt", "pdf", "docx"]:
                contenu = lire_contenu_fichier(chemin_complet)
                if contenu:
                    categorie_predite = predire_categorie(contenu)
                categorie = categorie_predite if categorie_predite else "Non_Classifié"
            else:
                categorie = "Autres_Fichiers"

            resultats_tri[nom_fichier] = categorie

    return resultats_tri


def nom_similaire(nouveau_nom, anciens_noms):
    """
    Compare un nouveau nom de fichier à une liste de noms existants.
    Retourne True si un mot-clé commun est détecté.
    """
    mots_nouveau = set(nouveau_nom.lower().replace("_", " ").replace("-", " ").split())
    for ancien in anciens_noms:
        mots_ancien = set(ancien.lower().replace("_", " ").replace("-", " ").split())
        if len(mots_nouveau.intersection(mots_ancien)) >= 1:
            return True
    return False

def deplacer_fichiers_par_categorie(resultats, dossier_base):
    """
    Déplace les fichiers selon la catégorie IA,
    en vérifiant aussi la ressemblance avec les fichiers déjà présents dans chaque dossier.
    """

    dossiers_existants = [d for d in os.listdir(dossier_base) if os.path.isdir(os.path.join(dossier_base, d))]

    for fichier, categorie_predite in resultats.items():
        chemin_source = os.path.join(dossier_base, fichier)
        cible_finale = None

        # Étape 1 : essaie de trouver un dossier contenant un fichier similaire
        for dossier in dossiers_existants:
            chemin_dossier = os.path.join(dossier_base, dossier)
            fichiers_existant = os.listdir(chemin_dossier)

            if nom_similaire(fichier, fichiers_existant):
                cible_finale = chemin_dossier
                break

        # Étape 2 : sinon, regarde si le dossier de la catégorie existe déjà
        if not cible_finale:
            for dossier in dossiers_existants:
                if dossier.lower() == categorie_predite.lower():
                    cible_finale = os.path.join(dossier_base, dossier)
                    break

        # Étape 3 : sinon, crée un nouveau dossier
        if not cible_finale:
            cible_finale = os.path.join(dossier_base, categorie_predite)
            os.makedirs(cible_finale, exist_ok=True)
            dossiers_existants.append(categorie_predite)

        # Déplacement du fichier
        try:
            shutil.move(chemin_source, os.path.join(cible_finale, fichier))
        except Exception as e:
            print(f"❌ Erreur pour {fichier} → {e}")

if __name__ == "__main__":
    dossier_a_trier = input("📂 Entrez le chemin du dossier à trier : ").strip()
    if not os.path.isdir(dossier_a_trier):
        print("❌ Dossier introuvable.")
    else:
        resultats = grouper_et_trier_fichiers(dossier_a_trier)
        deplacer_fichiers_par_categorie(resultats, dossier_a_trier)
        print("🎉 Tri terminé.")
