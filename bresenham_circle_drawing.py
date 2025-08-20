import matplotlib.pyplot as plt

# Function to put pixels at 8 symmetric points
def draw_circle_points(xc, yc, x, y, points):
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ])

# Function to generate circle points using Bresenham's Algorithm
def circle_bres(xc, yc, r):
    points = []
    x = 0
    y = r
    d = 3 - 2 * r

    # Draw initial points
    draw_circle_points(xc, yc, x, y, points)

    # Loop until x <= y
    while y >= x:
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        x += 1
        draw_circle_points(xc, yc, x, y, points)

    # Remove duplicates (optional)
    points = list(set(points))
    return points

# Function to plot the circle
def plot_circle(points, xc, yc, r):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, color="red", s=10, label="Bresenham Pixels")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Bresenham's Circle (Center=({xc},{yc}), Radius={r})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

# Driver code
if __name__ == "__main__":
    xc, yc, r = 50, 50, 30

    # Generate circle points
    points = circle_bres(xc, yc, r)

    # Print generated points
    print("Generated Points:")
    for p in points:
        print(p)

    # Plot the circle
    plot_circle(points, xc, yc, r)
