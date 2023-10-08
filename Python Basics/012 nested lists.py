
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

'''
# print list or individual cells
print(cells[0])
print(cells[0][1])
print(cells[1][2])

# use for loop to iterate list and print elements
for x in cells:
    print ('Element:', x)

# to access elements of sublists: nested for loops
for x in cells:
    for y in x:
        print('Sub-element:', y)

#renamed variables and making value explicit
table = [['C1', 'C2', 'C3'], ['D1', 'D2', 'D3']]
for row in table:
    for cell in row:
        # print cell with empty space and get rid of new-line character at end
        print(cell, '', end='')
    # print to get a new-line character
    print()

# nested-list comprehension: repeat inner-list comprehension until control variable of j reaches value of 4 

tab = [[i for i in range (1,6)] for j in range(4)]
print(tab)
'''
