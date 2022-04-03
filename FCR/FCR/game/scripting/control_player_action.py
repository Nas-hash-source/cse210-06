from constants import *
from game.scripting.action import Action


class Control_Player_Action(Action):
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast):
        player = cast.get_first_actor(PLAYER_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            player.get_body().move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            player.get_body().move_right()  
        elif self._keyboard_service.is_key_down(UP): 
            player.get_body().move_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            player.get_body().move_down()
        else: 
            player.get_body().stop_moving()    