#반복문 이진 탐색

def iteration_bs(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if array[mid]==target:
      return mid
    elif array[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

index = iteration_bs(array, target, 0, n-1)
if index == None:
  print("원소가 존재하지 않습니다.")
else:
  print(index+1)