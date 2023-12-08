import sys

input = sys.stdin.readline

# 내 카드로 상대의 카드 수를 나워 나머지가 0이면 승리,
# 상대 카드 수로 내 카드가 나눠 떨어지면 패배
# 둘 다 아니면 무승부
# 승리는 1점, 패배는 -1점, 모든 플레이어와 게임하면 끝

# 일단 완탐으로 해볼까?

N = int(input())
cardList = list(map(int, input().split()))


# 각각의 플레이어에 대해
# 한번에 가야함, value로 정렬한다.
# 아니면 값을 딕셔너리 키로 두고, 점수를 value 로?
max_val=max(cardList)
cardDict=dict()
existList=[False for i in range(1000000+1)]

for i in cardList:
    cardDict[i]=0
    existList[i]=True
for start in range(0, N):
# 여기를 시간복잡도를 줄여야하는데, 어떻게 줄이지.
# 범위화 할수 없음->이분탐색 아닌듯
# 인덱스랑 값을 놓고, 정렬한 다음에 얘보다 큰 애들에 대해서 얘를 곱해서 만들어지는 애면 +1씩 해볼까?
    cnt=2
    end = cardList[start] * cnt
    while end <= max_val:
        #비교되는 값이 start로 나눠 떨어진다면 start에 속하는 값을 +1, end에 속하는 값을 -1
        if existList[end]:
            #값이 존재한다면
            cardDict[end]-=1
            cardDict[cardList[start]]+=1
        cnt+=1
        end=cardList[start] * cnt
for i in cardList:
    print(cardDict[i],end=' ')