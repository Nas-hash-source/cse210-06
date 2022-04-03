from constants import *
from game.scripting.action import Action


class Draw_Rectangle_Actor(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def draw_texts(self, cast):
        texts = cast.get_actors(LABEL_GROUP)
        for text in texts:
            self._video_service.draw_text(text)

    def draw_bricks(self, cast):
        bricks = cast.get_actors(BRICK_GROUP)
        for brick in bricks:
            body = brick.get_body()

            if brick.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = brick.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)

    def draw_player(self, cast):
        player = cast.get_first_actor(PLAYER_GROUP)
        body = player.get_body()
        if player.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
                
        image = player.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)