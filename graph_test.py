#!/usr/bin/env python
"""
    File name:			graph_test.py
    Author:				Michele Landi / Raoul Landi
    Modified by:		Michele landi / Raoul Landi
    Matr Raoul Landi:	0258005
    Matr Michele Landi:
    Date created:		09/01/2018
    Date last modified:	09/01/2018
    Python Version:		3.6
    File Versione:		1.0.0


	Traccia 2 - Nodo medio
	Sia dato un grafo non orientato aciclico e non pesato ​G​.
	Data una coppia di nodi ​(n1,n2)​ in ​G​, la distanza ​dist(n1,n2)​ é il minor numero di archi necessari a connettere ​n1. 
	Un nodo ​m ​é ​medio​ di ​n1 ​ed ​n2 ​se e solo se é ​equidistante​ da ​n1 ​e ​n2​, ovvero se ​dist(n1,m) ​= 
	dist(m,n2)​. 
	 
	Progettare e implementare un algoritmo che, dato un grafo non orientato aciclico e non 
	pesato ​G​, determini il nodo ​m*​ che risulta essere ​medio per il maggior numero di coppie di 
	nodi​.
"""

import random
import time

from graph.Graph_AdjacencyList import GraphAdjacencyList
#import numpy as np
#from dictTrees.dictionaryAVL import DictAVL
#from dictTrees.dictBinaryTree import DictBinaryTree
#import matplotlib.pyplot as plt



class Graph_Test():

	def generateGraph(self):

		oGraph = GraphAdjacencyList()

		Ntot = random.randrange(10, 100)

		nodes = []
		for N in range( 0 , Ntot ):
			nodes.apped(N)
			oGraph.addNode(N)
