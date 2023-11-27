import sys

input = sys.stdin.readline

# 코테에 꽤나 자주 나오는 dp유형 익히기

# 가장 긴 증가하는 부분 수열 구하기.

# 현재 문자까지의 가장 긴 증가하는 부분 수열의 길이를 dp에 저장해나가는데
# 두 문자열의 인덱스로 이루어진 배열을 만든다.
A = list(input().rstrip())
B = list(input().rstrip())
answer = 0
lenA = len(A)
lenB = len(B)


# 백트래킹을 구현하고 테이블에 저장하는 방식
# 부분 수열의 길이와, 현재 문자에 대한 정보로 dp배열을 구성하자
# 현재 문자까지의 공통 부분 수열의 최대 길이를 저장할건데
# 두 문자에 대한 배열?
# dp배열에 저장될 값은 1부터 현재까지의 길이
# dp=[lenA][lenB]
def findMax(idxA, idxB, length, tempStr):
    global answer
    # 끝까지 다 조사했으면 반환하기
    if idxA == lenA:
        print(length)
        print(tempStr)
        answer=max(length, answer)
        return length
    # 현재 인덱스부터 뒤로 쭉 조사하면서 같은게 있으면 길이를 1 늘려주고 현재 idxB의 위치 저장
    # 다음 인덱스로 가자
    for i in range(idxB, lenB):
        if A[idxA] == B[i]:
            findMax(idxA + 1, i + 1, length + 1,tempStr+A[idxA])
    # 안똑같으면 그냥 다음걸로 보내야지
    findMax(idxA + 1, idxB, length, tempStr)


findMax(0, 0, 0 ,"")
print(answer)




