import collections
with open('input.txt') as f:
    content = f.read()
content = content.split('\n\n')
total = 0
# part 1
# new_content = ["".join(set(x.replace('\n', ''))) for x in content]
# for single in new_content:
#     total += len(single)

# print(total)

# part 2
for single in content:
    member = 1
    extra_member = single.count('\n')
    member += extra_member
    characters_number = collections.Counter(single.replace('\n', ''))
    for key, value in characters_number.items():
        if value == member:
            total += 1

print(total)