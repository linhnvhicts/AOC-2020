with open('input.txt') as f:
    content = f.readlines()
content = [list(x.replace('\n', '')) for x in content] 
total_height = len(content)
width = len(content[0])

def traverse(row, height, tree_count, shift_right, shift_down):
    if height < total_height - 1:
        current_index = row + shift_right
        if current_index < width:
            next_down = content[height + 1][current_index]
            if next_down == "#":
                tree_count += 1
            next_row = current_index
        else:
            current_index = row - width + shift_right
            next_down = content[height + 1][current_index]
            if next_down == "#":
                tree_count += 1
            next_row = current_index
        
        next_heigth = height + shift_down
        traverse(next_row, next_heigth, tree_count, shift_right, shift_down)
    else:
        print(tree_count)


traverse(0, 0, 0, 3, 1)

                




        
