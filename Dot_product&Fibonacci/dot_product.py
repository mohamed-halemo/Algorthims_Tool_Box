#Uses python3

import sys
import time
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(len(arr)):
 
        # Last i elements are already in place so we subtract i
        for j in range(0, n-i-1):
            
            #loop through all to n-i-1
            #keep checking each 2 elements next to each other
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]             # Swap if the element found is greater

    return arr

def max_dot_product(a, b):
    #sorted a and b to get maximum dot product which is sum of multiplicatoins at the end
    SortedA=bubbleSort(a)
    SortedB=bubbleSort(b)
    Summation=0
    #looped over a , b would work also as both have n elements
    #then add the summation of their product
    for i in range(len(a)):
        Summation=Summation+SortedA[i]*SortedB[i]
    
    return Summation

if __name__ == '__main__':
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
