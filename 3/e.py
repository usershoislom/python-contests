n = int(input())
k = int(input())

col = []

for i in range(n):
    tmp = input().split()
    col.append(set(map(int, tmp)))

count = {}

for wires in col:
    for wire in wires:
        if wire not in count:
            count[wire] = 1
        else:
            count[wire] += 1


tmp = input()
broken = list(map(int, tmp.split()))

sorted_dict = {}

sorted_keys = sorted(count, key=lambda x: (-count[x], x))

for wire in sorted_keys:
    if wire not in broken:
        sorted_dict[wire] = count[wire]
res = []
for key, value in sorted_dict.items():
    # print(value)
    res.append(value)
    k -= 1
    if k == 0:
        break
res.reverse()
print(*res)