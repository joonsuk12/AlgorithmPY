import sys, copy
input=sys.stdin.readline


'''
그냥 구현이네
1번이면 상하좌우
2번이면 좌우, 상하
3번이면 상우, 우하, 하좌, 좌상
4번이면 상빼고, 하빼고, 좌빼고, 우빼고
5번이면 4방향 전부 보내기
'''
dr1=[-1,1,0,0]
dc1=[0,0,-1,1]
dr2=[0,0,-1,1]
dc2=[-1,1,0,0]
dr3=[[-1,0],[0,1],[1,0],[0,-1]]
dc3=[[0,1],[1,0],[0,-1],[-1,0]]
#4,5는 필요없을듯


#입력부
N,M=map(int,input().split())
cctv_list=[]
board=[]
answer=M*N+10
for i in range(N):
    templist=list(map(int,input().split()))
    for j in range(M):
        temp=templist[j]
        if temp!= 0 and temp!=6:
            cctv_list.append([i,j])
    board.append(templist)
#함수부




def countEmpty(temp_board):
    temp_count=0
    for i in temp_board:
        for j in i:
            if j==0:
                temp_count+=1
    return temp_count

def reachArm1(index,temp_board, dir):
    nr=index[0]
    nc=index[1]
    while 1:
        nr += dr1[dir]
        nc += dc1[dir]
        # 범위를 벗어나면 브레이크
        if not (0 <= nr < N and 0 <= nc < M and temp_board[nr][nc] != 6):
            break
        if temp_board[nr][nc]==0:
            temp_board[nr][nc]='#'
    return temp_board


def reachArm2(index, temp_board, dir):
    #0이면 상하, 1이면 좌우
    if dir==0:
        for i in range(0,2):
            temp_board=reachArm1(index,temp_board,i)
    else:
        for i in range(2,4):
            temp_board = reachArm1(index, temp_board, i)
    return temp_board


def reachArm3(index, temp_board, dir):
    #0이면 상좌, 1 좌하, 2 하우, 3 우상
    if dir == 0:
        temp_board = reachArm1(index, temp_board, 0)
        temp_board = reachArm1(index, temp_board, 2)
    elif dir==1:
        temp_board = reachArm1(index, temp_board, 2)
        temp_board = reachArm1(index, temp_board, 1)
    elif dir==2:
        temp_board = reachArm1(index, temp_board, 1)
        temp_board = reachArm1(index, temp_board, 3)
    else:
        temp_board = reachArm1(index, temp_board, 3)
        temp_board = reachArm1(index, temp_board, 0)
    return temp_board


def reachArm4(index, temp_board, dir):
    if dir == 0:
        temp_board = reachArm1(index, temp_board, 0)
        temp_board = reachArm1(index, temp_board, 2)
        temp_board = reachArm1(index, temp_board, 1)
    elif dir == 1:
        temp_board = reachArm1(index, temp_board, 2)
        temp_board = reachArm1(index, temp_board, 1)
        temp_board = reachArm1(index, temp_board, 3)
    elif dir == 2:
        temp_board = reachArm1(index, temp_board, 1)
        temp_board = reachArm1(index, temp_board, 3)
        temp_board = reachArm1(index, temp_board, 0)
    else:
        temp_board = reachArm1(index, temp_board, 3)
        temp_board = reachArm1(index, temp_board, 0)
        temp_board = reachArm1(index, temp_board, 2)
    return temp_board


def reachArm5(index, temp_board):
    for i in range(4):
        temp_board=reachArm1(index, temp_board, i)
    return temp_board


def dfs(count, temp_board):
    global answer
    #기저조건
    if count==len(cctv_list):
        tempans=countEmpty(temp_board)
        if answer>tempans:
            answer=tempans
        return
    #각각의 경로에 맞게 dfs를 보냄
    # print(count)
    cctv_type=temp_board[cctv_list[count][0]][cctv_list[count][1]]
    # print(cctv_type)

    backup=copy.deepcopy(temp_board)
    if cctv_type==1:
        for i in range(4):
            dfs(count+1,reachArm1(cctv_list[count],temp_board,i))
            temp_board=copy.deepcopy(backup)
    elif cctv_type==2:
        for i in range(2):
            dfs(count+1,reachArm2(cctv_list[count],temp_board,i))
            temp_board = copy.deepcopy(backup)
    elif cctv_type==3:
        for i in range(4):
            dfs(count+1,reachArm3(cctv_list[count],temp_board,i))
            temp_board = copy.deepcopy(backup)
    elif cctv_type==4:
        for i in range(4):
            dfs(count+1,reachArm4(cctv_list[count],temp_board,i))
            temp_board = copy.deepcopy(backup)
    else:
        dfs(count+1, reachArm5(cctv_list[count],temp_board))

def solution():
    global answer
    #cctv리스트에 대해서 완탐을 돌릴것, 지나쳐도 되니까 순서도 상관없음
    # print(cctv_list)
    dfs(0,board)
    print(answer)
    return answer
#실행
solution()