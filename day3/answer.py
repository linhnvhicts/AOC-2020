# import sys
# sys.setrecursionlimit(10000)

with open('input.txt') as f:
    content = f.readlines()
content = [list(x.replace('\n', '')) for x in content] 
height = len(content)
width = len(content[0])

def traverse(row, height):
    tree_count = 0
    if height < height + 1:
        try:
            next_down = content[height + 1][row + 3]
            if next_down == "#":
                tree_count += 1
            next_row = row + 3
        except IndexError:
            bad_row = row + 3
            new_row = bad_row - width - 1 # start from index new_row of that line
            next_down = content[height + 1][new_row + 3]
            if next_down == "#":
                tree_count += 1
            next_row = new_row + 3
        
        next_heigth = height + 1
        
        traverse(next_row, next_heigth)
    else:
        return tree_count


print(traverse(0, 0))

                




        
