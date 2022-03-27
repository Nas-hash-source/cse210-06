
import random
from constants import *
from game.scripting.draw_bricks_action import DrawBricksAction
from game.casting.body import Body
from game.casting.brick import Brick
from game.casting.cast import Cast
from game.casting.image import Image
from game.casting.point import Point


class Director():
    """The person in charge of setting up the cast and script for each scene."""

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._cast = Cast()

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    def start_game(self):
        """Starts the game. Runs the main game loop."""
        self._prepare_new_game(self._cast)
        self._video_service.open_window()
        self._video_service.load_images("batter/assets/images/")
        x=0
        while self._video_service.is_window_open():
            self._process(self._cast)
            self.do_outputs(self._cast)
            if x%(13*BRICK_WIDTH) ==0:
                y = 1
                for r in range(1, FIELD_BOTTOM//BRICK_HEIGHT - 5):
                    if y%2 ==0:
                        self._add_line_of_bricks1(self._cast,-13,0, r)
                    else:
                        self._add_line_of_bricks2(self._cast,14,27, r)
                    y+=1
            x+=1        
                                
        self._video_service.unload_images()
        self._video_service.close_window()       

    def _prepare_new_game(self, cast):
        self._add_obstacles(cast)

    
    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _add_line_of_bricks1(self, cast, start, stop, r):
        blank1 = random.randint(start,stop)
        blank2 = random.randint(start,stop)
        for i in range(start, stop, 1):
            if i == blank1 or i==blank2:
                continue
            x = FIELD_LEFT + i * BRICK_WIDTH
            y = FIELD_TOP + r * BRICK_HEIGHT
            position = Point(x, y)
            size = Point(BRICK_WIDTH, BRICK_HEIGHT)           
            image = Image(BRICK_IMAGE)
            velocity = Point(1,0)
            body = Body(position, size, velocity)
            brick = Brick(body, image)
            cast.add_actor(BRICK_GROUP1, brick)

    def _add_line_of_bricks2(self, cast, start, stop, r):        
        blank1 = random.randint(start,stop)
        blank2 = random.randint(start,stop)
        for i in range(start, stop, 1):
            if i == blank1 or i==blank2:
                continue
            x = FIELD_LEFT + i * BRICK_WIDTH
            y = FIELD_TOP + r * BRICK_HEIGHT
            position = Point(x, y)
            size = Point(BRICK_WIDTH, BRICK_HEIGHT)           
            image = Image(BRICK_IMAGE)
            velocity = Point(-1,0)
            body = Body(position, size, velocity)
            brick = Brick(body, image)
            cast.add_actor(BRICK_GROUP2, brick)               
    
    def _add_obstacles(self, cast):
        start = 1
        stop = FIELD_BOTTOM//BRICK_HEIGHT - 5
        x = 1
        for r in range(start, stop):
            if x%2 ==0:
                self._add_line_of_bricks1(cast,0, 13, r)
            else:
                self._add_line_of_bricks2(cast,0, 13, r)
            x+=1

    def _process(self, cast):
        bricks1 = cast.get_actors(BRICK_GROUP1)
        bricks2 = cast.get_actors(BRICK_GROUP2)
        for brick in bricks1:
            brick.get_body().move_next(FIELD_RIGHT, FIELD_BOTTOM)
            if brick.get_body().get_position().get_x() == FIELD_RIGHT:
                cast.remove_actor(BRICK_GROUP1, brick)

        for brick in bricks2:
            brick.get_body().move_next(FIELD_RIGHT, FIELD_BOTTOM)
            if brick.get_body().get_position().get_x() == -BRICK_WIDTH:
                cast.remove_actor(BRICK_GROUP2, brick)
    
    def do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        DRAW_BRICKS_ACTION = DrawBricksAction(self._video_service)
        self._video_service.clear_buffer()
        DRAW_BRICKS_ACTION.execute(cast)
        self._video_service.flush_buffer()



     