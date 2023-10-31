import sys
input=sys.stdin.readline

N_out=int(input())
S_out=list(map(int,input().split()))
flag=False

#원소의 개수가 최대 20개이므로 powerSet으로 문제를 풀이해보자.
def solution(N,S):
    global flag
    check_num=min(S)
    #숫자중 가장 작은수를 찾음, 해당 수보다 작은 수가 있으면 해당 수가 부분 수열의 합으로 나올 수 없는 가장 작은수
    if min(S)>1:
        print(1)
        exit(0)

    #숫자의 전체합-1까지 확인하기
    #근데 정렬해서 다음 합으로 가는게 나을듯?
    #20개에서 몇개 뽑아서 만든 수를 정렬해서 차가 1 이상 나면 이전수+1을 반환하게끔할걸
    temp_S=S[:]
    temp_S=sorted(temp_S)
    while check_num<=sum(S):
        flag=False
        testNum(check_num,N,S)
        if flag:
            check_num += 1
            continue
        else :
            print(check_num)
            exit(0)
    if flag:
        print(sum(S)+1)
    return

#nC1~nCn까지 테스트해보게끔 하는게 더 의미있겠다.

def testNum(num,end,num_list):
    global flag

    def Combination(temp,goal,visit,cnt,end_cnt,nums):
        global flag
        if flag:
            return
        #목표한 goal에 도달했으면 함수 종료
        if temp==goal:
            flag=True
            return
        #end_cnt에 도달했으면 함수 종료
        if cnt==end_cnt:
            return
        #목표한 숫자를 넘겼어도 함수 종료
        if temp>goal:
            return
        #반복문 돌면서 아직 안고른 애들 중 하나 고르고 방문처리하고 다음으로 넘어가야 함
        for idx in range(cnt,end_cnt):
            if visit[idx]: continue
            visit[idx]=True
            Combination(temp+nums[idx],goal,visit,cnt+1,end_cnt,nums)
            visit[idx]=False

    # nC1~nCn까지 해보면서 목표한 num을 만들 수 있으면 true, 끝까지 없으면 false 반환
    for i in range(1,end):
        if flag: return
        visited = [False for r in range(end)]
        Combination(0,num,visited,0,end,num_list)

solution(N_out,S_out)