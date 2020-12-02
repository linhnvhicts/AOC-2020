import itertools
from itertools import combinations

with open('input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content] 

#solution 1: just replace 3 to 2 and remove index 2 from equation
#solution 2
results = list(combinations(content,3))
final_results = []
for i in results:
    if i[0] + i[1] + i[2]== 2020:
        final_results.append((i[0], i[1], i[2], i[0] * i[1] * i[2]))

print(final_results)