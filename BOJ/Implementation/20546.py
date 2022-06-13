#20546 - 기적의 매매법

#준현이는 살 수 있으면 무조건 구매

#성민
# 1. 모든 거래는 전량 매수와 매도
# 2. 3일 연속 가격이 전일 대비 상승하는 주식은 다음나 무조건 가격이 하락 -> 전량 매도
# 3. 3일 연속 증가 후 하락한 주식은 다음날 무조건 상승, 전량 매수


def bnp(money, stocks):
    result = 0
    for stock in stocks:
        count = money // stock
        money -= (count*stock)
        result += count

    return money+result*stocks[-1]

def timing(money, stocks):
    result = 0
    
    for i in range(3,len(stocks)):
        if stocks[i-3] < stocks[i-2] < stocks[i-1] < stocks[i]:
            #전량매도
            money += stocks[i] * result
            result=0       

        elif stocks[i-3] > stocks[i-2] > stocks[i-1] > stocks[i]:
            #전량매수
            count = money//stocks[i]
            money -= count*stocks[i]
            result += count
    
    return money+result*stocks[-1]


n = int(input())
stocks = list(map(int,input().split()))

jun = bnp(n, stocks)
sung = timing(n, stocks)


if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")


