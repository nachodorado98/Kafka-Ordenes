from confluent_kafka.admin import AdminClient, NewTopic

def crearTopic(topic:str)->None:

	admin=AdminClient({"bootstrap.servers":"kafka1:19092"})

	if topic in admin.list_topics().topics:

		print(f"Topic {topic} creado")
		return

	print(f"Creando topic {topic}...")

	objeto_topic=NewTopic(topic=topic, num_partitions=3, replication_factor=1)

	admin.create_topics([objeto_topic])

	crearTopic(topic)
