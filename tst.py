from collections import namedtuple

AStarHelper = namedtuple("AStarHelper", ["pos", "new_way", "new_cost"])

a = AStarHelper(1, 2, 3)

b, c, d = a

print(b, c, d)