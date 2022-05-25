#성적 출력

n = int(input())

array = []
for i in range(n):
  student_info = input().split()
  array.append((student_info[0], int(student_info[1])))

array = sorted(array, key=lambda student:student[1])
for student in array:
  print(student[0], end=' ')