from constants import *
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.rectangle_actor import Rectangle_Actor


class Add_Player(Rectangle_Actor):
    def __init__(self):
        self._image = Image(PLAYER_IMAGE)
    
    def execute(self, cast):
        x = int(SCREEN_WIDTH/2)
        y = SCREEN_HEIGHT - PLAYER_HEIGHT
        position = Point(x,y)
        size = Point(PLAYER_WIDTH, PLAYER_HEIGHT)           
        velocity = Point(0,0)
        body = Body(position, size, velocity)
        player = Rectangle_Actor(body, self._image)
        cast.add_actor(PLAYER_GROUP, player)