import math
import matplotlib.pyplot as plt

def rotate_polygon(points, angle_deg, xp, yp):
    """Rotate polygon (list of (x,y)) by angle_deg around pivot (xp, yp)."""
    rad = math.radians(angle_deg)
    c, s = math.cos(rad), math.sin(rad)
    rotated = []
    for x, y in points:
        x_shift, y_shift = x - xp, y - yp
        xr = xp + (x_shift * c) - (y_shift * s)
        yr = yp + (x_shift * s) + (y_shift * c)
        rotated.append((xr, yr))
    return rotated

def print_points(title, pts):
    print(title)
    for i, (x, y) in enumerate(pts, 1):
        print(f"  P{i} = ({x:.2f}, {y:.2f})")
    print()

def plot_polygons(orig, rotated, pivot, angle_deg):
    def close_ring(pts):
        return pts + [pts[0]] if pts and pts[0] != pts[-1] else pts

    o = close_ring(orig[:])
    r = close_ring(rotated[:])

    ox, oy = zip(*o)
    rx, ry = zip(*r)

    fig, ax = plt.subplots(figsize=(7, 6))
    fig.canvas.manager.set_window_title("Polygon Rotation Visualization")

    # Original (before rotation)
    ax.plot(ox, oy, "--", linewidth=2, label="Original polygon")
    ax.scatter(*zip(*orig), s=35)

    # Rotated
    ax.plot(rx, ry, "-", linewidth=3, label=f"Rotated ({angle_deg}°)")
    ax.scatter(*zip(*rotated), s=35, marker="x")

    # Pivot
    ax.scatter([pivot[0]], [pivot[1]], s=60, marker="D", label="Pivot")

    # View
    all_x = [*map(lambda p: p[0], orig), *map(lambda p: p[0], rotated), pivot[0]]
    all_y = [*map(lambda p: p[1], orig), *map(lambda p: p[1], rotated), pivot[1]]
    pad = 40
    ax.set_xlim(min(all_x) - pad, max(all_x) + pad)
    ax.set_ylim(min(all_y) - pad, max(all_y) + pad)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linewidth=0.5, alpha=0.6)
    ax.set_title("2D Polygon Rotation about a Pivot", fontsize=14)
    ax.set_xlabel("X"); ax.set_ylabel("Y")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    # Sample n = 4; points: (100,100) (100,200) (200,200) (200,100); angle=45; pivot=(200,200)
    points = [(100, 100), (100, 200), (200, 200), (200, 100)]
    angle_deg = 45
    pivot = (200, 200)

    # ---------- PROCESS ----------
    rotated = rotate_polygon(points, angle_deg, pivot[0], pivot[1])

    # ---------- OUTPUT PRINT ----------
    print_points("Original polygon vertices:", points)
    print_points(f"Rotated polygon vertices (angle={angle_deg}°, pivot={pivot}):", rotated)

    # ---------- PLOT ----------
    plot_polygons(points, rotated, pivot, angle_deg)
