from itertools import product
val = []
for i in range(2):
    val.append(list(map(int, input().strip().split())))
answer =(list(product(*val)))
for i in range(len(answer)):
    print(answer[i], end=" ")
