# Returns true if point (x,y) is in_q2.
def in_q2(x, y):
    return x <= 0 and y >= 0

# Returns true if a point is on the edge of a quadrant
def on_edge(x, y):
    return x == 0 or y == 0

# Inputs: p1, p2 are point tuples (x, y)
# Returns true if both points are in q2 and not both on the edge of the quadrant
def line_in_q2(p1, p2):
    return (in_q2(*p1) and in_q2(*p2)) and not (on_edge(*p1) and on_edge(*p2))


def filter_line_segments(lines):
    return [i for (i, p1, p2) in lines if line_in_q2(p1, p2)]
