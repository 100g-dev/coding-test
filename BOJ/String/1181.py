#1181 - 단어 정렬

n = int(input())

words = []
for i in range(n):
    words.append(input())

words = list(set(words)) #중복제거
words.sort() #정렬
words.sort(key = len) #길이정렬

for word in words:
    print(word)