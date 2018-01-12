#!/usr/bin/env python
"""
    File name:			    graph_measure.py
    Author:			        Michele Landi / Raoul Landi
    Modified by:		    Michele landi / Raoul Landi
    Matr Raoul Landi:		0258005
    Matr Michele Landi:
    Date created:		    09/01/2018
    Date last modified:		09/01/2018
    Python Version:		    3.6
    File Versione:		    1.0.0


    Traccia 2 - Nodo medio
    Sia dato un grafo non orientato e non pesato ​G​.
    Data una coppia di nodi ​(n1,n2)​ in ​G​, la distanza ​dist(n1,n2)​ é il minor numero di archi necessari a connettere ​n1. 
    Un nodo ​m ​é ​medio​ di ​n1 ​ed ​n2 ​se e solo se é ​equidistante​ da ​n1 ​e ​n2​, ovvero se ​dist(n1,m) ​= dist(m,n2)​. 
     
    Progettare e implementare un algoritmo che, dato un grafo non orientato e non 
    pesato ​G​, determini il nodo ​m*​ che risulta essere ​medio per il maggior numero di coppie di nodi​.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from graph.Graph_AdjacencyList import GraphAdjacencyList
from graph.shortestPaths import FloydWarshall_ADJ
from graph_test import Graph_Test
from graph_mean import getNodeMedium, Nodes_Mean




def generateAddNoneMeasure(Sample, Node):
    """
    :param Sample: il numero di campioni o di ripetizioni per la creazione del grafo
    :param Node: il numero massimo di nodi per creare lo span del grafo per l'asse X
    :return: plot tra valore misurato e calcolato
    """

    # creazione dei campioni
    dictTime = {}
    for j in range(1, Sample):
        Graph = GraphAdjacencyList()
        for N in range(0, Node):
            inizio = time.clock()
            Graph.addNode(N)
            fine = time.clock() - inizio
            if N not in dictTime.keys():
                dictTime[N] = []
            dictTime[N].append(fine)

    X = []
    Y = []

    for key in sorted(dictTime.keys()):
        X.append(key)
        M = np.mean(np.array(dictTime[key]))
        Y.append(M)

    X = np.array(X)
    Y = np.array(Y)
    Yt = np.ones(len(Y))
    Yt = Yt * np.mean(Y)

    plt.figure('Tempo aggiungi vertice')
    plt.grid(True)
    plt.title('Tempo aggiungi vertice')
    plt.ylabel('tempo in s')
    plt.xlabel('numero di vertici')
    plt.xlim([np.min(X), np.max(X)])
    plt.ylim([0, np.max(Y) * 1.2])
    plt.plot(X, Y, 'r-', label='Tempo misurato con {0} campioni'.format(Sample))
    plt.plot(X, Yt, 'b-', label='Tempo medio')
    plt.legend(loc='upper left')
    plot = plt
    return plot

def generateInsertEdgeMeasure(Sample, Node):
    # creazione dei campioni
    dictTime = {}
    for j in range(1, Sample):
        Graph = GraphAdjacencyList()

        nodes = []
        for i in range(Node):
            node = Graph.addNode(i)
            nodes.append(node)

        for node_src in nodes:
            for node_dst in nodes:
                if node_src != node_dst:
                    M = Graph.numEdges()

                    if M not in dictTime.keys():
                        dictTime[M] = []

                    inizio = time.clock()
                    Graph.insertEdge(node_src.id, node_dst.id, 1)
                    fine = time.clock() - inizio

                    dictTime[M].append(fine)

    X = []
    Y = []

    for key in sorted(dictTime.keys()):
        X.append(key)
        M = np.mean(np.array(dictTime[key]))
        Y.append(M)

    X = np.array(X)
    Y = np.array(Y)
    Yt = np.ones(len(Y))
    Yt = Yt * np.mean(Y)

    plt.figure('Tempo aggiungi arco')
    plt.grid(True)
    plt.title('Tempo aggiungi arco')
    plt.ylabel('tempo in s')
    plt.xlabel('numero di archi')
    plt.xlim([np.min(X), np.max(X)])
    plt.ylim([0, np.max(Y) * 1.2])
    plt.plot(X, Y, 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot(X, Yt, 'b-', label='T(n)=cost')
    plt.legend(loc='upper left')
    plot = plt
    return plot

def generateDegMeasure(Sample, Node):
    # creazione dei campioni
    dictTime = {}
    for j in range(1, Sample):
        graph = GraphAdjacencyList()

        nodes = []
        for i in range(Node):
            node = graph.addNode(i)
            nodes.append(node)

        for node_src in nodes:
            for node_dst in nodes:
                if node_src != node_dst:

                    graph.insertEdge(node_src.id, node_dst.id, 1)

                    inizio = time.clock()
                    D = graph.deg(node_src.id)
                    fine = time.clock() - inizio

                    if D > 0:
                        if D not in dictTime.keys():
                            dictTime[D] = []
                        dictTime[D].append(fine)

    X = []
    Y = []

    for key in sorted(dictTime.keys()):
        X.append(key)
        M = np.mean(np.array(dictTime[key]))
        Y.append(M)

    X = np.array(X)
    Y = np.array(Y)
    Yt = X
    R = Yt / Y
    C = np.max(R)

    plt.figure('Tempo calcolo del grado')
    plt.grid(True)
    plt.title('Tempo calcolo del grado')
    plt.ylabel('andamento temporale')
    plt.xlabel('numero di grado del nodo X')
    plt.xlim([np.min(X), np.max(X)])
    plt.ylim([0, np.max(Yt) * 1.2])
    plt.plot(X, C*Y, 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot(X, Yt, 'b-', label='T(n)=sigma(X)')
    plt.legend(loc='upper left')
    plot = plt
    return plot

def generateGraphTestMeasure(Sample):
    #calcolo dei campioni
    dictTime = {}
    for j in range(1, Sample):
        inizio = time.clock()
        graph = Graph_Test.generateGraph()
        fine = time.clock() - inizio

        n = graph.numNodes()

        if n not in dictTime.keys():
            dictTime[n] = []

        dictTime[n].append(fine)

    X = []
    Y = []

    for key in sorted(dictTime.keys()):
        X.append(key)
        M = np.mean(np.array(dictTime[key]))
        Y.append(M)

    X = np.array(X)
    Y = np.array(Y)
    Yt = np.power(X, 3)
    #R = Yt / Y
    C = np.max(Yt) / np.max(Y)

    plt.figure('Tempo generazione del grafo G non pesato e non orientato')
    plt.grid(True)
    plt.title('Tempo generazione del grafo G')
    plt.ylabel('andamento temporale')
    plt.xlabel('numero di vertici')
    plt.xlim([np.min(X), np.max(X)])
    plt.ylim([0, np.max(Yt) * 1.2])
    plt.plot(X, C*Y, 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
    plt.plot(X, Yt, 'b-', label='T(n)=N^3')
    plt.legend(loc='upper left')
    plot = plt
    return plot

def generateShortPath(Sample,Node):
	# calcolo dei campioni
	dictTime = {}
	for j in range(1, Sample):
		Graph = GraphAdjacencyList()

		nodes = []
		for i in range(Node):
			node = Graph.addNode(i)
			nodes.append(node)

			for node_src in nodes:
				for node_dst in nodes:
					if node_src != node_dst:
						N = Graph.numNodes()

						if N not in dictTime.keys():
							dictTime[N] = []

						Graph.insertEdge(node_src.id, node_dst.id, 1)
						Graph.insertEdge(node_dst.id, node_src.id, 1)

						inizio = time.clock()
						FloydWarshall_ADJ(Graph)
						fine = time.clock() - inizio

						dictTime[N].append(fine)


	X = []
	Y = []

	for key in sorted(dictTime.keys()):
		X.append(key)
		M = np.mean(np.array(dictTime[key]))
		Y.append(M)

	X = np.array(X)
	Y = np.array(Y)
	Yt = np.power(X, 3)
	R = Yt / Y
	C = np.max(R)

	plt.figure('Tempo calcolo percorsi minimi di G con FloydWarshall')
	plt.grid(True)
	plt.title('Tempo calcolo percorsi minimi di G con FloydWarshall')
	plt.ylabel('andamento temporale')
	plt.xlabel('numero di vertici')
	plt.xlim([np.min(X), np.max(X)])
	plt.ylim([0, np.max(Yt) * 1.2])
	plt.plot(X, C*Y, 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
	plt.plot(X, Yt, 'b-', label='T(n)=N^3')
	plt.legend(loc='upper left')
	plot = plt
	return plot

def generateNodesMean(Sample,Node):
	# calcolo dei campioni
	dictTime = {}
	for j in range(1, Sample):
		Graph = GraphAdjacencyList()

		nodes = []
		for i in range(Node):
			node = Graph.addNode(i)
			nodes.append(node)

			for node_src in nodes:
				for node_dst in nodes:
					if node_src != node_dst:
						N = Graph.numNodes()

						if N not in dictTime.keys():
							dictTime[N] = []

						Graph.insertEdge(node_src.id, node_dst.id, 1)
						Graph.insertEdge(node_dst.id, node_src.id, 1)

						inizio = time.clock()
						Nodes_Mean(Graph)
						fine = time.clock() - inizio

						dictTime[N].append(fine)


	X = []
	Y = []

	for key in sorted(dictTime.keys()):
		X.append(key)
		M = np.mean(np.array(dictTime[key]))
		Y.append(M)

	X = np.array(X)
	Y = np.array(Y)
	Yt = np.power(X, 4)
	R = Yt / Y
	C = np.mean(R)

	plt.figure('Tempo calcolo dei nodi medi dei percorsi')
	plt.grid(True)
	plt.title('Tempo calcolo dei nodi medi dei percorsi')
	plt.ylabel('andamento temporale')
	plt.xlabel('numero di vertici')
	plt.xlim([np.min(X), np.max(X)])
	plt.ylim([0, np.max(Yt) * 1.2])
	plt.plot(X, C*Y, 'r-', label='T(n) misurato con {0} campioni'.format(Sample))
	plt.plot(X, Yt, 'b-', label='T(n)=N^3')
	plt.legend(loc='upper left')
	plot = plt
	return plot


if __name__ == "__main__":
    #plotA = generateAddNoneMeasure( 100 , 21 )
    #plotB = generateInsertEdgeMeasure(100, 21)
    #plotC = generateDegMeasure(100, 41)
    #plotD = generateGraphTestMeasure(1000)
	#plotE = generateShortPath(100, 11)
	plotF = generateNodesMean(10, 11)

    #plotA.show()
    #plotB.show()
    #plotC.show()
    #plotD.show()
	#plotE.show()
	plotF.show()

