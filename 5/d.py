import re

pattern = r'((?<![\.\w])(?:[a-z0-9]|\.[a-z0-9])*\.(?:hlm|brhl))\.?\s'

with open('input.txt', 'r') as f, open('output.txt', 'w') as o:
    file_names = []
    lines = f.readlines()
    for line in lines:
        slt = re.findall(pattern, line)
        for sl in slt:
            if sl[0] != '.':
                file_names.append(sl)
    for f in file_names:
        o.write(f + '\n')
