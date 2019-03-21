import sys
sys.setrecursionlimit(10**6) # "Run Time Error" if not.

NEIGHBOURS = [( 0, 1),
              ( 0,-1),
              ( 1, 0),
              (-1, 0)]

def remove_neighbours(pixels, x, y):
    if pixels[x][y]:
        pixels[x][y] = False
        for i, j in NEIGHBOURS:
            new_x = x + i
            new_y = y + j
            if not (new_x < 0 or new_y < 0 or new_x >= len(pixels) or new_y >= len(pixels[0])):
                pixels = remove_neighbours(pixels, new_x, new_y)
    return pixels

for case_i, case in enumerate(sys.stdin):
    m, n = [int(x) for x in case.split()]
    found = [[False for x in range(n)] for x in range(m)]
    for l in range(m):
        line = sys.stdin.readline()
        for pixel in range(n):
            if line[pixel] == "-":
                found[l][pixel] = True
    
    count = 0
    remaining = list(range(len(found)))
    while len(remaining) > 0:
        for x in remaining:
            line = found[x]
            if True in line:
                y = line.index(True)
                found = remove_neighbours(found, x, y)
                count += 1
            else:
                remaining.remove(x)
                continue
    
    print(f"Case {case_i + 1}: {count}")



