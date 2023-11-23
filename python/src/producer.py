from confluent_kafka import Producer
import json
import time

from config import TOPIC
from crear_topic import crearTopic
from crear_ordenes import obtenerOrdenes

crearTopic(TOPIC)

producer=Producer({"bootstrap.servers": "kafka1:19092"})

ordenes=obtenerOrdenes()

for orden in ordenes:

	print(f"Orden {orden['id_orden']}")

	producer.produce(TOPIC, value=json.dumps(orden))

	time.sleep(0.01)

producer.flush()
