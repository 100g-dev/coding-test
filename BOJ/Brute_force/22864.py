#22864 - 피로도

a, b, c, m = map(int, input().split())

time = 0
work = 0
tired = 0

if a > m:
    print(0)
else:
    while time != 24:
        time += 1
        if tired + a <= m:
            work += b
            tired += a
        else:
            tired -= c
            if tired < 0:
                tired=0

    print(work)