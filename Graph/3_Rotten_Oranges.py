def orangesRotting(grid):
    
    from collections import deque
    visited = set()
    queue = deque()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                visited.add((row,col))
            elif grid[row][col] == 2:
                queue.append((row,col))
    ans = 0

    while visited and queue:
        for _ in range(len(queue)):
            r,c = queue.popleft()
            for neigbour in ((r,c-1),(r,c+1),(r-1,c),(r+1,c)):
                if neigbour in visited:
                    visited.remove(neigbour)
                    queue.append(neigbour)
        ans +=1
    return -1 if visited else ans
    