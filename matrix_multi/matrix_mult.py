# Uses python3
import numpy as np
import math
def splitMatrix(matrix):

   
    row, col = matrix.shape #get matrix shape

    row2, col2 = row//2, col//2 #divide it by 2
    # return the matrix divided into 4 matrices
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
def CalculateFast(A, B, n):
    # Write your BONUS code here
    
    if len(A) == 1 and len(B)==1:  # IF matrix size is 1x1
        return A * B        #return product
    #split matrix A and B into 4 matrices until it's 1x1 to return their product
    A11, A12, A21, A22 = splitMatrix(A)
    B11, B12, B21, B22 = splitMatrix(B)
    #call the function 8 times to get p1 To p7 and on each call's end it returns C to that Call
    p1 = CalculateFast(A11, B12 - B22,n) 
    p2 = CalculateFast(A11 + A12, B22,n)       
    p3 = CalculateFast(A21 + A22, B11,n)       
    p4 = CalculateFast(A22, B21 - B11,n)       
    p5 = CalculateFast(A11 + A22, B11 + B22,n)       
    p6 = CalculateFast(A12 - A22, B21 + B22,n) 
    p7 = CalculateFast(A11 - A21, B11 + B12,n)
    #once calculated put values in C 
    C11 = p5 + p4 - p2 + p6 
    C12 = p1 + p2          
    C21 = p3 + p4           
    C22 = p1 + p5 - p3 - p7 
    #C matrix
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    #return C at last or for each call to use it above also from used :n to avoid zeros from padding
    return C[:n,:n]

def matrix_mult_fast(A,B,n):
    #check neareast rounded power of 2 and using int as it returns float
    CheckPowerOf2=int(pow(2,np.ceil(np.log(n)/np.log(2))))
    #padding check
    checked=False
    if  checked==False:
        pad=CheckPowerOf2
        #pad the matrix with pad-n so it's always correct for example for n=6 pad=8>> so we do 8-6 to get 2 as padding size
        A=np.pad(A, [(0, pad-n), (0, pad-n)], mode='constant')
        B=np.pad(B, [(0, pad-n), (0, pad-n)], mode='constant')
        checked=True
        #now go calculate using padded A and B 
    return CalculateFast(A,B,n)

def matrix_mult(A,B,n):
    #check neareast rounded power of 2 and using int as it returns float

    CheckPowerOf2=int(pow(2,np.ceil(np.log(n)/np.log(2))))
    #padding check

    checked=False
    if  checked==False:
        pad=CheckPowerOf2
        #pad the matrix with pad-n so it's always correct for example for n=6 pad=8>> so we do 8-6 to get 2 as padding size

        A=np.pad(A, [(0, pad-n), (0, pad-n)], mode='constant')
        B=np.pad(B, [(0, pad-n), (0, pad-n)], mode='constant')
        checked=True
        #now go calculate using padded A and B

    return CalculateNaive(A,B,n)
def CalculateNaive(A, B, n):
   
    if len(B) == 1 and len(A)==1:  # IF matrix size is 1x1
        return A * B #return product
    else:
        #split matrix A and B into 4 matrices until it's 1x1 to return their product

        A11, A12, A21, A22 = splitMatrix(A)
        B11, B12, B21, B22 = splitMatrix(B)
#call function 8 times to calculate C and on each Call's end it returns a C to that call
        C11=CalculateNaive(A11,B11,n)+CalculateNaive(A12,B21,n)
        C12=CalculateNaive(A11,B12,n)+CalculateNaive(A12,B22,n)
        C21=CalculateNaive(A21,B11,n)+CalculateNaive(A22,B21,n)
        C22=CalculateNaive(A21,B12,n)+CalculateNaive(A22,B22,n)

        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    #finally return C to a call or in the end also from used :n to avoid zeros from padding
    return C[:n,:n]


if __name__ == '__main__':
    n = int(input())
    A = []
    B = []
    # Enter matrix 1 values, press enter after each row
    # Matrix 1 filling
    for i in range(n):
        A.append([int(j) for j in input().split()]) 

    # Enter matrix 2 values, press enter after each row
    # Matrix 2 filling
    for i in range(n):
        B.append([int(j) for j in input().split()]) 

    A = np.array(A)
    B = np.array(B)

    print(matrix_mult(A, B, n))

    ''' UNCOMMENT this line if you will submit BONUS'''
    print(matrix_mult_fast(A, B, n))