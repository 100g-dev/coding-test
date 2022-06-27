#14719 - 빗물

h, w = map(int, input().split())
wall = list(map(int, input().split()))

left = 0
right = w-1
max_left = wall[left]
max_right = wall[right]

result = 0

while left< right:
    max_left = max(max_left, wall[left])
    max_right = max(max_right, wall[right])

    if max_left>= max_right:
        result += max_right - wall[right]
        right -= 1
    if max_left < max_right:
        result += max_left - wall[left]
        left += 1


print(result)