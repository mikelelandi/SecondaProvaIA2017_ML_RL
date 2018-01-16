#!/usr/bin/env python
"""
	File name:				graph_test.py
	Author:					Michele Landi / Raoul Landi
	Modified by:			Michele landi / Raoul Landi
	Matr Raoul Landi:		0258005
	Matr Michele Landi:     0243311
	Date created:			09/01/2018
	Date last modified:		13/01/2018
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


		# si stabilisce il numero dei vertici totali N del grafo, compreso tra 5 e 50
		Ntot = random.randrange(5 , 51)


		# si aggiungono i vertici al grafo con ID incremntale
		# tempo di esecuzione Teorico O(N)
		nodes = []
		for i in range(0 , Ntot):
			node = oGraph.addNode(i)
			nodes.append(node)
		# creazione di una lista IdNodesA composta dai ID dei nodi del grafo scelti casualmente
		Sample = random.randrange(1 , len(nodes))
		IdNodesA = random.sample(range(0 , Ntot) , Sample)
		# creazione di una lista IdNodesB composta dai ID dei nodi del grafo scelti casualmente
		Sample = random.randrange(1 , len(nodes))
		IdNodesB = random.sample(range(0 , Ntot) , Sample)


		# creazione degli archi che congiungono in maniera randomica nodi della lista IdNodesA con i nodi della lista IdNodesB
		# tempo di esecuzione teorico O(N^2)
		for IdA in IdNodesA:
			node_src = oGraph.getNode(IdA)
			for IdB in IdNodesB:
				node_dst = oGraph.getNode(IdB)
				if random.randrange(0 , 2) == 1 and node_src != node_dst and oGraph.isAdj(node_src.id , node_dst.id) == False and oGraph.isAdj(
						node_dst.id , node_src.id) == False:
					oGraph.insertEdge(node_src.id , node_dst.id , 1)
					oGraph.insertEdge(node_dst.id , node_src.id , 1)


        # simulazione dell'operazione di cancellazione in maniera randomica di un quinto dei nodi e gli eventuali archi ad essi associati
		# tempo di esecuzione teorico O(1)
		listNodes=[]
		for i in range(0, Ntot):
		 listNodes.append(i)
		percNode=len(listNodes)//5
		count=0
		while count<percNode:
		 count=count+1
		 iDeleteNode = random.randrange(0,len(listNodes))
		 listAdj=oGraph.getAdj(listNodes[iDeleteNode])
		 for i in range (0,len(listAdj)):
		   oGraph.deleteEdge(listNodes[iDeleteNode],listAdj[i])
		 oGraph.deleteNode(listNodes[iDeleteNode])
		 listNodes.pop(iDeleteNode)

		return oGraph


if __name__ == "__main__":

	print ("----------  generateGraph  ----------------------")
	print("--- stampa del grafo ---")
	Gph = Graph_Test.generateGraph()
	Gph.print()
