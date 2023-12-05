import sys
input=sys.stdin.readline


# 1 3 8 10 18 20 25
# ->
# 1~10   18~25
# ->K5로 두방컷남 ㅋㅋ
#
# 일단 정렬하고,
# 첫번째부터 끝반경까지 쏴보고, 두번째 생존부터 끝까지 쏴보고 해서 늘리면 되는데
# 이분탐색으로 K를 찾는 문제.
# start=1
# end는 당연히 가장 멀리있는 녀석의 인덱스/2+1임
#
# 늘리는 기준->끝까지 다 못죽였으면 탐색범위를 뒤로,
# 줄이는 기준->다죽였으면 최소에 저장하고 범위를 앞으로

N,K=map(int,input().split())
idxList=[]

for i in range(N):
    idxList.append(int(input()))

idxList.sort()

#이분탐색 돌리기, 이분탐색하는건 반경을 찾기 위함.
start=1
end=max(idxList)//2+1
answer=end

while start<=end:
    R=(start+end)//2
    #K번 쏘면서 애들 죽이기
    killed=[False for i in range(N)]
    tempKiled=0
    possible=False
    for i in range(K):
        #K번 쏘는데, 인덱스 배열에서 안죽은 애부터 죽이면서 넘어감
        killRange=idxList[tempKiled]+2*R
        for j in range(tempKiled,N):
            #만약 인덱스가 살상범위 안이면 죽인다.
            if idxList[j]<=killRange:
                killed[j]=True
                tempKiled+=1
            else: break
        #마지막까지 죽었으면 가능한거고 끝내면댄다.
        if killed[N-1]:
            possible=True
            break
    if possible:
        #가능하면 정답에 저장하고 범위를 줄여
        answer=min(answer,R)
        end=R-1
    else:
        #불가능하면 범위를 뒤로 보낸다
        start=R+1
print(answer)