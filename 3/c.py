from collections import Counter

string = input()
num = int(input())

freq= Counter(string[i:i+num] for i in range(len(string)-num+1))
result = sorted(substr for substr, freq in freq.items() if freq >= 2)

print(result)
