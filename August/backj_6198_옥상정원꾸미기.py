import sys
input=sys.stdin.readline

'''
10억... 반복문 한번 돌면 끝이여

'''
#선언

#입
N=int(input())
buildings=[]
for i in range(N):
    buildings.append(int(input()))
#함
def solution():
    answer=0
    stack=[]
    for i in range(0,len(buildings)):
        temp=buildings[i]
        #스택의 뒤부터 돌면서 나보다 작은놈들은 팝해주면서 답을 늘려주기,
        while len(stack)!=0:
            #나보다 크거나 같은 놈이 나오기전까지 스택을 팝하다 나보다 큰놈만나면 그 전에 들어가기
            if stack[-1]<=temp:
                stack.pop()
                continue
            #나보다 크면 냅다 스택에 집어넣기
            stack.append(temp)
            break
        if len(stack)==0:
            stack.append(temp)
            continue
        answer+=len(stack)-1
    #마지막에 남는 스택의 헤드를 빼고 갯수세서 답에 더하기
    return answer


#출
print(solution())
