# Projet AWS IoT Core avec MQTT

Ce projet vise à démontrer comment connecter un dispositif à AWS IoT Core en utilisant MQTT (Message Queuing Telemetry Transport). Le projet simule l'envoi de données de température à un topic MQTT sur AWS IoT Core à l'aide de la bibliothèque Paho MQTT en Python.

## Fonctionnement du Projet

Le projet consiste en un script Python qui simule un dispositif de surveillance de la température. Le script établit une connexion sécurisée avec AWS IoT Core, publie périodiquement des données de température simulées sur un topic MQTT et affiche un message de succès à chaque publication.

## Prérequis

- Clés et certificats AWS IoT Core générés et accessibles
- Installez les dépendances à partir du fichier requirements.txt en exécutant la commande : `pip install -r requirements.txt`

## Étapes pour la Configuration AWS IoT Core

1. **Créer un objet (Thing) :** Créez un objet (Thing) dans AWS IoT Core pour représenter votre dispositif. Notez l'identifiant unique du Thing ("Thing Name").

2. **Créer une politique (Policy) :** Créez une politique définissant les autorisations nécessaires pour le Thing. Spécifiez les actions autorisées (publication, souscription, etc.) et les ressources associées.

3. **Créer un certificat et attacher la politique :** Générez un certificat pour le Thing. Attachez la politique créée précédemment au certificat pour définir ses autorisations.

4. **Sélectionner l'endpoint du topic MQTT :** Trouvez l'endpoint MQTT associé à votre région AWS pour établir une connexion MQTT sécurisée.

## Configuration

1. Remplacez les chemins des fichiers de certificats dans le script (`certificate.pem.crt`, `private.pem.key`, `AmazonRootCA1.pem`) par les chemins corrects sur votre machine.
2. Modifiez les informations de connexion AWS IoT Core (AWS_HOST, AWS_PORT) en fonction de votre région et de votre configuration.

## Exécution sans Docker

1. Ouvrez une invite de commande dans le répertoire du projet.
2. Exécutez le script Python : `python app.py`.

Le script commencera à publier des données simulées de température sur le topic MQTT "topic/temperature" toutes les 5 secondes. Utilisez Ctrl+C pour interrompre l'exécution.

## Exécution avec Docker

1. Assurez-vous que les certificats AWS sont dans le même répertoire que le Dockerfile.
2. Ouvrez une invite de commande dans le répertoire du projet.
3. Construisez l'image Docker : `docker build -t nom_de_ton_image .`
4. Exécutez le conteneur : `docker run --name mon_conteneur -v $PWD/AWScertificats:/app/AWScertificats -d nom_de_ton_image`.
5. Affichez les logs du conteneur : `docker logs mon_conteneur`.

Le conteneur exécutera le script pour publier des données de température simulées sur le topic MQTT. Utilisez `docker stop mon_conteneur` pour arrêter le conteneur.
