#17276 - 배열 돌리기

def turn(n, d, graph):
    count = abs(d)//45
    minus = False if d>=0 else True

    for _ in range(count):
        result = [item[:] for item in graph]

        if minus: #반시계
           for i in range(n):
            result[n//2][i] = graph[i][i]

            for i in range(n):
                result[n-i-1][i] = graph[n//2][i]

            for i in range(n):
                result[i][n//2] = graph[i][n-i-1]
            
            for i in range(n):
                result[i][i] = graph[i][n//2]

        else: #시계
            for i in range(n): #주대각선->열
                result[i][n//2] = graph[i][i]

            for i in range(n): #열->부대각선
                result[i][n-i-1] = graph[i][n//2]

            for i in range(n): #부대각선->행
                result[n//2][n-i-1] = graph[i][n-i-1]
            
            for i in range(n): #행->주대각선
                result[i][i] = graph[n//2][i]

        graph = [item[:] for item in result]

t= int(input())
for _ in range(t):
    n, d = map(int, input().split())
    graph= [list(map(int, input().split())) for _ in range(n)]
    turn(n, d, graph)

    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()
