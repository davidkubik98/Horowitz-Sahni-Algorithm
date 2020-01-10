# CISC 365 - Assignment 2
# Created by David Kubik
# Part 1

import random

def BFI_Subset_Sum(s,k):
    # Naive algorithm that generates all subsets and computes the sum of each one.
    sets = [[]] 
    for i in range(0,len(s)): #Creates a new set for each combination
        lengthOfSets = len(sets)
        for j in range(0, lengthOfSets):
            temp = sets[j] + [s[i]] 
            sets.append(temp)
            if sum(temp) == k: #Creates a temporary sum and compares it to the target, k.
                return temp
    return None #No solution found

def modified_BFI_Subset_Sum(s):
    #Modified algorithm that generates all the subsets of a set.
    sets = [[]]
    for i in range(0,len(s)):
        lengthOfSets = len(sets)
        for j in range(0, lengthOfSets):
            temp = sets[j] + [s[i]]
            sets.append(temp)
    return sets 

def HS_Subset_Sum(s, k):
    #Horowitz-Sahni algorithm
    #Splits the set into two different sets
    s_left = s[:len(s)//2]
    s_right = s[len(s)//2:]
    #Uses the modified algorithm to get all the subsets of each set.
    listOfLeftSubsets = modified_BFI_Subset_Sum(s_left) 
    listOfRightSubsets = modified_BFI_Subset_Sum(s_right)
    #Checks all the sums to see if they add up to the target value.
    for i in listOfLeftSubsets:
        if sum(i) == k:
            return i
    for i in listOfRightSubsets:
        if sum(i) == k:
            return i
    #None of the sums add up to the target value, sort the lists to prepare for the PairSum function
    listOfLeftSubsets.sort()
    listOfRightSubsets.sort()
    #Using the PairSum function
    if Pair_Sum(listOfLeftSubsets, listOfRightSubsets, k) == None:
        return None
    else:
        print (Pair_Sum(listOfLeftSubsets, listOfRightSubsets, k))

def Pair_Sum(Values_1, Values_2, k):
    p1 = 0
    p2 = (len(Values_2)-1)
    
    while p1 <= (len(Values_1)-1) and (p2 >= 0):
        combo = Values_1[p1] + Values_2[p2]
        t = sum(combo)
        if t == k:
            return (p1, p2)
        elif t < k:
            p1 = p1 + 1
        else:
            p2 = p2 - 1
    return None

#Testing

array = [3,5,3,9,18,4,5,6]
n = int(28)
n2 = int(52)

print ("Checking BFI_Subset_Sum with array [3,5,3,9,18,4,5,6] and target 28:")
if (HS_Subset_Sum(array,n)) == None:
    print ("No solutions found")
else:
    print (HS_Subset_Sum(array,n))
print()

print ("Checking BFI_Subset_Sum with array [3,5,3,9,18,4,5,6] and target 52:")
if (HS_Subset_Sum(array,n2)) == None:
    print ("No solutions found")
else:
    print (HS_Subset_Sum(array,n2))
print()

print ("Checking HS_Subset_Sum with array [3,5,3,9,18,4,5,6] and target 28:")
if (HS_Subset_Sum(array,n)) == None:
    print ("No solutions found")
else:
    print (HS_Subset_Sum(array,n))
print ()

print ("Checking HS_Subset_Sum with array [3,5,3,9,18,4,5,6] and target 52:")
n2 = int(52)
if (HS_Subset_Sum(array,n2)) == None:
    print ("No solutions found")
else:
    print (HS_Subset_Sum(array,n2))
print ()









