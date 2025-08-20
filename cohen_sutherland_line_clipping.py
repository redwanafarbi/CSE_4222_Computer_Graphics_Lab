import matplotlib.pyplot as plt

# Clipping window
x_left, x_right = 120, 500
y_bottom, y_top = 100, 350

# Region codes
LEFT, RIGHT, BOTTOM, TOP = 1, 2, 4, 8

def region_code(x, y):
    code = 0
    if x > x_right:
        code |= RIGHT
    elif x < x_left:
        code |= LEFT
    if y > y_top:
        code |= TOP
    elif y < y_bottom:
        code |= BOTTOM
    return code

def cohen_sutherland(x1, y1, x2, y2):
    """
    Returns: (accepted: bool, x1, y1, x2, y2)
    If rejected, returns (False, None, None, None, None)
    """
    code1 = region_code(x1, y1)
    code2 = region_code(x2, y2)

    while True:
        # Trivially accepted
        if (code1 | code2) == 0:
            return True, x1, y1, x2, y2
        # Trivially rejected
        if (code1 & code2) != 0:
            return False, None, None, None, None

        # Choose an endpoint that is outside
        code_out = code1 if code1 != 0 else code2

        # Avoid division by zero
        dx = x2 - x1
        dy = y2 - y1

        if code_out & TOP:
            # y = y_top
            x = x1 + (dx / dy) * (y_top - y1) if dy != 0 else float("inf")
            y = y_top
        elif code_out & BOTTOM:
            # y = y_bottom
            x = x1 + (dx / dy) * (y_bottom - y1) if dy != 0 else float("-inf")
            y = y_bottom
        elif code_out & RIGHT:
            # x = x_right
            y = y1 + (dy / dx) * (x_right - x1) if dx != 0 else float("inf")
            x = x_right
        else:  # LEFT
            # x = x_left
            y = y1 + (dy / dx) * (x_left - x1) if dx != 0 else float("-inf")
            x = x_left

        # Replace the outside point with intersection and update code
        if code_out == code1:
            x1, y1 = x, y
            code1 = region_code(x1, y1)
        else:
            x2, y2 = x, y
            code2 = region_code(x2, y2)

def plot_demo():
    # Original line
    x1, y1 = 50, 200
    x2, y2 = 500, 400

    accepted, cx1, cy1, cx2, cy2 = cohen_sutherland(x1, y1, x2, y2)

    plt.figure(figsize=(7, 5))

    # Draw clipping window (rectangle)
    rect_x = [x_left, x_right, x_right, x_left, x_left]
    rect_y = [y_bottom, y_bottom, y_top, y_top, y_bottom]
    plt.plot(rect_x, rect_y, color="gold", linewidth=2, label="Clipping window")

    # Draw original line
    plt.plot([x1, x2], [y1, y2], color="tab:gray", linestyle="--", linewidth=2, label="Original line")

    # Draw clipped line if accepted
    if accepted:
        plt.plot([cx1, cx2], [cy1, cy2], color="white", linewidth=3, label="Clipped line")

    plt.gca().set_facecolor("#0f172a")  # dark background (optional)
    plt.title("Cohen–Sutherland Line Clipping")
    plt.xlabel("x"); plt.ylabel("y")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True, linewidth=0.4, alpha=0.4)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_demo()
