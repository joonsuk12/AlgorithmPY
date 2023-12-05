import sys

input = sys.stdin.readline

# 1 - 1
# 2 - 2,1+1  3 - 2+1, 1+1+1, 1+2, 3
# 4 - 2+2,1+3,1+1+1+1,2+1+1

# 바로 직전거(다 1 더해서 만들 수 있음)
# 2개 전꺼(다 2 더해서 만들 수 있음)
# 3개 전꺼(다 3 더해서 만들 수 있음)

# 현재꺼를 만드려면 이전꺼 세개 더하면 댐
# 바텀업
T = int(input())
getNum = []
answer = []
for i in range(T):
    getNum.append(int(input()))

dp = [0 for i in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
maxNum=max(getNum)


#초기 연산은 한번만 진행하기
for j in range(4, maxNum + 1):
    dp[j] = (dp[j - 1] + dp[j - 2] + dp[j - 3])%1000000009


for i in range(T):
    print(dp[getNum[i]])
