import json
import logging
import paho.mqtt.client as mqtt

# Configuramos logging
logging.basicConfig(
    filename='/app/logs/consumidor.log',  # Archivo donde se guardan los logs
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")  # Decodifica el payload
    try:
        data = json.loads(msg)  # Intenta convertir a diccionario
        logging.info(f"Recibido: {data}")  # Guarda log en archivo
        print("Recibido:", data)           # También imprime en consola
    except json.JSONDecodeError:
        logging.warning(f"Mensaje inválido: {msg}")  # Mensaje inválido al log
        print("Mensaje inválido:", msg)

# Creamos el cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
client.on_message = on_message

# Conectamos al broker y nos suscribimos al topic
client.connect("mosquitto", 1883, 60)
client.subscribe("habitacion/ambiente")

# Loop infinito esperando mensajes
client.loop_forever()

