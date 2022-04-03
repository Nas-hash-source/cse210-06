from constants import *
from game.casting.body import Body
from game.casting.image import Image
from game.scripting.add_obstacle import Add_Obstacle
from game.scripting.add_player import Add_Player
from game.scripting.add_label import Add_Label
from game.scripting.add_stats import Add_Stats
from game.scripting.action import Action

class Prepare_New_Game(Action):
    def __init__(self):
        pass
    def execute(self, cast):
        ADD_OBSTACLE = Add_Obstacle()
        ADD_PLAYER = Add_Player()
        ADD_STATS = Add_Stats()
        ADD_STATS.execute(cast)
        ADD_LABEL = Add_Label(cast)
        ADD_LABEL.execute(cast)
        ADD_OBSTACLE.execute(cast, START_X, STOP_X)
        ADD_PLAYER.execute(cast)
