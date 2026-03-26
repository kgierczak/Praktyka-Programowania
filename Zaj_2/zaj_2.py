import os
import time
import random

WIDTH = 20
HEIGHT = 20
ALIVE = " 𖹭 "
DEAD = " . "

def create_grid():
    return [[random.randint(0, 1) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def display_grid(grid):
    print("\033[H\033[J")
    print("Gra w życie \n")

    output = []
    for row in grid:
        output.append("".join(ALIVE if cell else DEAD for cell in row))

    print("\n".join(output))
    print(f"\n[ Press Ctrl+C to exit ]")

def count_neighbors(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue

            nr, nc = r + i, c + j
            if 0 <= nr < HEIGHT and 0 <= nc < WIDTH:
                count += grid[nr][nc]
    return count

def get_next_generation(grid):
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for r in range(HEIGHT):
        for c in range(WIDTH):
            neighbors = count_neighbors(grid, r, c)

            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0

    return new_grid

def main():
    grid = create_grid()

    try:
        while True:
            display_grid(grid)
            grid = get_next_generation(grid)
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\n\nSimulation ended by user.")

if __name__ == "__main__":
    main()