import sys

input = sys.stdin.readline

N = int(input())
devList = []
for i in range(N):
    devList.append(list(map(int, input().split())))

# 삼각형을 계속 이어서 더해간다.
start = devList[0]
answer = 0
for i in range(1, N-1):
    # 삼각형을 이루는 세 좌표: start, 현재 점, 다음 점
    now = devList[i]
    next_point = devList[i+1]

    # 세 좌표를 알 때 삼각형의 넓이를 구하는 공식
    temp = (start[0]*now[1] + now[0]*next_point[1] + next_point[0]*start[1] -
            now[0]*start[1] - next_point[0]*now[1] - start[0]*next_point[1]) / 2.0

    answer += temp

# 소수점 아래 둘째자리에서 반올림하는 방법
answer = abs(answer)
print(round(answer, 2))