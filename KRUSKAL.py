#!/usr/bin/python3.5
#coding: utf-8
from collections import defaultdict

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

class Grafo:

    def __init__(self,vertices):
        self.V= vertices    #Numero de vértices
        self.grafo = []     # lista para armazenar o grafo


    #Função que adiciona vértices e arestas
    def addVertice(self,u,v,w):
        self.grafo.append([u,v,w])

    def find(self, pai, i):
        if pai[i] == i:
            return i
        return self.find(pai, pai[i])

    def union(self, pai, rank, x, y):
        xroot = self.find(pai, x)
        yroot = self.find(pai, y)

        if rank[xroot] < rank[yroot]:
            pai[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            pai[yroot] = xroot

        else :
            pai[yroot] = xroot
            rank[xroot] += 1

    #CONSTROIA ARVORE DE ESPALHAMENTO MÍNIMO
    def KruskalMST(self):

        #RESULTADO DA ARVORE
        Arvore_Final =[]

        i = 0
        e = 0

        #PASSO 2: COLOCAMOS AS ARESTAS EM MODO CRESCENTE
        #SE NÃO PODEMOS MODIFICAR O GRAFO, CRIAMOS CÓPIA
        #DO JÁ EXISTENTE.

        #comando sorted cria uma nova lista e atriui a ela o
        #valor da lista passada de modo ordenado
        #key=lambda é uma função anônima que passa (nesse caso)
        #o parametro pelo qual será ordenado que é representado
        #pelo item no segundo espaço da TUPLA
        print(CorDaLetra.amarelo,"TUPLA ORIGINAL :: ",self.grafo,CorDaLetra.original)
        self.grafo =  sorted(self.grafo,key=lambda item: item[2])
        print(CorDaLetra.ciano,"TUPLA ORDENADA :: ",self.grafo,CorDaLetra.original)

        pai = []
        rank = []

        print(CorDaLetra.verde,"self.V :: ",self.grafo,CorDaLetra.original)
        #INICIA O RANK - (Pra fazer união por rank)
        #DEFINE O ARRAY PAI
        for no in range(self.V):
            pai.append(no)
            #print(CorDaLetra.vermelho,node,CorDaLetra.original)
            rank.append(0)
            #print(CorDaLetra.magenta,rank,CorDaLetra.original)
        print(CorDaLetra.magenta,"rank ",rank,CorDaLetra.original)
        print(CorDaLetra.magenta,"pai",pai,CorDaLetra.original)

        while e < self.V -1 :
            #PASSO 2: Escolhe a menor aresta e incrementa o indice
            #para ser executada a próxima iteração

            u,v,w =  self.grafo[i] #VARIAVEIS U V & W RECEBEM OS
            #VALORES ATUAIS DO GRAFO
            i = i + 1

            print(CorDaLetra.amarelo,"pai : ",pai[i],CorDaLetra.original)
            print(CorDaLetra.amarelo,"iteração : ",i,CorDaLetra.original)
            print(CorDaLetra.vermelho,"u : ",u,CorDaLetra.original)
            print(CorDaLetra.verde,"v : ",v,CorDaLetra.original)

            x = self.find(pai, u)
            print(CorDaLetra.vermelho,"x : ",x,CorDaLetra.original)

            y = self.find(pai ,v)
            print(CorDaLetra.verde,"y : ",y,CorDaLetra.original)

            #VERIFICA SE U É IGUAL A V PARA SABER SE PODE FAZER
            #PARTE DA SOLUÇÃO
            if x != y:
                e = e + 1
                Arvore_Final.append([u,v,w])
                self.union(pai, rank, x, y)

        #IMPRIME O CONTEUDO DE U, V E W
        print ("VERTICES DA ARVORE DE ESPALHAMENTO MÍNIMO")
        for u,v,w  in Arvore_Final:
            print (u,"-->",v,"---",w)

### MAIN
g = Grafo(4)
g.addVertice(0, 1, 23)
g.addVertice(0, 2, 17)
g.addVertice(0, 3, 19)
g.addVertice(1, 2, 22)
g.addVertice(1, 3, 20)
g.addVertice(2, 3, 25)
print(CorDaLetra.azul,g.grafo,CorDaLetra.original)

g.KruskalMST()