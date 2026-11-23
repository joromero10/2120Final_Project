#Pseudocode for sets asking users for all elements in set, determining whether sets are a proper set of each other 
#and drawing a venn diagram of the sets 
import math
import pandas

def set_elements():
    #Prompt user for elements of the first set
    setA = input("Enter the elements of the first set separated by commas: ")
    setA = {int(item.strip()) for item in setA.split(",")}
    print("The elements of the first set (set A) are: ", setA)
    
    #Prompt users for elements of the second set
    setB = input("Enter the elements of the second set separated by commas: ")
    setB = {int(item.strip()) for item in setB.split(",")}
    print("The elements of the second set (set B) are: ", setB)

set_elements()