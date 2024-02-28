#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: giuseppebondi
"""
import networkx as nx

def carica_parole_da_file(nome_file):
    with open(nome_file, 'r', encoding='utf-8') as file:
        parole = set(parola.strip().lower() for parola in file)
    return parole

# Carica le parole italiane da un file di testo


source = str(input("Inserisci radice: "))

target = str(input("Inserisci target: "))

if len(source)==len(target):
    
    italian_words = carica_parole_da_file('parole_ita.txt')
    
    src = False
    trgt = False
    
    if source in italian_words:
        src =True
    else :
        print ("source non presente nel dizionario")
        
    
    if target in italian_words:
        trgt= True
    else:
        print ("target non presente nel dizionario")
    
    if src and trgt:
        
        print("Caricamento grafo....")
        
        grafo=nx.Graph()
        
        grafo=nx.read_gexf("Grafo_italian_words.gexf",str)
        
        print("Ricerca metagramma...")
        
        print (nx.dijkstra_path(grafo, source, target))
        
    
else:
    print("le parole inserite non hanno la stessa lunghezza, riprova" )