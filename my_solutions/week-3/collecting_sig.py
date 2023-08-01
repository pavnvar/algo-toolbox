def get_input():
    number_segments = int(input())
    segments_list = []
    for x in range(number_segments ):
        input_list =  list(map(int, input().split()))
        segments_list.append(input_list)
    return(segments_list)
    
def get_minimal_segments(segments_list):
    points = []
    current_segment_end = segments_list[0][-1]
    points.append(current_segment_end)
    for segment in segments_list:
        if(current_segment_end < segment[0]):
            current_segment_end = segment[-1]
            points.append(current_segment_end)
    return points
def display_ouput(minimal_segment_list):
    print(len(minimal_segment_list))
    minimal_segment_list.sort()
    print(*minimal_segment_list)
segments_list = get_input()
segments_list.sort(key = lambda segment : segment[-1])
points = get_minimal_segments(segments_list)
display_ouput(points)


