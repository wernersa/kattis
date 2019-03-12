import sys

# Stack: Last-in, First-out
# Queue: First-in, First-out
# Priority Queue: Largest element first
# Impossible
# Not sure


def operate(operations):
    # We assume all data structures could be true to begin with
    bags = {         "stack": [True, []],
                     "queue": [True, []],
            "priority queue": [True, []]}

    for operation, item in operations:

        if operation == 1:
            # Add operation
            bags["stack"][1].append(item)
            bags["queue"][1].insert(0,item)
            bags["priority queue"][1].append(item)
        else:
            # Remove operation
            try:
                if bags["stack"][1].pop() != item:
                    bags["stack"][0] = False
                if bags["queue"][1].pop() != item:
                    bags["queue"][0] = False
                bags["priority queue"][1].sort()
                if bags["priority queue"][1].pop() != item:
                    bags["priority queue"][0] = False
            except:
                print("impossible")
                return

    #Check possible data structures:
    possible = [bags[x][0] for x in bags.keys()]
    if sum(possible) > 1:
        print("not sure")
    elif sum(possible) == 0:
        print("impossible")
    else:
        for key, val in bags.items():
            if val[0] == True:
                print(key)


    
    

for i, line in enumerate(sys.stdin):
    line = line.split()
    line = list(map(int, line))
    if len(line) == 1:
        i_left = line[0]
        operations = list()
        continue
    else:
        operations.append(line)
        i_left -= 1
    if i_left == 0:
        operate(operations)
