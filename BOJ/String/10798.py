#10798 - 세로읽기

magnet =[[0]*15 for i in range(5)]


for i in range(5):
    data = input()
    magnet[i][:len(data)] = data

result=''
for i in range(15):
    for j in range(5):
        
        if magnet[j][i]==0:
            continue
        else:
            result+=magnet[j][i]
print(result)