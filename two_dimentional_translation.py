import matplotlib.pyplot as plt

def translate_line(P, T):
    """
    P: [[x1, y1], [x2, y2]]  (line endpoints)
    T: [tx, ty]              (translation vector)
    """
    # Original points
    (x1, y1), (x2, y2) = P[0][:], P[1][:]

    # Translated points
    x1_t, y1_t = x1 + T[0], y1 + T[1]
    x2_t, y2_t = x2 + T[0], y2 + T[1]

    # Plot
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.canvas.manager.set_window_title("Line Translation Visualization")

    # Original line
    ax.plot([x1, x2], [y1, y2], "-", linewidth=2, label="Original line")
    ax.scatter([x1, x2], [y1, y2], s=40)

    # Translated line
    ax.plot([x1_t, x2_t], [y1_t, y2_t], "--", linewidth=2, label="Translated line")
    ax.scatter([x1_t, x2_t], [y1_t, y2_t], s=40, marker="x")

    # Optional: show translation vector from original midpoint to translated midpoint
    mx, my = (x1 + x2)/2, (y1 + y2)/2
    mx_t, my_t = (x1_t + x2_t)/2, (y1_t + y2_t)/2
    ax.arrow(mx, my, mx_t - mx, my_t - my, length_includes_head=True, head_width=0.4, alpha=0.7, label="Translation vector")

    # Axes & aesthetics
    pad = 5
    all_x = [x1, x2, x1_t, x2_t]
    all_y = [y1, y2, y1_t, y2_t]
    ax.set_xlim(min(all_x) - pad, max(all_x) + pad)
    ax.set_ylim(min(all_y) - pad, max(all_y) + pad)

    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linewidth=0.5, alpha=0.6)
    ax.set_title("Line Translation", fontsize=14)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    P = [[5, 8], [12, 18]]  # coordinates of the line endpoints
    T = [2, 1]              # translation vector (tx, ty)
    translate_line(P, T)
