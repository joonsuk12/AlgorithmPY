import sys

input = sys.stdin.readline

T = int(input())
numList = []
for i in range(T):
    numList.append(int(input()))
ansList = []
calList=[' ','+','-']
realcalList=['+','-']


def cal(tempList):
    list_len=len(tempList)
    cal_list=[]
    temp_num=str()
    for j in range(list_len):
        #연산자 나오기 전까지는 숫자를 만들고
        if j==list_len-1:
            temp_num += str(tempList[j])
            cal_list.append(int(temp_num))
        if tempList[j]==' ':
            continue
        if not tempList[j] in realcalList:
            temp_num+=str(tempList[j])
        #연산자 나오면 이전에 만들던 숫자 리스에 넣고 숫자 문자 초기화
        else:
            cal_list.append(int(temp_num))
            cal_list.append(tempList[j])
            temp_num=""
    #다 돌면서 숫자 다음 연산자 면 그 다음 숫자를 찾아서 연산
    #마지막 인자가 연산자면 땡
    cal_len=len(cal_list)
    if cal_len<3:
        return
    #계산
    ans=cal_list[0]
    for at in range(0,cal_len-2):
        if cal_list[at] in realcalList:
            continue
        #연산자 기준에 따라
        if cal_list[at+1]=='+':
            ans+=cal_list[at+2]
        else:
            ans-=cal_list[at+2]
    if ans==0:
        for i in tempList:
            print(i,end='')
        print()
    return

def dfs(idx, tempList, num_list):
    # 탈출지점
    if idx ==len(num_list):
        cal(tempList)
        return
    #dfs 로직, 더하거나 빼거나 합치거나로 넘어간다.
    for calc in range(3):
        tempList.append(calList[calc])
        tempList.append(num_list[idx])
        dfs(idx+1,tempList,num_list)
        tempList.pop()
        tempList.pop()



for num in numList:
    dfs(0, [1], [i for i in range(2, num + 1)])
    print()
