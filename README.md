
# Projet Scraping : Jujutsu Kaisen

Ce projet a pour objectif de récupérer les informations des personnages du manga Jujutsu Kaisen disponibles sur le site Wiki.
Ce projet a été réalisé par Karen Azoulay.

## Installation

- Clonez le projet
- Installez Requests
```pip install requests```
- Installez Requests Cache
```pip install requests-cache```
- Installez bs4 pour l'utilisation de BeautifulSoup
```pip install bs4```
- Installez pandas
```pip install pandas```
- Installez xlswriter, xlrd et openpyxl pour pouvoir générer l'excel :
```
pip install xlsxwriter
pip install xlrd
pip install openpyxl
```
- Allez dans le dossier et lancez dans votre terminal de commande :
```python jujutsuKaisen.py```

## Explication de la démarche de développement
### Les étapes de développement

L'objectif étant de récupérer les informations des personnages du manga Jujutsu Kaisen, j'ai décomposé ce projet en différentes étapes. 
1. Définir la page listant tous les personnages du manga
2. Récupérer sur cette page un nombre défini par l'internaute de nom de personnage
3. Définir les pages listant les informations pour chaque personnage en utilisant leurs noms récupérés précédemment
4. Lister toutes les informations disponibles sur ses personnages
5. Affichez ses informations dans le terminal
6. Générez un document excel récapitulant toutes les informations des personnages sélectionnés
Pour réaliser ces différentes étapes, j'ai développer diverses fonctions.

### Les fonctions

Le projet est séparer en 4 fonctions différentes :
- ```get_character_jujutsu_list_page``` qui définit quel est la page listant les personnages du manga Jujutsu Kaisen
- ```get_character``` qui récupère les noms des personnages disponible sur la page
- ```get_jujutsu_page``` qui trouve la page comportant les informations détaillés de chaque personnage
- ```get_cara_character``` qui récupère les informations des personnages
Vous trouverez toutes les étapes de ses fonctions dans le code en commentaire.
