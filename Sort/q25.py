#q25 - 실패율
#programmers 42889

n= 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

stages.sort()
result = {}
for i in range(n):
    result[i+1] = 0

index = 0
while index < len(stages):
    if stages[index] > n:
        break
    count = 1
    for j in stages[index+1:]:
        if stages[index] == j:
            count+=1
        else:
            break
    
    result[stages[index]] = (count)/(len(stages)-index)
    index += count

print(sorted(result, key=lambda x: -result[x]))
