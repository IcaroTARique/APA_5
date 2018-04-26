#!/usr/bin/python3.5
#coding: utf-8
import sys

class CorDeFundo(object):
    vermelho = '\033[41m'
    verde = '\033[42m'
    azul = '\033[44m'
    ciano = '\033[46m'
    magenta = '\033[45m'
    amarelo = '\033[43m'
    branco = '\033[47m'
    preto = '\033[40m'

class CorDaLetra(object):
    vermelho ='\033[31m'
    verde ='\033[32m'
    azul ='\033[34m'
    ciano ='\033[36m'
    magenta ='\033[35m'
    amarelo ='\033[33m'
    preto ='\033[30m'
    branco ='\033[37m'
    original ='\033[0;0m'
    reverso ='\033[2m'
    negrito = '\033[1m'

class Grafo():

    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for coluna in range(vertices)]
                      for linha in range(vertices)]

    def minDistance(self, dist, sptSet):

        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.grafo[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.grafo[u][v]:
                        dist[v] = dist[u] + self.grafo[u][v]

        print ("Vertices e suas distâncias")
        for no in range(self.V):
            if(no != dist[no]):
                print (CorDeFundo.branco, CorDaLetra.preto,no,"------",dist[no],CorDaLetra.original)


g  = Grafo(4)
g.grafo = [[0,23,17,19],
           [23,0,22,20],
           [17,22,0,25],
           [19,20,25,0],];

g.dijkstra(0);