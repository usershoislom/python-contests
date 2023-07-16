l = int(input())
command = list(input())

string = "".join(command)

if len(command) <= l:
    print(string)
else:
    row = ''
    row = string[0:l] + ' '
    print(row[:-1])

    string = string[l:]
    for i in range(len(string)):
        print('&' * (l-1) + string[i])
