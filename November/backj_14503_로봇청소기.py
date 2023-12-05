import sys

input = sys.stdin.readline

isStop = False
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
board = []
answer = 0

R, C = map(int, input().split())
robot = list(map(int, input().split()))

for i in range(R):
    board.append(list(map(int, input().split())))

def findNearPos(r, c):
    global R,C
    # 주변 4방향중에 0이 있다면 true
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0<=nr<R and 0<=nc<C) and board[nr][nc] == 0:
           return True
    return False


while not isStop:
    roR = robot[0]
    roC = robot[1]
    roD = robot[2]
    # 현재 칸이 청소 안된 경우,현재칸을 청소한다. 청소는 2로하자
    if board[roR][roC] == 0:
        answer += 1
        board[roR][roC] = 2
    # 현재 칸의 주변 4칸 중에 청소되지 않은 빈 칸이 있는 경우
    if findNearPos(roR, roC):
        #반시계 90도 회전
        roD -= 1
        if roD == -1: roD = 3
        robot[2] = roD
        #방향 기준 앞이 빈칸일 경우 전진
        if (0<=roR+dr[roD]<R and 0<=roC+dc[roD]<C) and board[roR+dr[roD]][roC+dc[roD]] == 0:
            robot[0]=roR+dr[roD]
            robot[1]=roC+dc[roD]
    else:
        #방향 한칸 뒤로 후진할 수 있으면
        revD=(roD+2)%4
        if (0<=roR+dr[revD]<R and 0<=roC+dc[revD]<C) and board[roR+dr[revD]][roC+dc[revD]] != 1:
            #한칸 후진하고 돌아가기
            robot[0] = roR + dr[revD]
            robot[1] = roC + dc[revD]
            continue
        else:
            isStop=True

print(answer)