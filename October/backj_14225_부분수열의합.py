import sys

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

S.sort()

target = 0
for i in S:
    if target + 1 < i : break
    target+=i

print(target+1)
