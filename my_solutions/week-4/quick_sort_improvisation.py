# Uses python3
''''
quicksort with 3 partitioins
1)element = pivot
2)element < pivot
3)element > pivot
'''
import sys
import random

def partition3(a, l, r):
    pivot_element = a[l]
    pivot_element_index_start = l
    pivot_element_index_end = l
    last_lesser_element = l
    for element in range(pivot_element_index_start+1, r+1):
        if a[element] == pivot_element:
            pivot_element_index_end += 1
            last_lesser_element += 1
            a.insert(pivot_element_index_end, a[element])
            del a[element+1]
        elif a[element] < pivot_element:
            last_lesser_element += 1
            a[last_lesser_element], a[element] = a[element], a[last_lesser_element]
            
    for element in range(pivot_element_index_end+1, last_lesser_element+1):
        a[pivot_element_index_start], a[element] = a[element], a[pivot_element_index_start]
        pivot_element_index_start += 1
        pivot_element_index_end += 1
    return pivot_element_index_start, pivot_element_index_end


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
