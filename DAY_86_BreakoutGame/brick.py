from turtle import Turtle
import random


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        # Define starting coordinates for the grid
        self.start_x = -385
        self.start_y = 280
        # Define the number of rows and columns
        self.num_rows = 4
        self.num_columns = 16
        # Define brick spacing
        self.brick_width = 50
        self.brick_height = 20
        # Define color list for bricks
        self.color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        
        # List to store brick instances
        self.bricks_list = []

        # Create the grid of bricks
        self.create_bricks()

    def create_bricks(self):
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                brick = Turtle()
                brick.shape("square")
                brick.color(random.choice(self.color_list))
                brick.shapesize(stretch_wid=1, stretch_len=2.5)  # Adjusted size to make bricks larger
                brick.penup()

                # Calculate position for each brick
                x_pos = self.start_x + col * self.brick_width
                y_pos = self.start_y - row * self.brick_height
                brick.goto(x_pos, y_pos)

                # Add the brick to the list
                self.bricks_list.append(brick)

    # Function to remove a brick from the screen
    def remove_brick(self, brick):
        brick.goto(1000, 1000)
        self.bricks_list.remove(brick)
        del brick
