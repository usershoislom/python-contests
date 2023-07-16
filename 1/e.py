a = int(input())
b = int(input())

# Преобразуем числа a и b в двоичную систему счисления
a = bin(a)[2:].zfill(10)
b = bin(b)[2:].zfill(10)

# Используем цикл для проверки каждого бита на совпадение
for i in range(10):
    if a[i] == "1" and b[i] == "1":
        print("False")
        break
else:
    if "1" in a:
        print("True")
    else:
        print("False")