#Uses python3
import sys

def lcs2(a, b):
    #write your code here
    m,n = len(a),len(b) #length of a     ,length of b

  
    # declaring the array for storing the length values
    LCS_ARR = [[None]*(n + 1) for i in range(m + 1)]
   # (+1) as we put first row and column by zeros
    for i in range(m + 1):
        for j in range(n + 1):
            #putting zeros in first column and row
            if i == 0 or j == 0 :
                LCS_ARR[i][j] = 0
            #else check if items are matching 
            elif a[i-1] == b[j-1]:
            #increase previous value by 1 we found a match
                LCS_ARR[i][j] = LCS_ARR[i-1][j-1]+1
            else:
            #else put max recent length
                LCS_ARR[i][j] = max(LCS_ARR[i-1][j], LCS_ARR[i][j-1])
  
    # L[m][n] contains the length of Longest common sequence
    return LCS_ARR[m][n]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
