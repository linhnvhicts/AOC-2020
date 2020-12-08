import re
with open('input.txt') as f:
    content = f.readlines()
content = [x.replace('\n', '').split(' ') for x in content] 
current_index = 0
current_accumulator = 0
passed_index = []

# part 2
# content[298][0] = 'nop' if content[298][0] == 'jmp' else 'jmp'

# part 1(comment part 2 above if handle part 1)
def traverse(index, accumulator):
    try:
        original_index = index
        single = content[index]
        if single[0] == 'nop':
            index += 1 
        elif single[0] == 'jmp':
            index = eval(str(index) + single[1])
        elif single[0] == 'acc':
            index += 1 
            accumulator = eval(str(accumulator) + single[1])
        if index in passed_index:
            print('messed up index need changing ' + str(original_index))
            print(index, accumulator)
            return
        else:
            passed_index.append(index)
            traverse(index, accumulator)
    except IndexError:
        print(accumulator)

traverse(current_index, current_accumulator)