import sys
input=sys.stdin.readline

'''
완탐 생각->80개의 길이->80개의 구간에서 1~80까지 구간을 나누어 완탐
작은 구간의 사이즈가 총 길이의 반 이상 넘어가면 더 할 필요 없음

큰 단위로 평가하기->사이즈를 반으로 나눠서 

1,2,3으로 이루어진 수열
뽑아서 나열하고 작은구간부터 비교하는건 어려울거같은데,,
뽑으면서 갈까
이전거랑은 반드시 다른 걸 뽑아야햠 -3**80->2*80
생각이 안나면 완탐으로 먼저 구현해본다.


'''
#입력
N=int(input())
anslist=[3 for _ in range(N)]
min_answer=0
for i in range(0,N):
    min_answer+=3*(10**i)
# # 1,2,3중 N자리까지의 수열 뽑기
#
# # 착한 수열인지 판단하기, 1자리는 어차피 다르게 뽑았으니까 2자리부터 N//2 까지 한칸 건너 확인하기
# 처음부터 끝까지 완탐해야함!
def check(arr):
    #범주 잡기
    for i in range(1,len(arr)):
        #시작점 잡기
        # print("rangeset"+" "+str(i))
        for start in range(0,len(arr)-(i*2)+1):
            #시작점에서 i개, 이후로 i개
            flag=1
            # print("startset"+" "+str(start))
            for end in range(start+i,start+(2*i)):
                # print(start+end-(start+i),end)
                # print("val: ",end=' ')
                # print(arr[start+end-(start+i)],arr[end])
                if arr[start+end-(start+i)]!=arr[end]:
                    #다른게 발견되면 브레이크하고 다음 스타트지점을 확인하기
                    flag=0
                    break
            if flag==1:
                return False
    return True

#배열의 개수를 정수로 바꾸기
def to_int(arr):
    temp=0
    for i in range(0, N):
        temp += arr[N-(i+1)] * (10 ** i)
    return temp

def Perm(cnt,arr):
    global min_answer,anslist
    #백트 조건,anslist 값이랑 비교해서 자릿값이 벌써 크다면?->걍 끝내버려
    if cnt>0 and arr[cnt-1]>anslist[cnt-1]:
        return
    #백트 조건2, 크기가 2이상일때, 나쁜수열이면 끝내버려
    if cnt>1 and not check(arr):
        return
    #탈출조건
    if cnt==N:
        #착한 수열 판별
        if check(arr):
            temp=to_int(arr)
            #착한 수열일 때, 최소비교
            if min_answer>temp:
                min_answer=temp
                anslist=arr
        return
    #한개씩 뽑기
    for i in range(1,4):
        #첫번째는 3개 다 뽑고
        if cnt==0:
            Perm(cnt+1,arr+[i])
        #이후부터는 이전거랑 안겹치는것만 집어넣자
        else:
            if arr[cnt-1]!=i:
                Perm(cnt+1,arr+[i])


#구현부
Perm(0,[])
print(min_answer)