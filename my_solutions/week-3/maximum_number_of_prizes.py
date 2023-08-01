def get_maximum_prizes(prizesNumber):
    totalSum = 0
    count = 0
    numberList = []
    for number in range(1,prizesNumber+1):
        if( prizesNumber >= totalSum + number):
            count += 1
            numberList.append(number)
            totalSum += number
        else:
            numberList[-1] += (prizesNumber - totalSum)
            break
    return (count, numberList) 


prizesNumber = int(input())
(count , numberList) = get_maximum_prizes(prizesNumber)
print(count)
print(*numberList)
