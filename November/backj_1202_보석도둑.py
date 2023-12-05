import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

# 조합풀이는 진짜 절대 네버 아님
# 보석 정보
jewels = []
for i in range(N):
    jewels.append(list(map(int, input().split())))

# 가방 정보
bags = []
for i in range(K):
    bags.append(int(input()))

# 보석을 무게순으로 정렬하고, 무게가 같다면 가치순으로 정렬한다
jewels.sort(key=lambda x: (x[0], x[1]))
# 가방도 작은 가방부터 채워보자
bags.sort()

heapList = []
answer = 0
check_idx = 0
# 가방마다 담을 수 있는 보석들을 찾는다.
for i in range(0, K):
    # 무게가 넘기전까지 일단 보석들을 다 찾아서 힙에 저장한다.
    while len(jewels) != 0:
        # 무게를 비교하고
        if bags[i] >= jewels[0][0]:
            # 최대힙으로 해야하므로 - 값을 넣고 뒤에 가치를 넣는다.
            heapq.heappush(heapList, (-jewels[0][1], jewels[0][1]))
            # jewels의 가장 작은 값부터 없애가야겠지?
            heapq.heappop(jewels)
        else:
            break
    # 작은 애들은 이미 힙에 들어있어 다음 가방에도 널 수 있다.
    # 현재 힙에 있는 값들 중 가장 큰 값을 정답에 저장해준다
    if heapList:
        answer += heapq.heappop(heapList)[1]
print(answer)
