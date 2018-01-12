#!/usr/bin/env python
"""
	File name:				graph_test.py
	Author:					Michele Landi / Raoul Landi
	Modified by:			Michele landi / Raoul Landi
	Matr Raoul Landi:		0258005
	Matr Michele Landi:
	Date created:			09/01/2018
	Date last modified:		09/01/2018
	Python Version:			3.6
	File Versione:			1.0.0


	Traccia 2 - Nodo medio
	Sia dato un grafo non orientato aciclico e non pesato ​G​.
	Data una coppia di nodi ​(n1,n2)​ in ​G​, la distanza ​dist(n1,n2)​ é il minor numero di archi necessari a connettere ​n1. 
	Un nodo ​m ​é ​medio​ di ​n1 ​ed ​n2 ​se e solo se é ​equidistante​ da ​n1 ​e ​n2​, ovvero se ​dist(n1,m) ​=  dist(m,n2)​. 
	 
	Progettare e implementare un algoritmo che, dato un grafo non orientato aciclico e non 
	pesato ​G​, determini il nodo ​m*​ che risulta essere ​medio per il maggior numero di coppie di 
	nodi​.
"""

import random
from graph.Graph_AdjacencyList import GraphAdjacencyList

class Graph_Test():

	def generateGraph():
		"""
		:return: un oggetto di tipo  GraphAdjacencyList con le seguenti caratteristiche:
				 Il numero di nodi è scelto casualmente da un range di 5-50, le conessioni tra i vertici
				 sono scelti casualmente.
		"""

		# instanziamo oGraph come oggetto di tipo GraphAdjacencyList
		oGraph = GraphAdjacencyList()

		# si stabilisce il numero dei vertici
		Ntot = random.randrange(5 , 51)

		# aggiungiamo i vertici al grafo tempo stimato O(Ntot)
		nodes = []
		for i in range(0 , Ntot):
			node = oGraph.addNode(i)
			nodes.append(node)

		# creiamo una lista A di ID casuali dei nodi del grafo
		Sample = random.randrange(1 , len(nodes))
		IdNodesA = random.sample(range(0 , Ntot) , Sample)

		# creiamo una lista B di ID casuali dei nodi del grafo
		Sample = random.randrange(1 , len(nodes))
		IdNodesB = random.sample(range(0 , Ntot) , Sample)

		# creazione degli archi
		for IdA in IdNodesA:
			node_src = oGraph.getNode(IdA)
			for IdB in IdNodesB:
				node_dst = oGraph.getNode(IdB)
				if random.randrange(0 , 2) == 1 and node_src != node_dst and oGraph.isAdj(node_src.id , node_dst.id) == False and oGraph.isAdj(
						node_dst.id , node_src.id) == False:
					oGraph.insertEdge(node_src.id , node_dst.id , 1)
					oGraph.insertEdge(node_dst.id , node_src.id , 1)

		return oGraph

	def getGraphFix():
			"""
			:return: un grafo non orientato con una struttura predifinita con la seguente lista di adiacenza:

					0:[1, 3, 6, 5, 4]
					1:[6, 0]
					2:[]
					3:[6, 0]
					4:[6, 0]
					5:[6, 0]
					6:[1, 3, 0, 5, 4]
					7:[]

					Il risultato corrisponde a un grafo non orientato con 8 vertici dei quali 2 non sono collegati e con 18 archi
			"""

			# instanziamo oGraph come oggetto di tipo GraphAdjacencyList
			oGraph = GraphAdjacencyList()


			#creazione degli nodi da 0 a 7
			nodes = []
			for i in range(0 , 8):
				node = oGraph.addNode(i)
				nodes.append(node)

			# creazione degli arci che partono dal nal nodo 0
			oGraph.insertEdge(0 ,1, 1)
			oGraph.insertEdge(0 ,3, 1)
			oGraph.insertEdge(0 ,6, 1)
			oGraph.insertEdge(0 ,5, 1)
			oGraph.insertEdge(0 ,4, 1)

			# creazione degli arci che partono dal nal nodo 1
			oGraph.insertEdge(1 ,6 , 1)
			oGraph.insertEdge(1 ,0 , 1)

			# creazione degli arci che partono dal nal nodo 2
			# vuoto

			# creazione degli arci che partono dal nal nodo 3
			oGraph.insertEdge(3 ,6 , 1)
			oGraph.insertEdge(3 ,0 , 1)

			# creazione degli arci che partono dal nal nodo 4
			oGraph.insertEdge(4 ,6 , 1)
			oGraph.insertEdge(4 ,0 , 1)

			# creazione degli arci che partono dal nal nodo 5
			oGraph.insertEdge(5 ,6 , 1)
			oGraph.insertEdge(5 ,0 , 1)

			# creazione degli arci che partono dal nal nodo 6
			oGraph.insertEdge(6 ,1 , 1)
			oGraph.insertEdge(6 ,3 , 1)
			oGraph.insertEdge(6 ,0 , 1)
			oGraph.insertEdge(6 ,5 , 1)
			oGraph.insertEdge(6 ,4 , 1)

			# creazione degli arci che partono dal nal nodo 7
			# vuoto

			return oGraph

	def getGraphFix2():
			"""
			:return: un grafo non orientato con una struttura predifinita con la seguente lista di adiacenza:

					0:[1, 4]
					1:[0, 2]
					2:[1]
					3:[4]
					4:[0, 3, 5]
					5:[4, 6]
					6:[5]
					7:[]

					Il risultato corrisponde a un grafo non orientato con 7 vertici dei quali 2 non sono collegati e con 18 archi
			"""
			# instanziamo oGraph come oggetto di tipo GraphAdjacencyList
			oGraph = GraphAdjacencyList()


			#creazione degli nodi da 0 a 7
			nodes = []
			for i in range(0 , 8):
				node = oGraph.addNode(i)
				nodes.append(node)

			# creazione degli arci che partono dal nal nodo 0
			oGraph.insertEdge(0 ,1, 1)
			oGraph.insertEdge(0 ,4, 1)

			# creazione degli arci che partono dal nal nodo 1
			oGraph.insertEdge(1 ,0 , 1)
			oGraph.insertEdge(1 ,2 , 1)

			# creazione degli arci che partono dal nal nodo 2
			oGraph.insertEdge(2 ,1 , 1)

			# creazione degli arci che partono dal nal nodo 3
			oGraph.insertEdge(3 ,4 , 1)

			# creazione degli arci che partono dal nal nodo 4
			oGraph.insertEdge(4 ,0 , 1)
			oGraph.insertEdge(4 ,3 , 1)
			oGraph.insertEdge(4, 5 , 1)

			# creazione degli arci che partono dal nal nodo 5
			oGraph.insertEdge(5 ,4 , 1)
			oGraph.insertEdge(5 ,6 , 1)

			# creazione degli arci che partono dal nal nodo 6
			oGraph.insertEdge(6 ,5 , 1)

			# creazione degli arci che partono dal nal nodo 7
			# vuoto

			return oGraph

	def getGraphFix3():
			"""
			:return: un grafo non orientato con una struttura predifinita con la seguente lista di adiacenza:

					0:[1, 3]
					1:[0, 2]
					2:[1]
					3:[0, 4, 5]
					4:[3]
					5:[3, 6]
					6:[5]
					7:[]

					Il risultato corrisponde a un grafo non orientato con 7 vertici dei quali 2 non sono collegati e con 18 archi
			"""

			oGraph = GraphAdjacencyList()


			#creazione degli nodi da 0 a 7

			nodes = []
			for i in range(0 , 8):
				node = oGraph.addNode(i)
				nodes.append(node)

			# creazione degli arci che partono dal nal nodo 0
			oGraph.insertEdge(0 ,1, 1)
			oGraph.insertEdge(0 ,3, 1)

			# creazione degli arci che partono dal nal nodo 1
			oGraph.insertEdge(1 ,0 , 1)
			oGraph.insertEdge(1 ,2 , 1)

			# creazione degli arci che partono dal nal nodo 2
			oGraph.insertEdge(2 ,1 , 1)

			# creazione degli arci che partono dal nal nodo 3
			oGraph.insertEdge(4 ,3 , 1)

			# creazione degli arci che partono dal nal nodo 4
			oGraph.insertEdge(3 ,0 , 1)
			oGraph.insertEdge(3 ,4 , 1)
			oGraph.insertEdge(3, 5, 1)

			# creazione degli arci che partono dal nal nodo 5
			oGraph.insertEdge(5 ,3 , 1)
			oGraph.insertEdge(5 ,6 , 1)

			# creazione degli arci che partono dal nal nodo 6
			oGraph.insertEdge(6 ,5 , 1)

			# creazione degli arci che partono dal nal nodo 7
			# vuoto

			return oGraph

if __name__ == "__main__":

	print ("----------  generateGraph  ----------------------")
	print("--- stampa del grafo ---")
	Gph = Graph_Test.generateGraph()
	Gph.print()

	print ("----------  getGraphFix  ----------------------")
	print("--- stampa del grafo ---")
	Gph = Graph_Test.getGraphFix()
	Gph.print()

	print ("----------  getGraphFix2  ----------------------")
	print("--- stampa del grafo ---")
	Gph = Graph_Test.getGraphFix2()
	Gph.print()

	print ("----------  getGraphFix3  ----------------------")
	print("--- stampa del grafo ---")
	Gph = Graph_Test.getGraphFix3()
	Gph.print()
