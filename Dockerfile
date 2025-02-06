# Utilise une image Python officielle comme image de base
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers du projet dans le conteneur
COPY . /app

# Copie les fichiers nécessaires au test
COPY Unit_test.py /app

# Expose un port si nécessaire (par exemple pour une API ou un serveur, ici pas nécessaire)
EXPOSE 5000

# Exécute les tests unitaires
CMD ["python", "-m", "unittest", "Unit_test.py"]
