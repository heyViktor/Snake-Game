import turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.create()
        self.head = self.blocks[0]

    def create(self):
        for position in POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        block = turtle.Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)

        self.blocks.append(block)

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for segment in range(len(self.blocks) - 1, 0, -1):
            x_position = self.blocks[segment - 1].xcor()
            y_position = self.blocks[segment - 1].ycor()
            self.blocks[segment].goto(x_position, y_position)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for piece in self.blocks:
            piece.hideturtle()
        self.blocks.clear()
        self.create()
        self.head = self.blocks[0]
