import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, message): #Función que se ejecuta cada vez que llega un mensaje al topic subscripto
    msg = message.payload.decode("utf-8") #Decodifica el payload a string y lo convierte de JSON a diccionario
    try:
        data = json.loads(msg)
        print("Recibido:", data)
    except json.JSONDecodeError:
        print("Mensaje inválido:", msg) #Imprime el mensaje recibido o error si no es JSON.

client = mqtt.Client(client_id="", protocol=mqtt.MQTTv311) #Crea un cliente MQTT.
client.on_message = on_message #Asigna la función on_message para manejar mensajes.
client.connect("mosquitto", 1883, 60) #Conecta al broker llamado "mosquitto" en el puerto 1883.
client.subscribe("habitacion/ambiente") #Se suscribe al topic "habitacion/ambiente".
client.loop_forever() #loop_forever() → entra en un loop infinito, esperando mensajes y ejecutando on_message.
