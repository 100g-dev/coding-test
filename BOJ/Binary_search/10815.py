#10815 - 숫자 카드

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
targets = list(map(int, input().split()))

def binary_search(array, target):
    start = 0
    end = len((array))-1

    while start<=end:
        mid = (start+end)//2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for t in targets:
    if binary_search(card, t) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')