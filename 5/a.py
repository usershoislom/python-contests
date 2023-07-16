string = input()
new_string = []
for i, value in enumerate(string): 
    if i % 2 == 0:
        new_string.append(value.lower())
    else:
        new_string.append(value.upper())

print(*new_string, sep="")