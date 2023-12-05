import sys
input=sys.stdin.readline


#입력이 순서대로 안들어옴, 그러면 걍 딕셔너리로 푸는게 나을 듯?
tree=dict()
N=int(input())
for i in range(N):
    name, left, right=input().split()
    tree[name]=[name,left,right]


#트리를 쭉 만들어 놨으면, A,B,C  B,A,C B,C,A 순서로 접근하기, 리프노드일 경우 출력하기
#항상 A부터 시작이니까
head=tree['A']
#재귀 느낌으로 계속 부르면 되지 않나?
def preOrder(now):
    print(now[0], end='')
    if now[1]!='.':
        preOrder(tree[now[1]])
    if now[2]!='.':
        preOrder(tree[now[2]])
    return
def midOrder(now):
    if now[1]!='.':
        midOrder(tree[now[1]])
    print(now[0], end='')
    if now[2]!='.':
        midOrder(tree[now[2]])
    return
def subOrder(now):
    if now[1]!='.':
        subOrder(tree[now[1]])
    if now[2]!='.':
        subOrder(tree[now[2]])
    print(now[0], end='')
    return

preOrder(head)
print()
midOrder(head)
print()
subOrder(head)
print()




