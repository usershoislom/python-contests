num1 = int(input())
num2 = int(input())

result = abs(num1) % abs(num2)
if num1 < 0:
    result *= -1
print(result)