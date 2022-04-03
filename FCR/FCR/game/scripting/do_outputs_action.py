from constants import *
from game.scripting.action import Action
from game.scripting.draw_rectangle_actor import Draw_Rectangle_Actor


class Do_Outputs_Action(Action): 
    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        DRAW_ACTION = Draw_Rectangle_Actor(self._video_service)
        self._video_service.clear_buffer()
        DRAW_ACTION.draw_texts(cast)
        DRAW_ACTION.draw_bricks(cast)
        DRAW_ACTION.draw_player(cast)
        self._video_service.flush_buffer()