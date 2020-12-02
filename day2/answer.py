with open('input.txt') as f:
    content = f.readlines()
content = [tuple(z.replace(':', '') for z in x.split(" ")) for x in content] 
content_len = len(content)
for single in content:
    letter_range = tuple(single[0].split('-'))
    string = single[2].replace('\n', '')
    count=0
    #solution 1
    # if single[2].replace('\n', '').count(single[1]) < int(letter_range[0]) or single[2].replace('\n', '').count(single[1]) > int(letter_range[1]):
    # content_len -= 1
    # solution 2
    try:
        if string[int(letter_range[0]) - 1] == single[1]:
            count +=1
    except Exception as e:
        pass
    try:
        if string[int(letter_range[1]) - 1] == single[1]:
            count +=1
    except Exception as e:
        pass

    if count != 1:
        content_len -= 1

print(content_len)
