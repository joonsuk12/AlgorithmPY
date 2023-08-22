import sys
input=sys.stdin.readline


# C개의 공유기를 설치, N개에서 C개를 설치해 가장 가까운 공유기 사이 거리가 가능한 크게
# 완탐식이면 N개에서 C개의 위치를 선택한 다음 최소 거리를 쭉 탐색하며 찾아야겠지만.
# x의 크기가 무려10억, 한번만 서치하는게 가능한 정도.
# 이게 이분탐색이다?
#양 끝단에 설치
#5개의 집
#3개를 어디에 설치할래?
#1 1 0 1 0 0 0 1 1
#1 0 0 1 1 0 0 1 1
#1 0 1 0 0 1 0 0 1
#1 0 0 0 0 0 0 0 1
#양 끝은 무조건인가?
#2개면 무조건 양 끝
#3개면 최대한 가운데#이분탐색하고,
#4개면 이런방식은 안되는데...
#음
#완탐으로 먼저 풀이



#입력부
answer=0
N,C=map(int,input().split())

houseList=[]
maxlen=0
for i in range(N):
    temp=int(input())
    maxlen=max(temp,maxlen)
    houseList.append(temp)
houseList.sort()


#함수부

#시간초과 해결 로직
#두 공유기 사이의 거리를 임의로 설정하고, 공유기를 놓을 수 있으면
#거리를 늘려보고, 없으면 거리를 줄여보는 방식으로, 구현하자
def BinarySet(start,end):
    global answer

    while start<=end:
        mid=(start+end)//2
        #mid를 최소거리로 해서 놓고 놓아지면 거리를 늘려보고
        if SetMap(mid)>= C:
            answer=max(mid,answer)
            start=mid+1
        #안놓아지면 거리를 줄이자.
        else:
            end=mid-1
    return
#해당 거리대로 공유기를 놓을 수 있는지 테스트해보기
def SetMap(mid):
    tempcount=1
    before=houseList[0]
    for i in range(1,N):
        if houseList[i]-before>=mid:
            tempcount+=1
            before=houseList[i]
    return tempcount

BinarySet(0,maxlen)
print(answer)