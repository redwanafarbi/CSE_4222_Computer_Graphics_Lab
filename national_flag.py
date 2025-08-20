import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

def draw_flag():
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.canvas.manager.set_window_title("Bangladesh Flag (Matplotlib)")

    # ---- Flag body: green rectangle (same coords as C code) ----
    flag_rect = Rectangle((50, 50), 350 - 50, 230 - 50,
                          facecolor="green", edgecolor="green", linewidth=2)
    ax.add_patch(flag_rect)

    # ---- Red circle on the flag ----
    red_circle = Circle((195, 140), radius=60, facecolor="red", edgecolor="red", linewidth=2)
    ax.add_patch(red_circle)

    # ---- White pole (rectangle) ----
    pole_rect = Rectangle((40, 40), 50 - 40, 430 - 40,
                          facecolor="white", edgecolor="black", linewidth=1.5)
    ax.add_patch(pole_rect)

    # ---- View settings ----
    # Match a typical old BGI canvas; ensure everything is visible
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 480)
    ax.invert_yaxis()                    # match graphics.h coordinate system (y grows downward)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title("Bangladesh Flag", fontsize=14)

    plt.show()

if __name__ == "__main__":
    draw_flag()
