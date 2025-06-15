import turtle
import time
# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# Start following instructions
def parse_instruction(instruction):
    instruction = instruction.strip()

    if not instruction:  # Skip empty or whitespace-only lines
        return
    if instruction.startswith("Tourne"):
        _, direction, _, degrees, _ = instruction.split()
        degrees = int(degrees)
        if direction == "gauche":
            t.left(degrees)
        elif direction == "droite":
            t.right(degrees)
        else:
            raise ValueError("Invalid direction")
    elif instruction.startswith("Avance"):
        _, spaces, _ = instruction.split()
        spaces = int(spaces)
        t.forward(spaces)
    elif instruction.startswith("Recule"):
        _, spaces, _ = instruction.split()
        spaces = int(spaces)
        t.backward(spaces)
    else:
        raise ValueError("Invalid instruction")

with open("turtle", "r") as f:
    try:
        for line in f:
            parse_instruction(line)
    except:
        print("error")        
# End
t.hideturtle()
screen.mainloop()
