'''
Faster than previous implementation as we are sending pre sorted array rather than sorting it at every recurrance 
T(n) = 2T(n/2) + O(n)
=> T(n) = O(nlogn)

'''


import math
import sys

def get_distance(point1:tuple, point2:tuple) -> int :
    #returns distance between two points
    return( point2[1] - point1[1])**2 + (point2[0] - point1[0])**2  


def get_minimum_distance(point_list_x_sorted, point_list_y_sorted) -> int :
    if len(point_list_x_sorted) == 2:
        return get_distance(point_list_x_sorted[0],point_list_x_sorted[1])
    if len(point_list_x_sorted) <= 1:
        #return big number
        return float('inf')
    n = len(point_list_x_sorted)
    mid = n // 2
    left_array_y_sorted = []
    right_array_y_sorted = []
    mid_point_encountered = False
    for point in point_list_y_sorted:
        if (point[0] < point_list_x_sorted[mid][0]) or ( (point[0] == point_list_x_sorted[mid][0]) and (point[1] < point_list_x_sorted[mid][1]) ):
            left_array_y_sorted.append(point)
        elif (point[0] > point_list_x_sorted[mid][0]) or ( (point[0] == point_list_x_sorted[mid][0]) and (point[1] >= point_list_x_sorted[mid][1]) ):
            if (point[0] == point_list_x_sorted[mid][0]) and (point[1] == point_list_x_sorted[mid][1]):
                if mid_point_encountered:
                    #already same middle point exists, hence coinciding hence distance is zero
                    return 0
                else:
                    mid_point_encountered = True
            right_array_y_sorted.append(point)

    left_partition_minimum_distance = get_minimum_distance(point_list_x_sorted[:mid], left_array_y_sorted)
    right_partition_minimum_distance = get_minimum_distance(point_list_x_sorted[mid:], right_array_y_sorted)
    minimum_distance = min(left_partition_minimum_distance, right_partition_minimum_distance)
    '''
    WE FOUND THE MINIMUM DISTANCE WITHIN EACH PARTITION,
    NOW WE NEED TO CHECK THERE EXISTS TWO POINTS FROM DIFFERENT 
    PARTITIONS WHOSE DISTANCE IS LESS THAN MINIMUM DISTANCE
    '''
    #filtered_points_y_sorted = list(filter( lambda point : abs(point[0]-point_list_x_sorted[mid][0]) < minimum_distance, point_list_y_sorted ))
    
    filtered_points_y_sorted = [point for point in point_list_y_sorted if abs(point[0]-point_list_x_sorted[mid][0]) < minimum_distance]
    len_point_list_y_sorted = len(filtered_points_y_sorted)
    for index, point in enumerate(filtered_points_y_sorted):
        '''
            interesting geometric result that we need only 7 iterations,
            find the proof here: https://www.youtube.com/watch?v=kCLGVat2SHk&t=1313s, 
            https://www.youtube.com/watch?v=frir6Sf7ft4&t=1111s,
            hence the outer loop is O(n)
        '''
        max_last_index_iter = min(index+7, len_point_list_y_sorted-1)
        for i in range(index+1, max_last_index_iter+1):
            distance = get_distance(point, filtered_points_y_sorted[i])
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance 

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    point_list = list(zip(x, y))       
    if len(point_list) == 1:
        print(0)
    else:
        #sort by x axis
        point_list_x_sorted = sorted(point_list, key = lambda point : (point[0], point[1]))
        point_list_y_sorted = sorted(point_list, key = lambda point : point[1])
        print(math.sqrt(get_minimum_distance(point_list_x_sorted = point_list_x_sorted, point_list_y_sorted = point_list_y_sorted)))