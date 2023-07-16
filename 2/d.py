a = int(input())
b = int(input())

strings = []

while True:
    c = input()
    if c == '0':
        break
    strings.append(c)

length = a
stroka = []

for word in strings:
    if len(word) <= length and len(stroka) < b:
        stroka.append(word)
        length -= len(word) + 1
    else:
        print(" ".join(stroka))
        stroka = [word]
        length = a - len(word) - 1
print(" ".join(stroka))