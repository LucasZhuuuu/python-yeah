import math

# Loop through the grid and count every pair of twin primes that are next to each 
# other horizontally, vertically, or diagonally


# 1. Both Prime
# 2. Next to eachother
# 3. Differ by exactly 2


# 12 5  7  9
# 11 13 17 19
# 4  6  7  3 
grid = [
    [12, 5, 7, 9], 
    [11, 13, 17, 19], 
    [4, 6, 7, 3]
]
def is_prime(n : int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

# count_pairs = (grid) -> int

# print(math.abs(#)) <-------- absolute value of # integer 

# tuple (x, y)
tuple1 = (3, 5) # could be something like coordinates

directions = [
    (-1, 0), # left
    (1, 0), # right
    (0, 1), # up
    (0, -1), # down
    (-1, 1), # northwest
    (1, 1), # northeast
    (-1, -1), # southwest
    (1, -1) # southeast
]

def count_pairs(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])

    count = 0
    
    for r in range(rows):
        for c in range(cols):

            current = grid[r][c]
            if not is_prime(current):
                continue
            else:
                # right = grid[r][c + 1]
                # left = grid[r][c - 1]
                # up = grid[r - 1][c]
                # down = grid[r + 1][c]
                for dr, dc in directions:
                    nr = r + dr 
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbour = grid[nr][nc]
                        print(f"neighbour: {neighbour} current: {current}")
                        if abs(neighbour - current) == 2 and is_prime(neighbour):
                            count += 1   
                            # print(f"neighbour: {neighbour} current: {current}")

            # if right - num == (math.abs(2)): # how to make this apply for all of them tho? 
            #                                     #without having to write it one by one?
            #     count_pairs += 1
            # else:
            #     break
    return count

print(count_pairs(grid))




# for n in grid



