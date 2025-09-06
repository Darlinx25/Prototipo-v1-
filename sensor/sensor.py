import time
import json
import random
import logging
import paho.mqtt.client as mqtt

# Configuramos logging
logging.basicConfig(
    filename='/app/logs/sensor.log',  # Archivo donde se guardan los logs
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Conectamos al broker usando el nombre del servicio en Compose
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
client.connect("mosquitto", 1883, 60)

while True:
    # Generamos valores aleatorios para temperatura y humedad
    msg = {
        "temp_celsius": random.randint(20, 30),
        "humedad": random.randint(50, 90)
    }
    payload = json.dumps(msg)
    
    # Publicamos el mensaje
    client.publish("habitacion/ambiente", payload)
    
    # Guardamos log en archivo y consola
    logging.info(f"Publicado: {payload}")
    print("Publicado:", payload)
    
    time.sleep(1)

