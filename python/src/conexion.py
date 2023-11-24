from pymongo import MongoClient

class ConexionMongo:

	def __init__(self)->None:

		cliente=MongoClient("mongo", 27017)

		bbdd=cliente["bbdd_ordenes"]

		self.tabla=bbdd["ordenes"]
