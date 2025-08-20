# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt

# Defining maximum number of points in polygon
MAX_POINTS = 20

# Function to return x-value of point of intersection of two lines
def x_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num / den

# Function to return y-value of point of intersection of two lines
def y_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num / den

# Function to clip all the edges w.r.t one clip edge of clipping area
def clip(poly_points, poly_size, x1, y1, x2, y2):
    # Use float to avoid losing precision on intersections
    new_points = np.zeros((MAX_POINTS, 2), dtype=float)
    new_poly_size = 0

    for i in range(poly_size):
        # i and k form a line in polygon
        k = (i + 1) % poly_size
        ix, iy = poly_points[i]
        kx, ky = poly_points[k]

        # Position w.r.t. clipper line (left side test)
        i_pos = (x2 - x1) * (iy - y1) - (y2 - y1) * (ix - x1)
        k_pos = (x2 - x1) * (ky - y1) - (y2 - y1) * (kx - x1)

        # Case 1 : both inside -> keep k
        if i_pos < 0 and k_pos < 0:
            new_points[new_poly_size] = [kx, ky]
            new_poly_size += 1

        # Case 2 : i outside, k inside -> add intersection then k
        elif i_pos >= 0 and k_pos < 0:
            xi = x_intersect(x1, y1, x2, y2, ix, iy, kx, ky)
            yi = y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)
            new_points[new_poly_size] = [xi, yi]
            new_poly_size += 1
            new_points[new_poly_size] = [kx, ky]
            new_poly_size += 1

        # Case 3 : i inside, k outside -> add only intersection
        elif i_pos < 0 and k_pos >= 0:
            xi = x_intersect(x1, y1, x2, y2, ix, iy, kx, ky)
            yi = y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)
            new_points[new_poly_size] = [xi, yi]
            new_poly_size += 1

        # Case 4 : both outside -> add nothing
        else:
            pass

    clipped_poly_points = np.array(new_points[:new_poly_size], dtype=float)
    return clipped_poly_points, new_poly_size

# Function to implement Sutherland–Hodgman algorithm
def suthHodgClip(poly_points, poly_size, clipper_points, clipper_size):
    for i in range(clipper_size):
        k = (i + 1) % clipper_size
        poly_points, poly_size = clip(
            poly_points, poly_size,
            clipper_points[i][0], clipper_points[i][1],
            clipper_points[k][0], clipper_points[k][1]
        )
        if poly_size == 0:
            break
    return poly_points, poly_size

# Plotting helper
def plot_polygons(original_poly, clipper_poly, clipped_poly=None):
    def close_ring(P):
        if len(P) == 0:
            return P
        if not np.allclose(P[0], P[-1]):
            return np.vstack([P, P[0]])
        return P

    orig = close_ring(np.array(original_poly, dtype=float))
    clip = close_ring(np.array(clipper_poly, dtype=float))
    plt.figure(figsize=(7, 6))

    # Clipper polygon
    plt.plot(clip[:,0], clip[:,1], linewidth=2, label="Clipper polygon")

    # Original polygon
    plt.plot(orig[:,0], orig[:,1], linestyle="--", linewidth=1.5, label="Original polygon")
    plt.scatter(orig[:-1,0], orig[:-1,1], s=25)

    # Clipped polygon (if any)
    if clipped_poly is not None and len(clipped_poly) > 0:
        clp = close_ring(np.array(clipped_poly, dtype=float))
        plt.plot(clp[:,0], clp[:,1], linewidth=3, label="Clipped polygon")
        plt.scatter(clp[:-1,0], clp[:-1,1], s=30)

    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("Sutherland–Hodgman Polygon Clipping")
    plt.grid(True, linewidth=0.4, alpha=0.5)
    plt.legend()
    plt.show()

# Driver code
if __name__ == "__main__":
    # Polygon vertices (clockwise or counter-clockwise)
    poly_points = np.array([[100, 150], [200, 250], [300, 200]], dtype=float)
    poly_size = len(poly_points)

    # Clipper polygon vertices (convex; order matters)
    # Example: square clipper
    clipper_points = np.array([[150, 150], [150, 200], [200, 200], [200, 150]], dtype=float)
    clipper_size = len(clipper_points)

    # Perform clipping
    clipped_points, clipped_size = suthHodgClip(poly_points, poly_size, clipper_points, clipper_size)

    # Print vertices of clipped polygon
    print("Clipped polygon vertices:")
    for i in range(clipped_size):
        x, y = clipped_points[i]
        print(f"({x:.2f}, {y:.2f})")

    # Plot
    plot_polygons(poly_points, clipper_points, clipped_points)
