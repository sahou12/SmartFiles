import os
import fitz  # pip install PyMuPDF
from docx import Document  # pip install python-docx

def lire_txt(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[Erreur TXT] {path} → {e}")
        return ""

def lire_docx(path):
    try:
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"[Erreur DOCX] {path} → {e}")
        return ""

def lire_pdf(path):
    try:
        doc = fitz.open(path)
        return "\n".join([page.get_text() for page in doc])
    except Exception as e:
        print(f"[Erreur PDF] {path} → {e}")
        return ""

def lire_contenu_fichier(path):
    ext = path.lower()
    if ext.endswith(".txt"):
        return lire_txt(path)
    elif ext.endswith(".docx"):
        return lire_docx(path)
    elif ext.endswith(".pdf"):
        return lire_pdf(path)
    else:
        return ""

def recherche_mot_cle(dossier, mot):
    fichiers_trouves = []
    extensions_autorisees = [".txt", ".docx", ".pdf"]

    for root, _, files in os.walk(dossier):
        for nom_fichier in files:
            if any(nom_fichier.lower().endswith(ext) for ext in extensions_autorisees):
                chemin = os.path.join(root, nom_fichier)
                try:
                    contenu = lire_contenu_fichier(chemin)
                    if mot.lower() in contenu.lower():
                        fichiers_trouves.append(chemin)
                except Exception as e:
                    print(f"[Erreur lecture] {chemin} → {e}")

    return fichiers_trouves

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def recherche_semantique(dossier, requete, seuil_similarite=0.5):
    fichiers_resultats = []
    fichiers_textes = []
    chemins_fichiers = []

    for root, _, files in os.walk(dossier):
        for nom in files:
            if nom.lower().endswith((".txt", ".docx", ".pdf")):
                chemin = os.path.join(root, nom)
                contenu = lire_contenu_fichier(chemin)
                if contenu.strip():
                    fichiers_textes.append(contenu)
                    chemins_fichiers.append(chemin)

    if not fichiers_textes:
        return []

    embeddings = model.encode(fichiers_textes, convert_to_tensor=True)
    requete_embedding = model.encode(requete, convert_to_tensor=True)
    similarites = util.cos_sim(requete_embedding, embeddings)[0]

    for i, score in enumerate(similarites):
        if score >= seuil_similarite:
            fichiers_resultats.append((chemins_fichiers[i], float(score)))

    fichiers_resultats.sort(key=lambda x: x[1], reverse=True)
    return fichiers_resultats



