from functools import cmp_to_key
def comparativeFunc(x, y):
    if( int(str(x) + str(y)) >= int(str(y) + str(x))):
        return 1
    else:
        return -1
inputQty = int(input())
inputList = list(map(int,input().split()))
sortedInputList = sorted(inputList, key=cmp_to_key( comparativeFunc ))
sortedInputList = [str(i) for i in sortedInputList ]
sortedInputList.reverse()
c = "".join(sortedInputList)
print(c)