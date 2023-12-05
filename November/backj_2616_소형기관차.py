import sys

input = sys.stdin.readline

# 간단한 누적합이면 될거같은데 왜 골3이지?


# 이거 다해서 최대 운송 손님 수를 측정하면 끝임.
# 누적합배열을 만들어놓고 풀이한다.
answer = 0

containerCnt = int(input())
containerList = list(map(int, input().split()))
trainCap = int(input())

sumList = [0] + containerList
for i in range(2, containerCnt + 1):
    sumList[i] += sumList[i - 1]
#zzz될리가없지
#백트로 풀면 시간초과, dp를 활용해보자
#기관차는 최대 3개 이므로 dp배열을 i번째 객차까지 j개의 기관차를 골랐을 때의
#최대로 고려한다.
dp=[[0 for j in range(4)] for i in range(containerCnt+1)]

#바텀업으로 갈건데 dp[i][j]의 값을 골라간다. dp[i][j]는 현재 객차까지
#기관차를 추가해서 담았을때와, 기관차를 추가하지 않고 안담았을때
#max(dp[i-trainCap][j-1]+(i-trainCap+1~현재까지의 누적합),dp[i-1][j])
for i in range(trainCap, containerCnt+1):
    for j in range(1,4):
        #트레인캡부터 1개씩 담아볼 수 있음
        dp[i][j]=max(dp[i-trainCap][j-1]+sumList[i]-sumList[i-trainCap],dp[i-1][j])



print(dp[containerCnt][3])
