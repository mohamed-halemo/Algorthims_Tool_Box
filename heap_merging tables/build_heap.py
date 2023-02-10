# python3

def heapify(arr,n,i,swaps):

    # Get Min among root and children
    Min = i  # Initialize Min as root
    left = 2 * i + 1     # leftchild = 2*i + 1
    right = 2 * i + 2     # rightchild = 2*i + 2
    # See if left child of root exists and is less than root
    if left < n and arr[Min] > arr[left]:
        Min = left
    # See if right child of root exists and is less than root
    if right < n and arr[Min] > arr[right]:
        Min = right
    # If root is not Min, swap with Min and continue heapifying and append in swaps 
    if Min != i:
        swaps.append((i, Min))
        arr[i], arr[Min] = arr[Min], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, Min,swaps)
def build_heap(data):
    n = len(data) #len of arr
    swaps=[]    #swaps 
    for i in range(n // 2 - 1, -1, -1): #looping on the array to heapify it or to sift it    
            heapify(data, len(data), i,swaps)   #heapify
    return swaps
            
def main():
    #####   DO NOT CHANGE THE CODE IN THIS PART #########
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
