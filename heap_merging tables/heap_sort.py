#python3
import sys
## HeapSort sorts in place ##

def heapify(arr,n,i):
    # Get Max among root and children
    Max = i  # Initialize Max as root
    left = 2 * i + 1     # leftchild = 2*i + 1
    right = 2 * i + 2     # rightchild = 2*i + 2
    # Check if left child of root exists and is less than root
    if left < n and arr[Max] < arr[left]:
        Max = left
    # See if right child of root exists and is less than root
    if right < n and arr[Max] < arr[right]:
        Max = right
    # If root is not Max, swap with Max and continue heapifying
    if Max != i:
        arr[i], arr[Max] = arr[Max], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, Max)
def heap_sort(arr):
    # Write your code here
    n = len(arr)
    # Build Max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        # Swap all to root to heapify
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)
    return arr

### DO NOT CHANGE INPUT/OUTPUT FORMAT ####

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    heap_sort(a)
    for x in a:
        print(x, end=' ')

