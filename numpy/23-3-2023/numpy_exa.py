def find_position(lst, value):

    positions = []
    '''
    for i in range(len(lst)):
        if lst[i] == value:
            positions.append(i + 1)'''

    count = len(positions)
    '''
    if count == 0:
        return f"value {value} not found in the list"
    elif count == 1:
        return f"the position of value {value} is {positions[0]}th position and it appears 1 time"
    else:'''
    position_str = ', '.join([str(p) + 'th position' for p in positions[:-1]])
    position_str += f" and {positions[-1]}th position"
    return f"the position of value {value} is {position_str} and it appears {count} times"

l1 = [15, 9, 11, 3, 23, 12, 3, 43]
value = 3
output = find_position(l1, value)
print(output)  # Output: the position of value 3 is 4th position, 7th position and it appears 2 times
