import sys
input=sys.stdin.readline

'''
N개의 집, 앞뒤로 다른 색으로 칠해야댐
완탐식 접근->3개중에 하나고르고 이전거랑 다른거 두개를 나누기
일단 백트로 먼저 구현해보는거야~
'''

#입력
N=int(input())
RGBlist=[[0 for _ in range(3)]for _ in range(N)]
for i in range(N):
    red,green,blue=map(int,input().split())
    RGBlist[i][0]=red
    RGBlist[i][1]=green
    RGBlist[i][2]=blue
#메서드 구현
#입력확인메서드
def inputTest():
    for i in RGBlist:
        print(i)
#백트래킹함수, 이전과 겹치지 않게 하나를 골라 끝까지 다 고르면, 최소 비용과 비교하기
answer=2000000
#메모제이션은 cnt랑 before를 활용해 weight를 담도록 하자
dplist=[[0 for _ in range(3)]for _ in range(N)]
def track(cnt,before,weight):
    global answer
    #기저조건
    if cnt==N:
        answer=min(answer,weight)
        return
    #가지치기 조건, weight가 answer를 넘어선다면 가지치기하기
    if weight>answer:
        return
    #구현부
    #이전과 겹치지 않게 하나를 고르는 것을 구현하는 방법, 1. 이전의 선택을 인자로 가지고 다니기
    #2. 셀렉티드 배열을 가지고 다니기, 1번 아이디어가 좋아보임
    #before->0,1,2,3으로 하고 before랑 같은건 함수 보내지 말고
    for i in range(1,4):
        if before==i:
            continue
        #해당 색을 선택하고, 선택한 애의 코스트를 나눠준다.
        track(cnt+1,i,weight+RGBlist[cnt][i-1])


#dp배열에는 현재 색을 집으로 선택할때의 최소 가중치를 저장한다고 생각하자.
#dp함수
def dptrack(cnt,now):
    global answer
    #기저조건, 0을 반환하는걸로 바꾸기
    if cnt==N:
        return 0
    # #가지치기 조건, weight가 answer를 넘어선다면 가지치기하기
    # if weight>answer:
    #     return
    #찾으려는 값이 저장되어 있다면 해당 값을 출력하게
    if dplist[cnt][now]!=0:
        return dplist[cnt][now]
    #구현부
    #dplist의 각각의 값에 이전에서의 최소값을 넣고
    for i in range(3):
        if now==i:
            continue
        #해당 색을 선택하고, 선택한 애의 코스트를 나눠준다.
        if dplist[cnt][now]==0:
            dplist[cnt][now]=dptrack(cnt-1,i)+RGBlist[cnt][now]
            continue
        dplist[cnt][now]=min(dplist[cnt][now],dplist[cnt-1][i-1])
    return dplist[cnt][now]


#실행
# track(0,0,0)

dptrack(0,3)
print(answer)

# inputTest()