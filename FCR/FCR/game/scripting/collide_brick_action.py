from constants import *
from game.scripting.action import Action
from game.scripting.add_label import Add_Label
from game.scripting.game_over import Game_Over
from game.scripting.add_player import Add_Player

class Collide_Brick_Action(Action):
    def __init__(self, physics_service):
        self._physics_service = physics_service
        
    def execute(self, cast):
        ADD_PLAYER = Add_Player()
        ADD_LABEL = Add_Label(cast)
        GAME_OVER = Game_Over()   
        player = cast.get_first_actor(PLAYER_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)

        for brick in bricks:
            player_body = player.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(player_body, brick_body):
                cast.clear_actors(PLAYER_GROUP)
                cast.clear_actors(LABEL_GROUP)
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
                ADD_LABEL.add_lives_text(cast)
                ADD_PLAYER.execute(cast)
                if stats.get_lives()==0:
                    GAME_OVER.execute(cast)
        