import sys

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) != 5:
        continue
    sha1, date, author, email, message = fields
    output = f"{sha1[:7]}{'.' * (73 - len(message))}{message}"
    print(output)
