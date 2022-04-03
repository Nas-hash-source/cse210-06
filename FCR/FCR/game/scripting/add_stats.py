from constants import *
from game.casting.stats import Stats

class Add_Stats():
    def __init__(self):
        self._stats = Stats()
    
    def execute(self, cast):
        cast.add_actor(STATS_GROUP, self._stats)