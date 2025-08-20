import matplotlib.pyplot as plt

def scale_polygon(points, sfx, sfy):
    """Scale polygon about origin by (sfx, sfy)."""
    return [(x * sfx, y * sfy) for (x, y) in points]

def print_points(title, pts):
    print(title)
    for i, (x, y) in enumerate(pts, 1):
        print(f"  P{i} = ({x}, {y})")
    print()

def plot_polygons(orig, scaled, sfx, sfy):
    def close_ring(pts):
        return pts + [pts[0]] if pts and pts[0] != pts[-1] else pts

    o = close_ring(orig[:])
    s = close_ring(scaled[:])

    ox, oy = zip(*o)
    sx, sy = zip(*s)

    plt.figure(figsize=(7, 6))
    plt.plot(ox, oy, "--", linewidth=2, label="Original polygon")
    plt.scatter(*zip(*orig), s=35)

    plt.plot(sx, sy, "-", linewidth=3, label=f"Scaled polygon (sfx={sfx}, sfy={sfy})")
    plt.scatter(*zip(*scaled), s=35, marker="x")

    # View settings
    all_x = [p[0] for p in orig] + [p[0] for p in scaled]
    all_y = [p[1] for p in orig] + [p[1] for p in scaled]
    pad = max(10, 0.1 * max(1, max(map(abs, all_x + all_y))))  # simple padding
    plt.xlim(min(all_x) - pad, max(all_x) + pad)
    plt.ylim(min(all_y) - pad, max(all_y) + pad)

    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True, linewidth=0.5, alpha=0.6)
    plt.title("Origin-based Polygon Scaling")
    plt.xlabel("X"); plt.ylabel("Y")
    plt.legend()
    plt.show()

if __name__ == "__main__":

    # Sample: n = 4; points: (100,100) (100,150) (150,150) (150,100); scale: (2,2)
    points = [(100, 100), (100, 150), (150, 150), (150, 100)]
    sfx, sfy = 2, 2

    # ---------- PROCESS ----------
    scaled = scale_polygon(points, sfx, sfy)

    # ---------- OUTPUT PRINT ----------
    print_points("Original polygon vertices:", points)
    print_points("Scaled polygon vertices:", scaled)

    # ---------- PLOT ----------
    plot_polygons(points, scaled, sfx, sfy)
