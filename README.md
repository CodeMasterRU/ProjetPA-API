# ProjetPA-API

## Architecture du projet


ProjetPA-API/
├─ apimongo/
│  ├─ server/
│  │  ├─ models/
│  │  │  ├─ article.py
│  │  ├─ routes/
│  │  │  ├─ article.py
│  │  ├─ app.py
│  │  ├─ database.py
│  ├─ main.py
├─ insert_mongo.py
├─ README.md
├─ requirements.txt
├─ scrap_carrefour.py
├─ streamlit_mongo.py









## Pré-requis

Le projet contient le scrapping des données du site Carrefour et l'insertion dans MongoDB, l'officiant en streamlit et la gestion de API

## Installation de bibliothèques

pip install -r requirements.txt

## Scrapping 

py ./scrap_carrefour.py

## MongoDB

### Start server et terminal de mongo, l'exécution d'insert de données récupérés

start mongod | mongosh

py ./insert_mongo.py

## Streamlit 

py ./streamlit_mongo.py

## API CRUD

py ./apimongo/main.py


