
def fast_count_segments(segment_list, points) -> list:
    '''
    STEPS:
    1) Label Each point as "START", "END", "POINT"
    2) Sort them in a number line as per point value, \
       if point values are same order of prefarance should be as follows "START","POINT","END"
       so that equal points are treated inside the segment line
    3) After sorting count occurance of each point in segments(a bit tricky, check code for counting logic)
    '''
    
    START_LABEL = 1
    END_LABEL = 3
    POINT_LABEL = 2
    frequency_count = [0]*len(points)
    start_list = list(map(lambda x : (x[0], START_LABEL), segment_list))
    end_list = list(map(lambda x: (x[1],END_LABEL), segment_list))
    point_list = list(map(lambda x: (x,POINT_LABEL), points))
    points_map = dict()
    #lets have a hash map between each point and its index 
    #as we dont want to do a linear search always while calculating frequency
    for index, point in enumerate(points):
        if point not in points_map:
            points_map[point] = list()
        points_map[point].append(index)
    combined_point_list = [*start_list,*end_list,*point_list]
    combined_point_list = sorted(combined_point_list, key = lambda x : (x[0],x[1]))
    count = 0
    for combined_point in combined_point_list:
        if combined_point[1] == START_LABEL:
            count = count + 1 
        elif combined_point[1] == POINT_LABEL:
            indexes = points_map[combined_point[0]]
            for index in indexes:
                frequency_count[index] = count
        else:
            count = count - 1
    
    
    return frequency_count

if __name__ == '__main__':
    number_of_segments, number_of_points = list(map(int, input().split()))
    segment_list = list()
    for i in range(0,number_of_segments):
        segment = tuple(map(int,input().split()))
        segment_list.append(segment)
    points = list(map(int,input().split()))
    point_inclusion_frequency_list = fast_count_segments(segment_list, points)
    for occurance in point_inclusion_frequency_list:
        print(occurance, end=' ')