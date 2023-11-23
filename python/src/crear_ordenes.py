import csv
from typing import List, Dict
import uuid

def leerArchivoOrdenes()->List[int]:

	with open("ordenes.csv", "r") as f:

		valores=list(csv.reader(f))

	return valores

def obtenerOrdenes()->Dict:

	ordenes=leerArchivoOrdenes()

	return [{"id_orden":uuid.uuid4().hex, "id_cliente":int(orden[1]), "cantidad":float(orden[2])} for orden in ordenes]