from confluent_kafka import Consumer, KafkaError
import json

from crear_topic import crearTopic
from config import TOPIC
from conexion import ConexionMongo

con=ConexionMongo()

crearTopic(TOPIC)

consumer=Consumer({"bootstrap.servers": "kafka1:19092", "group.id":"grupo1"})

consumer.subscribe([TOPIC])

print("Escuchando...")

while True:

	mensaje=consumer.poll(timeout=100)

	if mensaje is None:

		continue

	if mensaje.error():

		if mensaje.error().code()==KafkaError._PARTITION_EOF:

			continue

		else:

			print(mensaje.error())

			break

	print(mensaje.value().decode("utf-8"))

	con.tabla.insert_one(json.loads(mensaje.value().decode("utf-8")))
