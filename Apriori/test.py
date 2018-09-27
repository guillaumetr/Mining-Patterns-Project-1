# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:07:52 2018

@author: Guillaume
"""

import os 
os.chdir("C:\\Users\Guillaume\Google Drive\Master Data Sciences\Q3\Mining patterns in data\Projet\Apriori")

from frequent_itemset_miner import *

toy_data = Dataset(r"C:\\Users\Guillaume\Google Drive\Master Data Sciences\Q3\Mining patterns in data\Projet\Apriori\datasets\toy.dat")

# select candidates according to the required min_support
def create_cand1(set_items):
    can1=list()
    for i in set_items:
        can1.append([i])
    can1=list(map(frozenset,can1))
    return can1
    
    
    
def min_support_cand(transactions,candidates,min_frequency):
    support = {}
    for item_set in transactions:
        for can in candidates:
            if can.issubset(item_set):
                    if can in support.keys():               
                        support[can]+=1
                    else:
                        support[can]=1
    frequency = {}
    can_selected = list()
    for can in support.keys():
        if support[can]/len(transactions) >= min_frequency:
            frequency[can]=support[can]/len(transactions)
            can_selected.append(can)
    return can_selected,frequency


def gen_next_cand(candidates):
    next_cand=[]
    k = len(candidates)
    for i in range(k) :
        for j in range(i+1,k):
            next_cand.append(candidates[i]|candidates[j])
    return next_cand

      
        
# Apriori algorithm 
frequency={}
cand1=create_cand1(toy_data.items)
stop=False
indice=0
candidates = []
transactions=list(map(frozenset,toy_data.transactions))

while stop == False:
    if indice !=0:
        candidates = gen_next_cand(candidates)
    else:
        candidates = cand1
        
    candidates,new_freq = min_support_cand(transactions,candidates,0.2)
    frequency.update(new_freq)
    
    if(len(candidates)==0):
        stop=True
    indice +=1
    
    




