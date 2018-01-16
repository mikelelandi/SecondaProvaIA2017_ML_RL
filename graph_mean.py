#!/usr/bin/env python
"""
	File name:				graph_mean.py
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
	 
	Progettare e implementare un algoritmo che, dato un grafo non orientato e non 
	pesato ​G​, determini il nodo ​m*​ che risulta essere ​medio per il maggior numero di coppie di nodi​.
"""

import random
from graph.shortestPaths import FloydWarshall_ADJ
from graph_test import Graph_Test

def Nodes_Mean(graph):
    """
    :param graph: deve essere uun oggetto di tipo grafo con Lista di adiacenza
    :return: lista del nodo medio o dei nodi medi a parimerito che risultano essere medio per il maggior numero di coppie di numeri
             esempio di lista :[[m*,c]] tale che m* è ID del nodo, c è il valore del numero delle coppie di nodi
    """

    # inizializiamo una lista ListIdNode composta dagli ID dei nodi del grafo, e un valore di contantore associato pari a 0
    # e un valore di indice all'interno della matrice
    # tempo teorico di esecuzione O(N)
    listIdNode = []
    countId=0
    for Node in graph.getNodes():
        listIdNode.append([Node.id,0,countId])
        countId=countId+1


    # inizializiamo una lista ListTemp composta dagli ID della sequenza dei nodi medi di tutte le coppie di nodi possibili
    # tempo teorico di esecuzione O(1)
    listTemp=[]


    # otteniamo la matrice con tutti i percorsi minimi tra tutte le possibili coppie di nodi del grafo
    # tempo di esecuzione teorico O(N^3)
    distances = FloydWarshall_ADJ(graph)


    # cerchiamo i percorsi minimi in cui è possibile calcolare un nodo medio m* tale che dist(n1,m*) ​=  dist(m*,n2)
    # dato che la matrice dei percorsi minimi è simmetrica ed il grafo non è orientato, l'elaborazione del minimo
    # è eseguita solo per la parte superiore alla diagonale della matrice
    # tempo di esecuzione teorico O(N^3)
    for i in range(0, graph.numNodes()-1):
        for j in range(i+1, graph.numNodes()):
            # il calcolo del nodo medio non viene eseguito se non esiste un arco tra la coppia di nodi in esame
            # e se nel percorso minimo della coppia di nodi sono presenti un numero di nodi pari
            if i != j and distances[i][j] != float('inf') and distances[i][j] % 2 == 0:
                # si procede in una visita in profondità per tutti i nodi ottenendo ID dei nodi del percorso
                listDfs=graph.dfs(listIdNode[i][0])
                count=0
                # si procede alla realizzazione di una lista ausiliaria della visita in profondità per tutti i nodi ottenendo la posizione
                # all'interno della matrice dei nodi del percorso
                listDfs2=[]
                while count<len(listIdNode):
                    if listIdNode[count][0] in listDfs:
                        listDfs2.append(listIdNode[count][2])
                    count=count+1
                # ciclo for per elaborare la posizione all'interno della matrice del nodo medio
                for m in listDfs2:
                    if distances[i][m] == distances[m][j] and \
                       distances[i][m] != float('inf') and \
                       distances[m][j] != float('inf') and \
                       distances[i][m] != 0 and \
                       distances[m][j] != 0:
                        #individuato se esiste il nodo medio m aggiorniamo la lista listTemp
                        listTemp.append(listIdNode[m][0])
                        break


    # procedimento per aggiornare il valore dei contatori associato a ogni nodo nella lista listIdNode
    # tempo di esecuzione teorico O(N^3)
    for q in range (0,len(listTemp)):
        for k in range (0,len(listIdNode)):
         if listTemp[q]==listIdNode[k][0]:
            listIdNode[k][1]=listIdNode[k][1]+1


    # creazione di uno struttura dati ad arrey medNode composto dall'ID e valore del contatore associato
    # del nodo o dei nodi che risultano essere i nodi medi per il maggior numero di coppie di nodi
    # tempo di esecuzione teorico O(N)
    medNode=[]
    for w in range (0,len(listIdNode)):
        if len(medNode)==0:
           medNode = [[listIdNode[0][0],listIdNode[0][1]]]
        elif listIdNode[w][1] > medNode[0][1]:
           medNode = [[listIdNode[w][0], listIdNode[w][1]]]
        elif (listIdNode[w][1])== (medNode[0][1]):
           medNode.append([listIdNode[w][0], listIdNode[w][1]])


    #verifica per caso limite in cui non esiste nessun nodo medio
    #tempo di esecuzione teorico O(1)
    if medNode[0][1]==0:
      medNode = []


    return(medNode)





if __name__ == "__main__":

    graph = Graph_Test.generateGraph()

    D = FloydWarshall_ADJ(graph)

    print ("---- print del grafo ----")
    graph.print()

    print ("---- Matrice dei minimi percorsi ----")
    for elm in D:
        print (elm)


    print("---- Nodo/Nodi medi più frequente [x,y] | x= ID nodo y= numero coppie di nodi per cui è medio ----")
    print(Nodes_Mean(graph))
