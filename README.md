# Ce README concerne le challenge : powerplant-coding-challenge

https://github.com/gem-spaas/powerplant-coding-challenge

powerplant-coding-challenge

Réalisé avec:
	- Python 3.7.2
	- Docker version 20.10.2, build 2291f61

# PARTIE DOCKER

## Pour créer l'image docker. Depuis l'intérieur du dossier (là où se trouve le Dockerfile), exécutez la commande suivante:

docker build -t flaskapp:latest .

## Pour lancer l'image docker. exécutez la commande suivante:

docker run -d -p 8888:8888 $ID_DOCKER_IMG

## Pour Lancer le test

python ./real_test01.py

# PARTIE NON DOCKER

## Pour installer les dépendances:

pip install -r requirements.txt

## pour lancer manuellement le serveur, depuis l'intérieur du dossier, exécutez la commande suivante:

flask run -h 0.0.0.0 -p 8888

Pour effectuer un test, à partir d'une nouvelle console, exécuter:
python real_test01.py

Cela effectue la commande POST avec un des payloads donné.

