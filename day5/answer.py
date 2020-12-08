with open('input.txt') as f:
    content = f.readlines()
content = [list(x.replace('\n', '')) for x in content] 
seat_list = []
for seat in content:
    row_list = list(range(0, 128))
    column_list = list(range(0, 8))
    rows = seat[:7]
    lists = seat[-3:]
    for idx, val in enumerate(rows):
        if val == "F":
            row_list = row_list[:(int(len(row_list)/2))]
        elif val == "B":
            row_list = row_list[(int(len(row_list)/2)):]

    for idx, val in enumerate(lists):
        if val == "L":
            column_list = column_list[:(int(len(column_list)/2))]
        elif val == "R":
            column_list = column_list[(int(len(column_list)/2)):]

    seat_number = row_list[0] * 8 + column_list[0]
    seat_list.append(seat_number)

seat_list.sort()
full_list = list(range(min(seat_list), max(seat_list) + 1))
print('part 1', max(seat_list))
print('part 2', [x for x in full_list if x not in seat_list][0])