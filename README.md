# Prototipo MQTT - Sensor Simulado

## Descripción

Prototipo de sistema MQTT que simula un sensor de temperatura y humedad.  
Incluye:

- **Broker MQTT (`mosquitto`)**: centraliza la comunicación.  
- **Sensor simulado**: publica cada segundo un mensaje JSON con temperatura y humedad.  
- **Consumidor**: se suscribe al topic y muestra los mensajes recibidos en consola.

---

## Formato de mensajes

```json
{
  "temp_celsius": 27,
  "humedad": 65
}
```
## Estructura de carpetas
```
Prototipo-v1/
├─ docker-compose.yml
├─ mosquitto/
│  ├─ config/
│  ├─ data/
│  └─ log/
├─ sensor/
│  ├─ Dockerfile.sensor
│  └─ sensor.py
├─ consumidor/
│  ├─ Dockerfile.consumidor
│  └─ consumidor.py
├─ publicar.sh
└─ consumir.sh
```
## Uso

- docker compose up -d                # Levantar contenedores
- docker compose logs -f consumidor   # Mensajes recibidos
- docker compose logs -f sensor       # Mensajes publicados
- docker compose logs -f mosquitto    # Actividad del broker

## Implementación

- Lenguaje: Python 3.11
- Librería MQTT: paho-mqtt
- Contenedores Docker:
- Broker: eclipse-mosquitto:latest
- Sensor: Python + sensor.py
- Consumidor: Python + consumidor.py
- Docker Compose orquesta los tres contenedores en la misma red.
