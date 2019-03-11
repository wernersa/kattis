import sys

class Dungeon(object):
    """docstring for Dungeon."""
    def __init__(self, n, m):
        super(Dungeon, self).__init__()
        self.intersection_n = int(n)
        self.corridor_n = int(m)
        self.matrix = []

    def add_line(self, x, y, f):
        x, y = int(x), int(y)
        #Sort from start -> end, factor
        sorted_line = [min(x,y), max(x,y), float(f)]
        self.matrix.append(sorted_line)

    def calculate_factor(self):
        # Sort the corridors by start and stop intersection 
        self.matrix.sort(key = lambda l: (l[0], l[1]))
        #print(self.matrix)
        starts, stops, factors = zip(*self.matrix)

        possible_stops = set(stops)
        intersections_best_factor = {intersection: None for intersection in possible_stops}
        intersections_best_factor.update({0: 1.0})

        # For every possible 
        for start, stop, factor in self.matrix:
            factor_pre = intersections_best_factor.get(start)
            if not factor_pre:
                # There no factor for the starting intersection, it might be a blind alley
                continue
            factor_post = factor_pre * factor
            # Check if the current factor is better
            if intersections_best_factor[stop] is not None:
                if factor_post < intersections_best_factor[stop]:
                    continue
            intersections_best_factor[stop] = factor_post
        
        #print(intersections_best_factor)
        
        return intersections_best_factor[self.intersection_n - 1]



current_dungeon = None

for i in sys.stdin:
    line = i.split()
    
    if len(line) == 2:
        if current_dungeon:
            # Output the factor
            final_factor = current_dungeon.calculate_factor()
            print('{:6.4f}'.format(final_factor))
        #Start a new dungeon
        current_dungeon = Dungeon(*line)
    elif len(line) == 3:
        current_dungeon.add_line(*line)