# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:07:52 2018

@author: Guillaume
"""

# working directory
import os 
os.chdir(r"C:\\Users\Guillaume\Documents\GitHub\Mining-Patterns-Project-1\Apriori")

#import the module frequent_itemset_miner
from frequent_itemset_miner import *

# creation of the first candidates from the different individual items
def create_cand1(set_items):
    can1=list()
    for i in set_items:
        can1.append([i])
    can1=list(map(frozenset,can1))
    return can1
    
    
# method that count the frequency for specfic candidates and select the ones which match with the minimal frequency
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

# method that generate new candidates based on those which have been selected
# hyper naive --> TO BE IMPROVED
def gen_next_cand(candidates):
    next_cand=[]
    k = len(candidates)
    for i in range(k) :
        for j in range(i+1,k):
                if candidates[i]|candidates[j] not in next_cand:
                        next_cand.append(candidates[i]|candidates[j])
    return next_cand


        
# Apriori algorithm 
def apriori(filepath, minFrequency):
    
    dataset = Dataset(filepath)
    
    frequency={}
    cand1=create_cand1(dataset.items)
    stop=False
    first=True
    candidates = []
    transactions=list(map(frozenset,dataset.transactions))

    while stop == False:
        if first==False:
            candidates = gen_next_cand(candidates) 
        else:
            candidates = cand1
            first=False
         
        candidates,new_freq = min_support_cand(transactions,candidates,0.2)
        frequency.update(new_freq)
    
        if(len(candidates)==0):
            stop=True
   
    return frequency

#test
apriori(r"C:\\Users\Guillaume\Google Drive\Master Data Sciences\Q3\Mining patterns in data\Projet\Apriori\datasets\toy.dat",0.2)
