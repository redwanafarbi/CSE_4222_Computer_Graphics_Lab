# Python 3 program for Bresenham’s Line Generation with Plotting
import matplotlib.pyplot as plt

# Bresenham's Line Generation function
def bresenham(x1, y1, x2, y2):
    points = []
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)
    y = y1

    for x in range(x1, x2 + 1):
        points.append((x, y))
        slope_error_new += m_new

        if slope_error_new >= 0:
            y += 1
            slope_error_new -= 2 * (x2 - x1)

    return points

# Function to plot the line
def plot_line(points, x1, y1, x2, y2):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, color="blue", label="Bresenham Pixels")
    plt.plot([x1, x2], [y1, y2], linestyle="--", color="red", label="Ideal Line")
    plt.title("Bresenham's Line Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Driver code
if __name__ == '__main__':
    x1, y1 = 3, 2
    x2, y2 = 15, 5

    # Generate points using Bresenham's Algorithm
    points = bresenham(x1, y1, x2, y2)

    # Print the points
    print("Generated Points:")
    for p in points:
        print(p)

    # Plot the line
    plot_line(points, x1, y1, x2, y2)
