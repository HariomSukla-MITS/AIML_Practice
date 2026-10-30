import tkinter as tk
import time
import math

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

center_x = 150
center_y = 150
radius = 120

def draw_clock():
    canvas.delete("all")

    # Draw clock face
    canvas.create_oval(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        outline="black", width=3
    )

    # Draw numbers
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = center_x + 95 * math.cos(angle)
        y = center_y + 95 * math.sin(angle)

        canvas.create_text(
            x, y, text=str(i), font=("Arial", 12, "bold")
        )

    # Get current time
    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate hand angles
    hour_angle = math.radians(
        (hour + minute / 60) * 30 - 90
    )
    minute_angle = math.radians(
        (minute + second / 60) * 6 - 90
    )
    second_angle = math.radians(second * 6 - 90)

    # Draw hour hand
    canvas.create_line(
        center_x, center_y,
        center_x + 50 * math.cos(hour_angle),
        center_y + 50 * math.sin(hour_angle),
        width=5
    )

    # Draw minute hand
    canvas.create_line(
        center_x, center_y,
        center_x + 75 * math.cos(minute_angle),
        center_y + 75 * math.sin(minute_angle),
        width=3
    )

    # Draw second hand
    canvas.create_line(
        center_x, center_y,
        center_x + 90 * math.cos(second_angle),
        center_y + 90 * math.sin(second_angle),
        fill="red", width=1
    )

    # Draw center point
    canvas.create_oval(
        center_x - 4, center_y - 4,
        center_x + 4, center_y + 4,
        fill="black"
    )

    root.after(1000, draw_clock)

draw_clock()
root.mainloop()