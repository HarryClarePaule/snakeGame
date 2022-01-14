from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=1, stretch_len=1)
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def reset(self) -> None:
        for seg in self.snake_segments:
            seg.goto(800, 800)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def grow_snake(self):
        self.add_segment(self.snake_segments[-1].position())

    def snake_move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg - 1].xcor()
            new_y = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.snake_segments[0].setheading(90)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.snake_segments[0].setheading(0)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.snake_segments[0].setheading(180)

    def go_down(self):
        if self.head.heading() != UP:
            self.snake_segments[0].setheading(270)