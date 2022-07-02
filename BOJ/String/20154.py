#20154 - 이 구역의 승자는 누구야?

alphab=[3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

string = input()
count = []
for a in string:
    count.append(alphab[ord(a)-ord('A')])


if (sum(count)%10)%2:
    print("I'm a winner!")
else:
    print("You're the winner?")