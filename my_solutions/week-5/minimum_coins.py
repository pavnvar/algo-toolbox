# Uses python3
import sys
coin_denominations = [1,3,4]
def get_change(m):
    minimum_coins = float('inf')
    if m == 0:
        return 0
    if minimum_change_array[m] != float('inf'):
        return minimum_change_array[m]
    for coin in coin_denominations:
        if m-coin >= 0:
            number_of_coins = get_change(m-coin)
            if number_of_coins+1 < minimum_coins:
                minimum_coins = number_of_coins + 1
    minimum_change_array[m] = minimum_coins
    return minimum_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    minimum_change_array  = [float('inf') for i in range(m+1)]
    minimum_change_array[0] = 0
    print(get_change(m))