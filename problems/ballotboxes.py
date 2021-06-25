#TODO: NOT SOLVED

import sys
import math

for case in range(3):
    N, B = [int(x) for x in sys.stdin.readline().split()]
    if N < 0:
        # All cases done, finished
        break
    cities = []

    # One ballot box for each city
    B = B - N

    cities_sum = 0
    for c in range(N):
        # [ population_per_box, ballotbox, population]
        population = int(sys.stdin.readline().strip())
        cities.append([population, 1, population])
        cities_sum += population
    
    cities.sort(reverse=True)
    
    cities_proporitons = [population[0] / cities_sum for population in cities]

    cities_subset = cities[:(B + 1)]  # Subset a minimum
    while B > 0:
        cities_subset[0][1] += 1  # Increment assigned boxes by one
        B -= 1  # Remove one box from the total pool available
        cities_subset[0][0] = cities_subset[0][2] / cities_subset[0][1]  # Calculate the assigned population per box
        cities_subset.sort(reverse=True)  # Sort by assigned_population
    print(int(math.ceil(cities_subset[0][0])))

    # Skip one line between each case
    sys.stdin.readline()
