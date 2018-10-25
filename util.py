import os
import time

def stopwords_files_to_list():
	lista = []
	for arquivo in os.listdir('stop-words'):
		with open('stop-words/{}'.format(arquivo), "r", encoding="ISO-8859-1") as file:
			lista.append((file.read().splitlines()))
	return lista

