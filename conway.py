import random, time, copy
width = 60
height = 20

# create a list of lists
next_cells = []
for x in range(width):
    column = []  # create new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append("#")  # add a living cell
        else:
            column.append(" ")  # add dead cell
    next_cells.append(column)  # next_cells is a list of column lists

while True: # main loop
    print("\n\n\n\n\n")  # separate each step with new lines
    current_cells = copy.deepcopy(next_cells)

    # print current cells on screen
    for y in range(height):
        for x in range(width):
            print(current_cells[x][y], end="")  # print the # or space
        print()  # print a new line at the end of the row

    # calculate next step's cells based on current step's cells
    for x in range(width):
        for y in range(height):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            left_coord = (x - 1) % width
            right_coord = (x + 1) % width
            above_coord = (y - 1) % height
            below_coord = (y + 1) % height

            # count number of living neighbours
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == "#":
                num_neighbors += 1
            if current_cells[x][above_coord] == "#":
                num_neighbors += 1
            if current_cells[right_coord][above_coord] == "#":
                num_neighbors += 1
            if current_cells[left_coord][y] == "#":
                num_neighbors += 1
            if current_cells[right_coord][y] == "#":
                num_neighbors += 1
            if current_cells[left_coord][below_coord] == "#":
                num_neighbors += 1
            if current_cells[x][below_coord] == "#":
                num_neighbors += 1
            if current_cells[right_coord][below_coord] == "#":
                num_neighbors += 1

                # Set cell based on Conway's Game of Life rules:
            if current_cells[x][y] == "#" and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[x][y] == "#"
            elif current_cells[x][y] == " " and num_neighbors == 3:
                next_cells[x][y] = "#"
            else:
                next_cells[x][y] = " "
    time.sleep(1)
