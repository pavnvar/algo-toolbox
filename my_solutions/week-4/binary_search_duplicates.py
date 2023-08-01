def binary_search(keys, query):
    left , right = 0, len(keys)-1
    if right >= left:
        mid = (left + right)//2
        if keys[mid] == query:
            index = binary_search(keys[left:mid],query)
            if index != -1:
                return index
            return mid

        elif keys[mid] < query:
            index = binary_search(keys[mid+1:right+1],query)
            if index != -1:
                return mid + 1 + index
            return -1
        elif keys[mid] > query:
            return binary_search(keys[left:mid],query)
    else:
        return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')