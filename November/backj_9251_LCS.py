import sys

input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())
answer = 0
lenA = len(A)
lenB = len(B)
# 백트래킹을 구현하고 테이블에 저장하는 방식
# def findMax(idxA, idxB, length, tempStr):
#     global answer
#     # 끝까지 다 조사했으면 반환하기
#     if idxA == lenA or idxB == lenB:
#         print(length)
#         print(tempStr)
#         answer=max(length, answer)
#         return length
#     # 현재 인덱스부터 뒤로 쭉 조사하면서 같은게 있으면 길이를 1 늘려주고 현재 idxB의 위치 저장
#     # idxB가 끝까지 갔으면 다음 걸로 한번 비교해봐야지
#     if idxB == lenB:
#         findMax(idxA + 1, 0, length, tempStr)
#     # 다음 인덱스로 가자
#     if A[idxA] == B[idxB]:
#         findMax(idxA + 1, idxB + 1, length + 1, tempStr + A[idxA])
#     else:
#         #다음 거랑 비교해보자
#         findMax(idxA, idxB+1, length, tempStr)
#         findMax(idxA+1, idxB, length, tempStr)


# dp로 바꿔보자

dp = [[-1] * lenB for _ in range(lenA)]
def findMaxDP(idxA, idxB):
    global answer

    #이제 기저는 0을 반환하게끔 한다.
    if idxA == lenA or idxB == lenB:
        return 0

    if dp[idxA][idxB] != -1:
        return dp[idxA][idxB]

    if A[idxA] == B[idxB]:
        dp[idxA][idxB] = 1 + findMaxDP(idxA + 1, idxB + 1)
    else:
        dp[idxA][idxB] = max(findMaxDP(idxA + 1, idxB), findMaxDP(idxA, idxB + 1))

    return dp[idxA][idxB]



result = findMaxDP(0, 0)
print(result)
