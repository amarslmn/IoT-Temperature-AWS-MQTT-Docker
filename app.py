import paho.mqtt.client as mqtt
import json
import time
import random
from dotenv import load_dotenv
import logging
import os




class ConnectAws:

    def __init__(self, AWS_HOST, AWS_PORT):
        self.AWS_HOST = AWS_HOST
        self.AWS_PORT = AWS_PORT
        
        self.client  = mqtt.Client()
        self.client.tls_set(
                            ca_certs="./AWScertificats/AmazonRootCA1.pem", 
                            certfile="./AWScertificats/certificate.pem.crt", 
                            keyfile="./AWScertificats/private.pem.key"
                            )
        try:
            self.client.connect(self.AWS_HOST, self.AWS_PORT)
            logging.info("Connexion établie au broker AWS IoT Core")
        except Exception as e:
            logging.error("Erreur lors de la connexion au broker AWS IoT Core : %s", e)

    def on_pulish(self):

        try:
            data = self.data_generate()
            logging.info("Donnée de température récupérée depuis la méthode data_generate")

        except Exception as e:
            logging.error("Erreur lors de la génération des données de température : %s", e)
        try:

            self.client.publish("topic/temperature", json.dumps(data))
            logging.info("Donnée de température publiée avec succès sur le topic")


        except Exception as e:
            logging.error("Erreur lors de la publication des données de température dans le topic : %s", e)
        
        




    
    def data_generate(self):
        
        val = random.randint(10,75)
        payload = {"timestamp": str(int(time.time())), "temperature": val}
        logging.info("Donnée de température générée avec la fonction random")
        return payload


    def run(self):
        self.client.loop_start()
        nombre_donnée = 0
        while True: 
            self.on_pulish()
            
            nombre_donnée += 1
            logging.info(f""" Nombre de données de température envoyéescls : {nombre_donnée}

                                    """)
            time.sleep(10)
            

# Configuration de la journalisation
logging.basicConfig(level=logging.DEBUG,  #
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# charger les variables d'environement
load_dotenv()


AWS_HOST = os.getenv("AWS_HOST")
AWS_PORT = 8883




datasend = ConnectAws(AWS_HOST=AWS_HOST, AWS_PORT=AWS_PORT)

datasend.run()

