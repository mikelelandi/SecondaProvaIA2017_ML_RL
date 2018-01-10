#!/usr/bin/env python
"""
    File name:			graph_test.py
    Author:			Michele Landi / Raoul Landi
    Modified by:		Michele landi / Raoul Landi
    Matr Raoul Landi:		0258005
    Matr Michele Landi:		
    Date created:		09/01/2018
    Date last modified:		09/01/2018
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


# import numpy as np
# from dictTrees.dictionaryAVL import DictAVL
# from dictTrees.dictBinaryTree import DictBinaryTree
# import matplotlib.pyplot as plt


class Graph_Test():

    def generateGraph():
        oGraph = GraphAdjacencyList()

        Ntot = random.randrange(5, 10)

        nodes = []
        for i in range(0, Ntot):
            node = oGraph.addNode(i)
            nodes.append(node)

        Sample = random.randrange(1, len(nodes))
        IdNodesA = random.sample(range(0, Ntot), Sample)

        Sample = random.randrange(1, len(nodes))
        IdNodesB = random.sample(range(0, Ntot), Sample)

        for IdA in IdNodesA:
            node_src = oGraph.getNode(IdA)
            for IdB in IdNodesB:
                node_dst = oGraph.getNode(IdB)
                if node_src != node_dst and oGraph.isAdj(node_src.id, node_dst.id) == False and oGraph.isAdj(node_dst.id, node_src.id) == False:
                    oGraph.insertEdge(node_src.id, node_dst.id,1)
                    oGraph.insertEdge(node_dst.id, node_src.id,1)

        return oGraph


if __name__ == "__main__":

    Gph = Graph_Test.generateGraph()

    print ("--- stampa del grafo ---")
    Gph.print()
