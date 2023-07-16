sentence = input()

target = ['hahaha', 'massiv', 'manul']

found_words = []

for substr in sentence.split():
    for word in target:
        if word in substr:
            # print(word)
            found_words.append(word)

# print(found_words)

print(len(set(found_words)) == 2)