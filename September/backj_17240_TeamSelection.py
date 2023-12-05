import sys
input=sys.stdin.readline

'''
다섯 역할, n명의 사람의 5개의 스텟,
역할군의 실력 합이 최대가 되게 팀을 짜라
n이 2만이므로 순열로 푸는건 불가능
딱 떠오르는건 2만을 가로로 쭈욱 늘려서
a로 정렬해서 최대를 뽑고
b로 정렬해서 최대를 뽑고
c로
백트로 풀이하는 그림도 있겠-아니다
현재 속성으로 정렬해서 최대인 애들을 찾아서 개수만큼 분기하기

백트 조건->최소의



이건가?

매 분기마다 최선의 선택을 하면서 가는데 이후에 최선의 선택과 겹친다면? 백트랰
최선의 선택하고 그다음부터는 순차적으로 가져감.->?

'''

#입력
max_list=[0,0,0,0,0]
answer=0
N=int(input())
selected=[False for i in range(N)]
range_dict=dict()
range_dict={0:'a',1:'b',2:'c',3:'d',4:'e'}
all_point_list=[]

a=[0 for i in range(N)]; b=[0 for i in range(N)];
c=[0 for i in range(N)]; d=[0 for i in range(N)]; e=[0 for i in range(N)]

#200000000
#인덱스의 위치 이후로 최대
max_list[4]=max(e)
max_list[3]=max(d)+max(e)
max_list[2]=max(e)+max(d)+max(c)
max_list[1]=max(e)+max(d)+max(c)+max(b)
max_list[0]=max(a)+max(e)+max(d)+max(c)+max(b)

for i in range(N):
    ta,tb,tc,td,te=map(int,input().split())
    a[i]=ta; b[i]=tb; c[i]=tc; d[i]=td; e[i]=te
#함수
all_point_list.append(a)
#뽑히지 않은 애들 중에서 최대를 뽑고 넘어가보는 함수.
#근데 이거 디피아님? 오 배열이 터질듯...
def pick(cnt, i):

    pass


def pick_player(cnt, temp_sum):
    global answer
    #기저조건
    if cnt==5:
        answer=max(answer,temp_sum)
        return
    #백트조건, 현재 임시합에 뒤에서의 최선의 결과(!)를 더해도 정답보다 작으면 가지치기
    if temp_sum+max_list[cnt]<answer:
        return
    #실행문, 현재선택에서 항상 최선의 선택을 먼저 해보고 이동하자.
    for i in range(N):
        if selected[i]: continue
        #선택 안 된 애들 중에서 가장 큰 녀석을 골라보고
        selected[i]=True
        pick_player(cnt+1,temp_sum+pick(cnt,i))
        selected[i]=False
    return

#실
pick_player(0,0)
print(answer)
