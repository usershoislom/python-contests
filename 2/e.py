i = int(input())
count = 0
password = 0

while count < i:
    password += 1
    if str(password).count('3') == 3:
        count += 1

print(password)
