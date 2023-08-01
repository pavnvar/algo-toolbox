'''
    Majority element : element that occurs more than n/2 times, in a list of size = n
'''
import sys

def get_frequency(a,left,right,query) -> int:
    count = 0
    for i in range(left,right+1):
        if a[i] == query:
            count = count + 1
    return count

def get_most_occuring_element(a, left, right) -> int:
    '''
        Finds element that occurs the most using, divide and conquer strategy    
    '''
    if left == right:
        return a[left]
    mid = (left + right)//2
    left_majority = get_most_occuring_element(a,left,mid)
    right_majority = get_most_occuring_element(a,mid+1,right)
    left_majority_frequency = get_frequency(a,left,right,left_majority)
    right_majority_frequency = get_frequency(a,left,right,right_majority)
    if left_majority_frequency > right_majority_frequency:
        return left_majority
    else:
        return right_majority

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    most_occuring_element = get_most_occuring_element(a,0,n-1)
    if get_frequency(a,0,n-1,most_occuring_element) > len(a)/2 :
        print(1)
    else:
        print(0)