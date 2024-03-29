import random
from collections import deque

#function that generates a random maze 
def maze_gen(rows, cols, begin, end):
    maze = [['#' for _ in range(cols)] for _ in range(rows)] #creates a 'maze' made of a grid of # as the walls
    stack = [begin] #keeps track of places to explore next
    maze[begin[0]][begin[1]] = ' ' #pre-sets the beginning point
    maze[end[0]][end[1]] = ' ' #pre-sets the end point

    while stack: #while stack still has places to explore 
        cell = stack[-1] #looks at the previous location
        x, y = cell 
        neighbors = [] #neighing points, places to go next

        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]: #looks in each direction for next cell to go 
            nx, ny = x + dx, y + dy 
            if 1 <= nx < rows - 1 and 1 <= ny < cols - 1 and maze[nx][ny] == '#': #if next cell is inside the grid of # or the 'maze'
                neighbors.append((nx, ny)) 

        if neighbors: #if theres new cell to go, randomize between neighbors
            nx, ny = random.choice(neighbors)
            maze[nx][ny] = ' ' #makes new cell empty
            maze[x + (nx - x) // 2][y + (ny - y) // 2] = ' ' #makes the wall between old and new cell empty
            stack.append((nx, ny)) #add new cell to next to explore
        else:
            stack.pop() #otherwise, go back if no new cells to go to 

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #if there is a way in and out 
        if maze[begin[0] + dx][begin[1] + dy] == '#': #allows for the starting point to not be blocked by a wall
            maze[begin[0] + dx][begin[1] + dy] = ' '
        if maze[end[0] + dx][end[1] + dy] == '#': #allows for the ending point to not be blocked by a wall
            maze[end[0] + dx][end[1] + dy] = ' '

    return maze #returns the generated maze

#function to find the shortest path
def shorest_path(begin, end, maze): 
    paths = [] #keeps track of each possible way
    been = set() #keeps track of places that have been visited
    rows = len(maze) #how many rows the maze has, also the height
    cols = len(maze[0]) #how many columns the maze has, also the width

    def bfs(begin, end): #to find the shorest path
        queue = deque() #places to check next
        been.add(begin) #takes note that its been visited
        queue.append((begin, [begin])) #starts exploring

        while queue: #looks until there is no celll left 
            curr, path = queue.popleft() #looks at next cell 
            been.add(curr) #takes note that its been visisted 

            if curr == end: #if end is reached, remember the path
                paths.append(path)
            else: #otherwise check all the directions possible
                i, j = curr[0], curr[1]
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    new_i, new_j = i + dx, j + dy
                    if new_i in range(rows) and new_j in range(cols) and (new_i, new_j) not in been and maze[new_i][new_j] == " ": #if next cell is unvisited and not a wall, go there next
                        queue.append(((new_i, new_j), path + [(new_i, new_j)]))
                        been.add((new_i, new_j))
        
    bfs(begin, end) 
    if paths:
        min_path_index = 0
        for i in range(len(paths)): #finds the shortest path taken
            if len(paths[i]) < len(paths[min_path_index]):
                min_path_index = i
        for i in paths[min_path_index]: #X is used to mark the cells that are on the path of shorest path on the maze 
            maze[i[0]][i[1]] = "X"


rows, cols = 11, 10 #dimensions of the maze 

begin_point = (1, 1) #beginning point 
end_point = (9, 8) #ending point


maze = maze_gen(rows, cols, begin_point, end_point)
shorest_path(begin_point, end_point, maze)


for row in maze:
    print(' '.join(row))
