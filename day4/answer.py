import collections
import re
with open('input.txt') as f:
    content = f.read()
content = content.split('\n\n')
new_content = [x.replace('\n', ' ') for x in content]
valid = 0
valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for single in new_content: # per passport
    details_list = single.split(' ')
    batch_keys = [] #list of key
    detail_dict = {} #dictionary of key and value
    for details in details_list:
        single_detail_list = details.replace(' ', '').split(':')
        detail_dict[single_detail_list[0]] = single_detail_list[1]
        batch_keys.append(single_detail_list[0])
    
    if set(valid_keys).issubset(batch_keys):
        if ((1920 <= int(detail_dict['byr']) <= 2002)
        and (2010 <= int(detail_dict['iyr']) <= 2020)
        and (2020 <= int(detail_dict['eyr']) <= 2030)
        and (150 <= int(detail_dict['hgt'].split('cm')[0]) <= 193 if detail_dict['hgt'][-2:] == 'cm' else 59 <= int(detail_dict['hgt'].split('in')[0]) <= 76 if detail_dict['hgt'][-2:] == 'in' else False)
        and (bool(re.match(r'#[0-9a-f]{6}', detail_dict['hcl'])))
        and(detail_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        and(len(detail_dict['pid']) == 9 and detail_dict['pid'].isdigit())):
            print(single)
            valid += 1
print(valid)


