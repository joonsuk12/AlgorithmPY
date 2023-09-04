import sys
input=sys.stdin.readline

'''
1개로 두고 작으면 오른쪽을 늘리고 크면 왼쪽을 줄이면서 이동해보자.
사이즈가 1개 아래로 줄면? 없는거아닌가
1 3 5 7 11

에라토스테네스로 한번 걸러서 소수를 뽑고, 소수에서 투포인터를 돌리면 되지 않을까 싶은 느낌적인 느낌

'''

#입력, 선언부
N=int(input())

ans_count=0
num_list=[1 for i in range(N+2)]
prime_list=[]
#함수부
def Aratos():
    global  num_list
    #(루트 N+1)+1까지만 본인 다음의 곱의 배열의 값을 0으로 바꾼다.
    num_list[0]=0
    num_list[1]=0
    top=int((N+1)**0.5)+2
    for i in range(2,top):
        j=2
        while i*j<=N:
            num_list[i*j]=0
            j+=1
    for i in range(0,N+2):
        if num_list[i]==1: prime_list.append(i)
#투포인터로 조사하면서 가는 함수
def two_point():
    start=0
    end=0
    sum=prime_list[0]
    global ans_count
    #start부터 end까지의 합을 가지고 다니면서 sum이 N보다 크면 앞을 줄여보고
    #sum이 N보다 작으면 뒤를 늘려보기, start가 end를 넘어가면 종료시키기.
    while start<=end and 0<=start<len(prime_list) and 0<=end<len(prime_list):
        if sum==N:
            ans_count+=1
            end+=1
            if end<len(prime_list):
                sum+=prime_list[end]
            else:
                break
        elif sum<N:
            end+=1
            if end < len(prime_list):
                sum += prime_list[end]
            else:
                break
        else:
            if start<len(prime_list):
                sum-=prime_list[start]
                start+=1
            else: break

#실행
def solution():
    Aratos()
    two_point()
    print(ans_count)
    return
solution()