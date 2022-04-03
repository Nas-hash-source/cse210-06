import random
from constants import *
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.rectangle_actor import Rectangle_Actor


class Add_Obstacle(Rectangle_Actor):
    """This class is responsible for adding the obstacles including the lines of brick to cross"""
    def __init__(self):
        self._image = Image(BRICK_IMAGE)

    
    def execute(self, cast, start_x, stop_x):
        #the line of bricks will have the opposite velocities alternatively
        #start_x refers to the beginning of what sets a line of the brick, stop_x its end
        instrument_code = 0
        for y in range(START_Y, STOP_Y):
            if instrument_code%2 ==0:
                self._add_line_of_bricks(cast, start_x, stop_x, y, Point(BRICK_VELOCITY,0))
            else:
                self._add_line_of_bricks(cast, start_x, stop_x, y, Point(-BRICK_VELOCITY,0))
            instrument_code+=1

    def _add_brick(self, cast, position, velocity):
        size = Point(BRICK_WIDTH, BRICK_HEIGHT)           
        body = Body(position, size, velocity)
        brick = Rectangle_Actor(body, self._image)
        cast.add_actor(BRICK_GROUP, brick)

    def _add_line_of_bricks(self, cast, start_x, stop_x, brick_y, velocity):
        brick_gap1 = random.randint(start_x,stop_x)
        brick_gap2 = random.randint(start_x,stop_x)
        while brick_gap1 == brick_gap2:
            brick_gap2 = random.randint(start_x,stop_x)

        for i in range(start_x, stop_x, 1):
            if i == brick_gap1 or i==brick_gap2:
                continue
            x = FIELD_LEFT + i * BRICK_WIDTH
            y = FIELD_TOP + brick_y * BRICK_HEIGHT
            position = Point(x,y)
            self._add_brick(cast, position, velocity)
    




        
    