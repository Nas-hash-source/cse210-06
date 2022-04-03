from constants import *
from game.casting.label import Label
from game.casting.point import Point
from game.scripting.action import Action


class Game_Over(Action):

    def __init__(self):
        pass
        
    def execute(self, cast):
        cast.clear_actors(BRICK_GROUP)
        x = int(SCREEN_WIDTH/3)
        y = int(SCREEN_HEIGHT/2)
        game_over = Label("GAME OVER", Point(x,y))
        game_over.set_font_size(FONT_SIZE)
        cast.add_actor(LABEL_GROUP, game_over)
