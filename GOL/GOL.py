from collections import Counter
 
def generation(world, N):
    "Play Conway's game of life for N generations from initial world."
    for g in range(N+1):
        display(world, g)
        world = life(world)

def life(world):
    """Count alive neighbors in the current world.
    Generate the alive bodies for the next world."""
    counts = Counter(n for c in world for n in offset(neighboring_cells, c))
    world = {c for c in counts 
             if counts[c] == 3 or (counts[c] == 2 and c in world)}
    return world
 
neighboring_cells = [(-1, -1), (-1, 0), (-1, 1), 
                     ( 0, -1),          ( 0, 1), 
                     ( 1, -1), ( 1, 0), ( 1, 1)]
 
def offset(cells, delta):
    "Slide/offset all the cells by delta, a (dx, dy) vector."
    (dx, dy) = delta
    return {(x+dx, y+dy) for (x, y) in cells}
 
def display(world, g):
    "Display the world as a grid of characters."
    print '          GENERATION {}:'.format(g)
    Xs, Ys = zip(*world)
    Xrange = range(min(Xs), max(Xs)+1)
    for y in range(min(Ys), max(Ys)+1):
        print ''.join('#' if (x, y) in world else '.'
                      for x in Xrange)
 
world   = {(0, 0), (1, 0), 
           (0, 1), (1, 1),
           (6, 2), (18, 2), (19, 2), (20, 2), (21, 2),
           (6, 3),
           (6, 4),
           (15, 5), (16, 5), (25, 5),
           (15, 6), (17, 6), (25, 6), (26, 6),
           (15, 7), (25, 7), (26, 7), (35, 7), (36, 7),
           (26, 8), (35, 8), (36, 8)}

 
generation(world, 5)
