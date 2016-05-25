# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill= 'blue')

w = 300

def create_lines_vasarely():
    for xyxy in range(w):
        if xyxy % 5 == 0:
            create_line(0, xyxy, xyxy, 300)
            create_line(xyxy, 0, 300, xyxy)

create_lines_vasarely()
canvas.pack()
mainloop()
