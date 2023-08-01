
def merge_arrays(a,b,left,right,ave):
    number_of_inversions = 0
    first_array = a[left:ave]
    second_array = a[ave:right]
    first_index = second_index =  0
    new_array_index = left
    while first_index < len(first_array) and second_index < len(second_array):
        if first_array[first_index] > second_array[second_index]:
            a[new_array_index] = second_array[second_index]
            second_index += 1
            #number of inversions = number of elements in sorted first subarray which is less that the current element of sorted second array 
            number_of_inversions = number_of_inversions + len(first_array[first_index:])
        else:
            a[new_array_index] = first_array[first_index]
            first_index += 1
        new_array_index += 1

    while first_index < len(first_array):
        a[new_array_index] = first_array[first_index]
        new_array_index += 1
        first_index += 1
        
    while second_index < len(second_array):
        a[new_array_index] = second_array[second_index]
        new_array_index += 1
        second_index += 1
    return number_of_inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge_arrays(a,b,left,right,ave)
    return number_of_inversions

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))