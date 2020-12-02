import itertools
from itertools import combinations

with open('input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content] 

results = list(combinations(content,3))
final_results = []
for i in results:
    if i[0] + i[1] + i[2]== 2020:
        final_results.append((i[0], i[1], i[2], i[0] * i[1] * i[2]))

print(final_results)