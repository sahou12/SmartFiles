import json
import os

FICHIER_GROUPES = "groupes.json"
GROUPES_PAR_DEFAUT = ["RH", "Finance", "Communication", "IT", "Direction", "Stagiaires"]

# Initialisation automatique des groupes
def initialiser_groupes():
    if not os.path.exists(FICHIER_GROUPES):
        data = {groupe: {"__global__": []} for groupe in GROUPES_PAR_DEFAUT}
        with open(FICHIER_GROUPES, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

# Ajouter un commentaire (chat ou fichier spécifique)
def ajouter_commentaire(groupe, utilisateur, fichier, commentaire):
    initialiser_groupes()
    with open(FICHIER_GROUPES, "r", encoding="utf-8") as f:
        data = json.load(f)

    if groupe not in data:
        data[groupe] = {}

    if fichier not in data[groupe]:
        data[groupe][fichier] = []

    data[groupe][fichier].append({"utilisateur": utilisateur, "commentaire": commentaire})

    with open(FICHIER_GROUPES, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def lire_commentaires(groupe, fichier=None):
    initialiser_groupes()
    with open(FICHIER_GROUPES, "r", encoding="utf-8") as f:
        data = json.load(f)

    if fichier:
        return data.get(groupe, {}).get(fichier, [])
    else:
        return data.get(groupe, {})  # retourne tout le groupe (tous les fichiers)


# Créer un groupe
def creer_groupe(nom_groupe):
    initialiser_groupes()
    with open(FICHIER_GROUPES, "r", encoding="utf-8") as f:
        data = json.load(f)

    if nom_groupe not in data:
        data[nom_groupe] = {}
        with open(FICHIER_GROUPES, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    return False

# Lister tous les groupes existants
def liste_groupes():
    initialiser_groupes()
    with open(FICHIER_GROUPES, "r", encoding="utf-8") as f:
        data = json.load(f)
    return list(data.keys())
