'''
T(n) = 2T(n/2) + O(nlogn)
=>T(n) = O(nlogn*logn)


SOME ADDITTIONAL POINTS FOR FASTER EXEC:
1)List Comprehension over filter
2)use zip over iterating over each input
3)IMP: rather than finding square root in distance every time, 
we find the squared distance and only find the square root while printing result(saved 4 seconds)
'''


from cgi import test
import math
import sys

def get_distance(point1:tuple, point2:tuple) -> int :
    #returns distance between two points
    return( round(math.sqrt( (point2[1] - point1[1])**2 + (point2[0] - point1[0])**2 ),4) )


def get_minimum_distance(point_list) -> int :
    if len(point_list) == 2:
        return get_distance(point_list[0],point_list[1])
    if len(point_list) <= 1:
        #return big number
        return 300000000000
    n = len(point_list)
    mid = n // 2
    left_partition_minimum_distance = get_minimum_distance(point_list[:mid])
    right_partition_minimum_distance = get_minimum_distance(point_list[mid:])
    minimum_distance = min(left_partition_minimum_distance, right_partition_minimum_distance)
    '''
    WE FOUND THE MINIMUM DISTANCE WITHIN EACH PARTITION,
    NOW WE NEED TO CHECK THERE EXISTS TWO POINTS FROM DIFFERENT 
    PARTITIONS WHOSE DISTANCE IS LESS THAN MINIMUM DISTANCE
    '''
    #filter points whose x-distance from the mid line is less than ,minimum distance
    #filtered_points_list = filter( lambda point : abs(point[0]-point_list[mid][0]) < minimum_distance, point_list )    
    filtered_points_list = [point for point in point_list if abs(point[0]-point_list[mid][0]) < minimum_distance]
    #sort as per y axis
    point_list_y_sorted = sorted(filtered_points_list, key = lambda point : point[1])
    len_point_list_y_sorted = len(point_list_y_sorted)
    for index, point in enumerate(point_list_y_sorted):
        '''
            interesting geometric result that we need only 7 iterations,
            find the proof here: https://www.youtube.com/watch?v=kCLGVat2SHk&t=1313s, 
            https://www.youtube.com/watch?v=frir6Sf7ft4&t=1111s,
            hence the outer loop is O(n)
        '''
        max_last_index_iter = min(index+7, len_point_list_y_sorted-1)
        for i in range(index+1, max_last_index_iter+1):
            distance = get_distance(point, point_list_y_sorted[i])
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance 

if __name__ == "__main__":
    
    
    # point_list = [] 
    # number_of_points = int(input())
    # for i in range(0,number_of_points):
    #     point = tuple(map(int,input().split()))
    #     point_list.append(point)
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
        point_list.sort(key = lambda point : point[0])
        print(get_minimum_distance(point_list = point_list))
    