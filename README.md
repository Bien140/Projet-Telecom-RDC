# Projet Telecom RDC
# Analyse SIG de la couverture télécom en RDC

##  Description
Ce projet analyse la couverture télécom en République Démocratique du Congo. Il croise les données d'antennes (OpenCellID), de population (WorldPop) et les limites administratives (GADM) pour identifier les provinces sous-couvertes et prioriser les investissements.

## 🛠️ Prérequis et Installation
Pour reproduire ce projet, installez les dépendances :
pip install pandas geopandas shapely matplotlib seaborn jupyter

## Comment exécuter le projet
1. Clonez ce dépôt.
2. Exécutez le script scripts/chargement des donnees.py. Cela générera le fichier projet_telecom.gpkg à la racine (non inclus dans ce dépôt car trop volumineux).
3. Ouvrez et exécutez le notebook scripts/exploration.ipynb pour l'analyse exploratoire.
4. Ouvrez et exécutez le notebook scripts/analyse_spatiale.ipynb pour les jointures spatiales et la génération des graphiques.
5. La carte finale est disponible dans le dossier outputs/.

## Résultats clés
- Kinshasa concentre l'essentiel des antennes (11 139 antennes pour 9,1M d'habitants).
- Le Sud-Kivu et la Tshopo sont des "déserts télécoms" (moins de 5 antennes pour plus de 4M d'habitants).
- Recommandation : Déployer en urgence des antennes dans les provinces du centre et de l'Est.

## Contenu du dépôt
- data/ : Données brutes (Antennes, Limites administratives).
- scripts/ : Script Python et Notebooks d'analyse.
- outputs/ : Carte finale au format PNG.

## Auteur
DAYA NZUAMBE Kenaya - Octobre 2026
