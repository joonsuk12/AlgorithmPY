import sys

input = sys.stdin.readline

N, M, L, K = map(int, input().split())
starList = []
answer=K

for i in range(K):
    col, row = map(int, input().split())
    starList.append([row, col])

#두 별을 좌하, 우상으로 뽑기

for start in starList:
    for end in starList:
        tempAns = K
        for i in starList:
            if start[1] <= i[1] <= start[1] + L and end[0]<= i[0] <= end[0]+L:
                tempAns -= 1
        answer = min(tempAns, answer)

print(answer)


#
# def setDev(direct, r, c):
#     global L, M, N
#     # 좌하 우하 좌상 우상
#     if direct == 0:
#         if r + L > M:
#             r -= (r + L) - M
#         if c + L > N:
#             c -= (c + L) - N
#         tempList = [[r, c], [r, c + L], [r + L, c], [r + L, c + L]]
#     elif direct == 1:
#         # 우하
#         if r + L > M:
#             r -= r + L - M
#         if c - L < 0:
#             c += L - c
#         tempList = [[r, c - L], [r, c], [r + L, c - L], [r + L, c]]
#     elif direct == 2:
#         # 좌상
#         if r - L < 0:
#             r += L - r
#         if c + L > N:
#             c -= (c + L) - N
#         tempList = [[r - L, c], [r - L, c + L], [r, c], [r, c + L]]
#
#     else:
#         # 우상
#         if r - L < 0:
#             r += L - r
#         if c - L < 0:
#             c += L - c
#         tempList = [[r - L, c - L], [r - L, c], [r, c - L], [r, c]]
#     return tempList
#
#
#
# for y, x in starList:
#     # 해당 점을 기준으로 4방향에 대해 도화지를 놓고
#     for i in range(4):
#         tempAns=K
#         tramp = setDev(i, y, x)
#         # 나머지 점들을 쭉 비교해보자고,
#         dev=[]
#         for row, col in starList:
#             #주어진 점이 범위 내에 있으면
#             leftLow=tramp[0]
#             if leftLow[0]<=row<=leftLow[0]+L and leftLow[1]<=col<=leftLow[1]+L:
#                 tempAns-=1
#                 dev.append([row,col])
#             #좌하 좌표만 알아도 가능하긴 함.
#         answer=min(answer,tempAns)
# print(answer)