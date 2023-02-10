# Uses python3
import sys
import time
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_fast(n, m):
    #intializing pisaont period variable and previous and current
    PisaontPeriod=0
    previous, current = 0, 1
    #looping over m*m as the period range won't exceed that number
    for i in range(0, m **2):
       #swapping previoud and current then changing current and getting it's moduls with m
        previous , current = current, (previous + current) % m
         
        # A Pisano Period starts with 01 so when we reach 0 and 1 give me lenght of the period which is i+1
        if (previous == 0 and current == 1):
            PisaontPeriod= i + 1
    #on knowing the period and from the special pattern of fibonacci n%PisaontPeriodLength>>gives N and Fn%M=FN%M
    n = n % PisaontPeriod
      
    return get_fibonacci_huge_naive(n,m)
if __name__ == '__main__':
    input = sys.stdin.read()

    n, m = map(int, input.split())

    print(get_fibonacci_huge_fast(n, m))

