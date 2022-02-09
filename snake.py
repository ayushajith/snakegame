from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270  # CONSTANTS IN CASE WE WANT TO TWEAK THE GAME
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)   # Previous SNAKE dissappears from the screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:  # IF SNAKE HEAD IS GOING IN A DIRECTION IT CANNOT GO IN THE OPPOSITE DIRECTION
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # IF SNAKE HEAD IS GOING IN A DIRECTION IT CANNOT GO IN THE OPPOSITE DIRECTION
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # IF SNAKE HEAD IS GOING IN A DIRECTION IT CANNOT GO IN THE OPPOSITE DIRECTION
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # IF SNAKE HEAD IS GOING IN A DIRECTION IT CANNOT GO IN THE OPPOSITE DIRECTION
            self.segments[0].setheading(RIGHT)

    def move_snake(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            # start, stop, step, range function doesn't allow keyword arguments
            """Here we are updating the last snake block inside the segment to it's predecessor's position
            So essentially the range function is going from last seg -> 2nd last segment and so on
            So segments[seg_no - 1] starts from the last segment and we tap in to its x and y coordinate
            and then we just update the segment before that to go to the updated x and y coordinate
            WE ARE DOING THIS TO MOVE THE TURTLE BLOCKS IN A SINGLE FILE IN ALL DIRECTIONS WITHOUT AFFECTING 
            IT'S BASIC BEHAVIOUR"""
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)
