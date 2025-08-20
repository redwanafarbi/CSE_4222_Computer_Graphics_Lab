import math
import matplotlib.pyplot as plt

def snowflake_segment(p1, p2, it):
    """
    Recursively generate the polyline points of a Koch segment from p1 to p2.
    p1, p2: (x, y)
    it: iteration depth
    returns: list of points [(x0,y0), (x1,y1), ...] including both ends
    """
    x1, y1 = p1
    x5, y5 = p2

    if it == 0:
        return [p1, p2]

    # Points at 1/3 and 2/3 along the segment
    dx, dy = (x5 - x1) / 3.0, (y5 - y1) / 3.0
    x2, y2 = x1 + dx,       y1 + dy
    x4, y4 = x1 + 2 * dx,   y1 + 2 * dy

    # Peak point (equilateral triangle outward)
    # This matches: ( (x1+x5)/2 + sqrt(3)*(y1-y5)/6 , (y1+y5)/2 + sqrt(3)*(x5-x1)/6 )
    xm, ym = (x1 + x5) / 2.0, (y1 + y5) / 2.0
    sx, sy = (math.sqrt(3) * (y1 - y5) / 6.0,
              math.sqrt(3) * (x5 - x1) / 6.0)
    x3, y3 = xm + sx, ym + sy

    # Recurse on 4 sub-segments: [p1->p2],[p2->p3],[p3->p4],[p4->p5]
    a = snowflake_segment((x1, y1), (x2, y2), it - 1)
    b = snowflake_segment((x2, y2), (x3, y3), it - 1)
    c = snowflake_segment((x3, y3), (x4, y4), it - 1)
    d = snowflake_segment((x4, y4), (x5, y5), it - 1)

    # Concatenate while avoiding duplicate endpoints
    return a[:-1] + b[:-1] + c[:-1] + d

def koch_snowflake(points, iteration):
    """
    Build full snowflake polyline from 3 control points (triangle vertices).
    points: [(xA,yA), (xB,yB), (xC,yC)]
    returns: list of points around the triangle (closed path)
    """
    pA, pB, pC = points
    seg1 = snowflake_segment(pA, pB, iteration)[:-1]
    seg2 = snowflake_segment(pB, pC, iteration)[:-1]
    seg3 = snowflake_segment(pC, pA, iteration)      # keep last to close
    return seg1 + seg2 + seg3

def plot_polyline(poly):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, linewidth=1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("Koch Snowflake")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    iteration = 4
    # Triangle
    tri = [(250, 15), (50, 350), (450, 350)]
    snow = koch_snowflake(tri, iteration)
    plot_polyline(snow)
