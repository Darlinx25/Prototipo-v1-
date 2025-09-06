import time
import json
import random
import paho.mqtt.client as mqtt

# Conectamos al broker usando el nombre del servicio en Compose
client = mqtt.Client()
client.connect("mosquitto", 1883, 60)

while True:
    # Generamos valores aleatorios para temperatura y humedad
    msg = {
        "temp_celsius": random.randint(20, 30),
        "humedad": random.randint(50, 90)
    }
    payload = json.dumps(msg)
    client.publish("habitacion/ambiente", payload)
    print("Publicado:", payload)
    time.sleep(1)
