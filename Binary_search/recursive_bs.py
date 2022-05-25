#재귀함수 이진 탐색

def recursive_bs(array, target, start, end):
  if start > end:
    return None
  mid = (start+end)//2

  if array[mid]==target:
    return mid
  elif array[mid] > target:
    return recursive_bs(array, target, start, mid-1)
  else:
    return recursive_bs(array, target, mid+1, end)


n, target = map(int, input().split())
array = list(map(int, input().split()))

index = recursive_bs(array, target, 0, n-1)
if index == None:
  print("원소가 존재하지 않습니다.")
else:
  print(index+1)