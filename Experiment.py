# CISC 365 - Assignment 2
# Created by David Kubik
# Part 2 : Conducting experiments to explore the relative efficiency of the two algorithms

import random

def BFI_Subset_Sum(s,k):
    global BFI_counter
    sets = [[]]
    
    for i in range(0,len(s)):
        lengthOfSets = len(sets)
        for j in range(0, lengthOfSets):
            BFI_counter += 1 
            temp = sets[j] + [s[i]]
            sets.append(temp)
            BFI_counter += 1
            if sum(temp) == k:
                return temp
    return None

def modified_BFI_Subset_Sum(s):
    global HS_counter
    sets = [[]]
    
    for i in range(0,len(s)):
        lengthOfSets = len(sets)
        for j in range(0, lengthOfSets):
            temp = sets[j] + [s[i]]
            sets.append(temp)
            HS_counter += 1
            
    return sets

def HS_Subset_Sum(s, k):
    global HS_counter 
    s_left = s[:len(s)//2]
    s_right = s[len(s)//2:]
    listOfLeftSubsets = modified_BFI_Subset_Sum(s_left) # Counter goes up in the modified version  
    listOfRightSubsets = modified_BFI_Subset_Sum(s_right)
    for i in listOfLeftSubsets:
        HS_counter += 1 # Counter goes up by one since it's calculating sum for each element
        if sum(i) == k:
            return i
    for i in listOfRightSubsets:
        HS_counter += 1 # Counter goes up by one since it's calculating sum for each element
        if sum(i) == k:
            return i
        
    listOfLeftSubsets.sort()
    HS_counter += 1 # Counter goes up by one since sorting is an operation
    listOfRightSubsets.sort()
    HS_counter += 1 # Counter goes up by one since sorting is an operation
    if Pair_Sum(listOfLeftSubsets, listOfRightSubsets, k) == None:
        return None
    else:
        print (Pair_Sum(listOfLeftSubsets, listOfRightSubsets, k))

def Pair_Sum(Values_1, Values_2, k):
    global HS_counter
    p1 = 0
    p2 = (len(Values_2)-1)
    
    while p1 <= (len(Values_1)-1) and (p2 >= 0):
        combo = Values_1[p1] + Values_2[p2]
        HS_counter += 2 # Counter goes up by two because it's accessing both lists
        t = sum(combo)
        if t == k:
            return (p1, p2)
        elif t < k:
            p1 = p1 + 1
        else:
            p2 = p2 - 1
    return None

#Testing

BFI_counter = 0 #Counts the number of operations for the BFI algorithm
HS_counter = 0 #Counts the number of operations for the HS algorithm

for n in range(4,15): # set sizes
    
    for i in range(1, 20): # number of tests
        
        S = [random.randint(0,100) for num in range(n)] # Generate a set S of n random integers
        target = [random.randint(0,100) for num in range(10)] # Generate a set of at least 10 target values

        for k in target: # for each target value
            BFI_Subset_Sum(S,k) 
            HS_Subset_Sum(S,k)
            
        averageBFI_set = BFI_counter // i # compute the average number of operations for BFI_Subset_Sum for this set
        averageHS_set = HS_counter // i # compute the average number of operations for HS_Subset_Sum for this set
        
    averageOpsBFI = BFI_counter // n # compute the average number of operations for BFI_Subset_Sum for this n
    averageOpsHS = HS_counter // n # compute the average number of operations for HS_Subset_Sum for this n
            
#Tabulate the computed average numbers of operations.

        
