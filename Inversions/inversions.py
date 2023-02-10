# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    #write your code here

    number_of_inversions=0
    # if array is empty or has 1 element return 0
    if right <= left:
        return number_of_inversions
    ave=(left+right)//2     # we get mid point to divide the array
    #going from left to mid in first call and it repeats  and divide each time
    number_of_inversions+=get_number_of_inversions(a,b,left,ave)
    #going from mid+1 to last point and it repeats and divide each time
    number_of_inversions+=get_number_of_inversions(a,b,ave+1,right)
    # now we call merge and give it array and temp array our left and mid and right
    number_of_inversions += merge(a, b, left, ave+1, right)
    #finally return our number of inversions
    return number_of_inversions
 

def merge(arr, temp_arr, left, mid, right):
    i = left     #starting with first index which is in left array
    j = mid  # starting with first index in right array
    k = left     # Starting index of to be sorted subarray
    Number_of_Inversions = 0

    # Conditions to make sure that i and j donot exceed their limits
    
    while i <= mid-1 and j <= right:
        # There will be no inversion if arr[i] <= arr[j] which means it's in right place

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]

            i += 1
        else:
            #if a[i] is greater than a[j], then there are (mid – i) inversions as left and righ subarraies are sorted
            temp_arr[k] = arr[j]
            # else Inversion will happen.
            Number_of_Inversions += (mid-i )
            j += 1
        k += 1

    # Copy any remaining elements of left to our array

    while i <= mid-1:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
 
    # Copy any remaining elements of right to our array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    #put sortted in original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
   
        
    return Number_of_Inversions
if __name__ == '__main__':
    # DO NOT change this code
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
