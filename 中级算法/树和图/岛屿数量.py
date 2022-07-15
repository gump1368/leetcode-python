#! -*- coding: utf-8 -*-
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        lands = []
        island_count = 0
        count = 0
        while True:
            x = count // cols
            y = count % cols
            print(x, y)
            if grid[x][y] == '1':
                island_count += 1
                lands.append((x, y))
                while lands:
                    x, y = lands.pop()
                    right = grid[x][y + 1] if y + 1 < cols else ''
                    down = grid[x + 1][y] if x + 1 < rows else ''
                    up = grid[x-1][y] if x-1 >= 0 else ''
                    left = grid[x][y-1] if y-1 >= 0 else ''
                    if right == '1' and (x, y+1) not in lands:
                        grid[x][y + 1] = '0'
                        lands.append((x, y + 1))
                    if down == '1' and (x+1, y) not in lands:
                        grid[x + 1][y] = '0'
                        lands.append((x + 1, y))
                    if up == '1' and (x-1, y) not in lands:
                        grid[x-1][y] = '0'
                        lands.append((x-1, y))
                    if left == '1' and (x, y-1) not in lands:
                        grid[x][y-1] = '0'
                        lands.append((x, y-1))

            count += 1
            if count >= rows * cols:
                break
        return island_count



if __name__ == '__main__':
    test = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    solution = Solution()
    print(solution.numIslands(test))

