import sys
input=sys.stdin.readline

N,K=map(int,input().split())
days=list(map(int,input().split()))
final_up=max(days)
lowest_price=K

#시간초과 로직
def checkPos(X):
    global lowest_price
    temp_sum=0
    temp_price=0
    idx=0
    #마지막 가격상승이후 코인이 0이 될때까지 -> 마지막 상승일+X일까지 계산하면댐
    for day in range(1,final_up+X):
        #오르는날이면 가격올리기
        if day==days[idx]:
            temp_price=X
            if idx<len(days)-1:
                idx+=1
        #안오르는 날이면 0이면 그대로 두고 0보다 크면 1씩 떨어뜨리기
        else:
            if temp_price>0:
                temp_price-=1
        #현재가 곱하기 1을 temp_sum에 더해준다.
        temp_sum+=temp_price*1
        #넘었으면 즉시 종료
        if temp_sum >= K:
            lowest_price = min(lowest_price, X)
            return True
    return False

#시간초과 안나는 로직
def checkPos2(X):
    global lowest_price
    total_price = 0
    for i in range(N):
        if i==N-1:
            for j in range(X,0,-1):
                total_price+=j
        # X일 동안 가격을 X로 올린 후, 가격을 1씩 줄임
        #다음날까지의 거리를 비교해 X이상 차이나면 1까지 내려서 더함
        #X이상 차이 안나면 해당 거리까지 합
        elif days[i+1]-days[i]>=X:
            for j in range(X, 0, -1):
                total_price += j
        else:
            for j in range(X,X-(days[i+1]-days[i]),-1):
                total_price += j
        if total_price >= K:
            lowest_price=min(lowest_price,X)
            return True
    return False
#이분탐색으로 풀 수 있을듯?
low=1
high=K
while low<=high:
    mid=(high+low)//2
    if checkPos2(mid):
        #가능하면 수를 줄여봐야지
        high=mid-1
    else:
        #불가능하면 수를 늘려봐야함
        low=mid+1

print(lowest_price)
