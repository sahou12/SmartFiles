from classifieur_ai import entraîner_classifieur
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Données enrichies
exemples = [
    ("Facture EDF du 15 avril 2023", "Facture"),
    ("Facture Amazon - Commande 12345", "Facture"),
    ("Facture mensuelle Internet Orange", "Facture"),
    ("Reçu de paiement de la taxe foncière", "Facture"),
    ("Devis pour la rénovation de cuisine", "Devis"),
    ("Proposition de devis - société BTP", "Devis"),
    ("Estimation du projet peinture", "Devis"),
    ("Offre tarifaire pour travaux électriques", "Devis"),
    ("Rapport trimestriel des ventes", "Rapport"),
    ("Rapport de stage - entreprise L'Oréal", "Rapport"),
    ("Analyse financière annuelle", "Rapport"),
    ("Compte-rendu de réunion du 23 mai", "Rapport"),
    ("Résumé de biologie - chapitre 3", "Notes"),
    ("Fiche de révision histoire-géo", "Notes"),
    ("Cours de macroéconomie L1", "Notes"),
    ("Introduction aux probabilités", "Notes"),
    ("Contrat de travail à durée déterminée", "Contrat"),
    ("Accord de location meublée", "Contrat"),
    ("Conditions générales de vente", "Contrat"),
    ("Contrat d’assurance habitation", "Contrat"),
    ("Curriculum Vitae - Julie Dupont", "CV"),
    ("Mon CV 2024 - développeur web", "CV"),
    ("Expériences professionnelles et compétences", "CV"),
    ("Profil LinkedIn exporté", "CV"),
    ("Lettre de motivation pour master RH", "Lettre"),
    ("Lettre de recommandation étudiant", "Lettre"),
    ("Lettre de démission", "Lettre"),
    ("Lettre administrative - demande de logement", "Lettre"),
    ("Objet : relance de facture impayée", "Mail"),
    ("Message de suivi de candidature", "Mail"),
    ("Email de confirmation de rendez-vous", "Mail"),
    ("Bonjour, voici le compte rendu de la réunion", "Mail"),
]

# Séparation en données d'entraînement et de test
textes, labels = zip(*exemples)
X_train, X_test, y_train, y_test = train_test_split(textes, labels, test_size=0.25, random_state=42)

# Entraînement
vect = TfidfVectorizer()
X_train_vect = vect.fit_transform(X_train)
X_test_vect = vect.transform(X_test)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_vect, y_train)

# Prédiction et affichage
y_pred = clf.predict(X_test_vect)
print("\n📊 Rapport de performance du modèle :\n")
print(classification_report(y_test, y_pred))

# Sauvegarde du modèle
os.makedirs("modeles", exist_ok=True)
joblib.dump(clf, "modeles/modele_clf.pkl")
joblib.dump(vect, "modeles/vectorizer.pkl")
print("\n✅ Nouveau modèle sauvegardé dans 'modeles/'")
