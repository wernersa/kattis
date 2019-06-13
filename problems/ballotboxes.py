import sys
import math

for case in range(3):
    N, B = [int(x) for x in sys.stdin.readline().strip("\n").split(" ")]
    if N < 0:
        # All cases done, finished
        break
    cities = []

    # One ballot box for each city
    B = B - N

    for c in range(N):
        # [ population, ballotbox, assigned_population]
        population = int(sys.stdin.readline().strip("\n"))
        cities.append([population, 1, population])
    
    cities.sort(key=lambda x: x[2]) #Sort by assigned_population
    cities_subset = cities[-(B + 1):] #Subset a minimum 
    while B > 0:
        pot_boxes = 1
        cities_subset[-1][1] += pot_boxes
        cities_subset[-1][2] = cities_subset[-1][0] / cities_subset[-1][1]
        B -= pot_boxes
        cities_subset.sort(key=lambda x: x[2]) #Sort by assigned_population
        cities_subset = cities_subset[-(B + 1):] #Subset a minimum
    print(int(math.ceil(cities_subset[-1][2])))

    sys.stdin.readline()

# print("output")

#print("error", file=sys.stderr )
