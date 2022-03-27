from constants import *
from game.scripting.action import Action


class DrawBricksAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast):
        bricks1 = cast.get_actors(BRICK_GROUP1)
        bricks2 = cast.get_actors(BRICK_GROUP2)
        for brick in bricks1:
            body = brick.get_body()

            if brick.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = brick.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)

        for brick in bricks2:
            body = brick.get_body()

            if brick.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = brick.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)