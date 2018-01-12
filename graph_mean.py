#!/usr/bin/env python
"""
	File name:				graph_mean.py
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
	 
	Progettare e implementare un algoritmo che, dato un grafo non orientato e non 
	pesato ​G​, determini il nodo ​m*​ che risulta essere ​medio per il maggior numero di coppie di nodi​.
"""

import random
from graph.shortestPaths import FloydWarshall_ADJ
from graph_test import Graph_Test

def Nodes_Mean(graph):
    """
    :param graph: deve essere uun oggetto di tipo grafo con Lista di adiacenza
    :return: matrice di dimensioni NxN con i nodi equidistanti per ogni percorso
    """
    # inizializiamo ma latrice M di dimensioni NxN con il valore None
    M = [[None for x in range(graph.numNodes())] for y in range(graph.numNodes())]

    # otteniamo la matrice con tutti i percorsi minimi del grafo
    distances = FloydWarshall_ADJ(graph)

    # cerchiamo i percorsi minimi dove possono avere un modo medio tale dist(n1,m) ​=  dist(m,n2)
    for i in range(0, graph.numNodes()):
        for j in range(i, graph.numNodes()):
            if i != j and distances[i][j] != float('inf') and distances[i][j] % 2 == 0:
                for m in graph.dfs(i):
                    if distances[i][m] == distances[m][j] and \
                       distances[i][m] != float('inf') and \
                       distances[m][j] != float('inf') and \
                       distances[i][m] != 0 and \
                       distances[m][j] != 0:

                        M[i][j] = m
                        break

    # return la matrice di M
    return M


def getNodeMedium(graph,n1,n2):
    """
    :param graph: deve essere uun oggetto di tipo grafo con Lista di adiacenza
    :param n1: Id del nodo di partenza del percorso del grafo [graph]
    :param n2: Id del nodo di destinazione del percorso del grafo [graph]
    :return: se esiste un nodo medio del percorso tra n1 e n2 ristituisce il suo Id  altrimenti None
    """

    Matrx = Nodes_Mean(graph)
    NodeM = Matrx[n1][n2]

    return NodeM

if __name__ == "__main__":

    #graph = Graph_Test.generateGraph()
    graph = Graph_Test.getGraphFix2()

    D = FloydWarshall_ADJ(graph)

    M = Nodes_Mean(graph)

    print ("---- print del grafo ----")
    graph.print()

    print ("---- Matrice dei minimi percorsi ----")
    for elm in D:
        print (elm)

    print ("---- Matrice dei Medi dei minimi percorsi ----")
    for elm in M:
        print (elm)

    n1,n2 = random.sample(range(0 , graph.numNodes()) , 2)
    print ("---- Nodo medio tra {} e {} ----".format(n1,n2))
    N = getNodeMedium(graph,n1,n2)
    print (N)