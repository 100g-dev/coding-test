#19637 - IF문 좀 대신 써줘
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

skill={}
for i in range(n):
    name, level = input().split()
    level=int(level)
    
    if level not in skill.keys():
        skill[level]=name

level_list = sorted(skill.keys())


for j in range(m):
    power = int(input())
    start = 0
    end = len(level_list)
    result=''

    while start<=end:
        mid = (start+end)//2
        
        if power<=level_list[mid]:
            result = level_list[mid]
            end = mid -1
        else:
            start = mid + 1

    print(skill[result])
        

