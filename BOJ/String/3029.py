#3029 - 경고

from termios import TAB0


h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int ,input().split(":"))

time1 = h1*60*60 + m1*60 + s1
time2 = h2*60*60 + m2*60 + s2

time = time2-time1 if time2>time1 else time2-time1+24*60*60

h = time//60//60
m = time//60 %60
s = time%60

print("%02d:%02d:%02d" %(h, m, s))