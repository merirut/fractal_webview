from flask import Flask, render_template
import math

flask_app = Flask(__name__)

def apply_rules(ch):
    if ch == 'A':
        return 'A-B--B+A++AA+B-'
    elif ch == 'B':
        return '+A-BB--B-A++A+B'
    else:
        return ch

def generate_gosper(axiom, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(apply_rules(c) for c in result)
    return result

def draw_gosper(instructions, length, angle, start_x, start_y):
    x, y = start_x, start_y
    direction = 90
    lines = []

    for command in instructions:
        if command == 'A' or command == 'B':
            new_x = x + length * math.cos(math.radians(direction))
            new_y = y + length * math.sin(math.radians(direction))
            lines.append(((x, y), (new_x, new_y)))
            x, y = new_x, new_y
        elif command == '+':
            direction -= angle
        elif command == '-':
            direction += angle

    return lines

@flask_app.route('/')
def index():
    axiom = 'A'
    iterations = 4
    length = 10
    angle = 60
    start_x = 650
    start_y = 450

    instructions = generate_gosper(axiom, iterations)
    lines = draw_gosper(instructions, length, angle, start_x, start_y)

    return render_template('index.html', lines=lines)
