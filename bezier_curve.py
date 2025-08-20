import math
import numpy as np
import matplotlib.pyplot as plt

def nCr(n, r):
    return math.comb(n, r)

def bernstein(n, k, u):
    return nCr(n, k) * (u**k) * ((1 - u)**(n - k))

def bezier_points(control_points, steps=10000):
    """
    control_points: list of (x, y)
    steps: number of samples between u in [0,1]
    returns: (xs, ys) of Bezier curve
    """
    pts = np.array(control_points, dtype=float)
    n = len(pts) - 1
    us = np.linspace(0.0, 1.0, steps)
    # Precompute all Bernstein basis values for efficiency
    B = np.stack([[bernstein(n, k, u) for k in range(n + 1)] for u in us], axis=0)  # [steps, n+1]
    curve = B @ pts  # matrix multiply -> [steps, 2]
    return curve[:, 0], curve[:, 1]

def plot_bezier(control_points, steps=10000):
    xs, ys = bezier_points(control_points, steps=steps)

    # Plot curve
    plt.figure(figsize=(7, 5))
    plt.plot(xs, ys, linewidth=2, label="Bezier curve")

    # Control polygon
    cx = [p[0] for p in control_points]
    cy = [p[1] for p in control_points]
    plt.plot(cx, cy, linestyle="--", linewidth=1.2, label="Control polygon")

    # Control points
    plt.scatter(cx, cy, s=50, zorder=3, label="Control points")

    plt.title("Bezier Curve (Bernstein polynomial)")
    plt.xlabel("x"); plt.ylabel("y")
    plt.grid(True, linewidth=0.5)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Control points
    control_pts = [(27, 243), (101, 47), (324, 197), (437, 23)]
    plot_bezier(control_pts, steps=10000)  # steps≈1/eps; 10000 ~ eps=0.0001
