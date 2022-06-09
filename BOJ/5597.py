#5597 - 과제 안 내신분?

student = [i for i in range(1, 31)]

for _ in range(28):
    report = int(input())
    student.remove(report)

print(min(student))
print(max(student))