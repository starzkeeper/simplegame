import random

from tkinter import Tk, Canvas, Label


window = Tk()
window.geometry("400x400")
window.title("Simple Game")


canvas = Canvas(window, width=400, height=400)
canvas.pack()

score_label = Label(window, text="Score: 0")
score_label.pack()


score = 0


def random_position():
    x = random.randint(25, 375)
    y = random.randint(25, 375)
    return x, y



def create_circle():
    x, y = random_position()

    canvas.create_oval(x, y, x + 50, y + 50, fill="green")



def move_circle(event):
    x, y = event.x, event.y
    items = canvas.find_overlapping(x - 25, y - 25, x + 25, y + 25)
    if len(items) > 0:
        global score
        score += 1

        score_label.config(text=f"Score: {score}")

        canvas.delete(items[0])

        create_circle()



canvas.bind("<Button-1>", move_circle)


create_circle()


window.mainloop()
