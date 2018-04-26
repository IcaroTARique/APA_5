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
        self.grafo = [[0 for column in range(vertices)]
                      for row in range(vertices)]


    def printMST(self, pai):
        print ("Vértice \tW")
        for i in range(1,self.V):
            print (CorDaLetra.negrito,CorDeFundo.verde,pai[i],"-",i,"\t",self.grafo[i][ pai[i] ],CorDaLetra.original)

    def minKey(self, key, mstSet):


        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index


    def primMST(self):


        key = [sys.maxsize] * self.V
        pai = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        pai[0] = -1

        for cout in range(self.V):

            u = self.minKey(key, mstSet)


            mstSet[u] = True

            for v in range(self.V):

                if self.grafo[u][v] > 0 and key[v] > self.grafo[u][v] and mstSet[v] == False:
                        key[v] = self.grafo[u][v]
                        pai[v] = u

        self.printMST(pai)

g  = Grafo(4)
g.grafo = [[0,23,17,19],
           [23,0,22,20],
           [17,22,0,25],
           [19,20,25,0],];


g.primMST();