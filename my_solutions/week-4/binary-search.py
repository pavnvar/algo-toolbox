# Uses python3
import sys
import math

def binary_search(a, x, left, right):
    if right >= left:
        mid = (left + right)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x :
            result = binary_search(a,x,left,mid-1)
        elif a[mid] < x:
            result = binary_search(a,x,mid+1,right)
        return result 
    else:
        return -1
    

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    result = []
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        result.append(binary_search(a,x,0,len(a)-1)) 
    print(*result)
