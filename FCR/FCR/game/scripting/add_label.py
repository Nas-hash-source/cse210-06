from constants import *
from game.casting.cast import Cast
from game.casting.label import Label
from game.casting.point import Point

class Add_Label():
    def __init__(self, cast):
        self._stats = cast.get_first_actor(STATS_GROUP)
    
    def execute(self, cast):
        self.add_lives_text(cast)

    def add_lives_text(self, cast):
        x = FIELD_LEFT
        y = CELL_SIZE
        lives_stat = self._stats.get_lives()
        lives_text = Label(f"Lives : {lives_stat}", Point(x,y))
        lives_text.set_font_size(FONT_SIZE)
        cast.add_actor(LABEL_GROUP, lives_text)
