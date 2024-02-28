#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: giuseppebondi
"""

import networkx as nx

import matplotlib.pyplot as plt

def carica_parole_da_file(nome_file):
    with open(nome_file, 'r', encoding='utf-8') as file:
        parole = set(parola.strip().lower() for parola in file)
    return parole

# Carica le parole italiane da un file di testo
italian_words = carica_parole_da_file('parole_ita.txt')


def filterArray(lettere):
    filtrate = set()
    for parola in italian_words:
        if len(parola)==lettere:
            filtrate.add(parola)
    return filtrate


#check Dist Uno
def parole_a_una_lettera_di_distanza(parola):
    parole = []
    # Prova a cambiare ogni lettera della parola con ogni lettera dell'alfabeto
    for i in range(len(parola)):
        for lettera in 'abcdefghijklmnopqrstuvwxyz':
            nuova_parola = parola[:i] + lettera + parola[i + 1:]
            if nuova_parola in italian_words and nuova_parola != parola:
                parole.append(nuova_parola)
    return parole


class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def aggiungi_vertice(self, vertice):
        self.grafo.add_node(vertice)

    def aggiungi_arco(self, vertice1, vertice2):
        self.grafo.add_edge(vertice1, vertice2)

    def plot_grafo(self):
        pos = nx.spring_layout(self.grafo)  # Posizionamento dei nodi
        nx.draw(self.grafo, pos, with_labels=True, font_weight='bold')
        plt.show()
    
    def VertList(self, listaVertici, daNodo):
        for Vert in listaVertici:
            self.aggiungi_vertice(Vert)
            self.aggiungi_arco(daNodo, Vert)
            #self.VertList(parole_a_una_lettera_di_distanza(Vert), Vert)ù
            
    def WriteGraph(self, path):
        self.grafo.write_gexf(grafo, path)
    
    

grafo = Grafo()

for parola in italian_words:
    grafo.aggiungi_vertice(parola)
    grafo.VertList( parole_a_una_lettera_di_distanza(parola),parola )
    

nx.write_gexf(grafo.grafo, "Grafo_italian_words.gexf")


