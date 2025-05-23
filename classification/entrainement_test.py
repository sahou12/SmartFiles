from classifieur_ai import entraîner_classifieur

exemples = [
    # Factures
    ("Facture EDF du 15 avril 2023", "Facture"),
    ("Facture Amazon - Commande 12345", "Facture"),
    ("Facture mensuelle Internet Orange", "Facture"),
    ("Reçu de paiement de la taxe foncière", "Facture"),

    # Devis
    ("Devis pour la rénovation de cuisine", "Devis"),
    ("Proposition de devis - société BTP", "Devis"),
    ("Estimation du projet peinture", "Devis"),
    ("Offre tarifaire pour travaux électriques", "Devis"),

    # Rapports
    ("Rapport trimestriel des ventes", "Rapport"),
    ("Rapport de stage - entreprise L'Oréal", "Rapport"),
    ("Analyse financière annuelle", "Rapport"),
    ("Compte-rendu de réunion du 23 mai", "Rapport"),

    # Notes de cours
    ("Résumé de biologie - chapitre 3", "Notes"),
    ("Fiche de révision histoire-géo", "Notes"),
    ("Cours de macroéconomie L1", "Notes"),
    ("Introduction aux probabilités", "Notes"),

    # Contrats
    ("Contrat de travail à durée déterminée", "Contrat"),
    ("Accord de location meublée", "Contrat"),
    ("Conditions générales de vente", "Contrat"),
    ("Contrat d’assurance habitation", "Contrat"),

    # CV
    ("Curriculum Vitae - Julie Dupont", "CV"),
    ("Mon CV 2024 - développeur web", "CV"),
    ("Expériences professionnelles et compétences", "CV"),
    ("Profil LinkedIn exporté", "CV"),

    # Lettres
    ("Lettre de motivation pour master RH", "Lettre"),
    ("Lettre de recommandation étudiant", "Lettre"),
    ("Lettre de démission", "Lettre"),
    ("Lettre administrative - demande de logement", "Lettre"),

    # Mails
    ("Objet : relance de facture impayée", "Mail"),
    ("Message de suivi de candidature", "Mail"),
    ("Email de confirmation de rendez-vous", "Mail"),
    ("Bonjour, voici le compte rendu de la réunion", "Mail"),
]

entraîner_classifieur(exemples)

print("✅ Entraînement enrichi terminé. Modèle mis à jour avec 8 catégories.")
