from constants import *
from game.casting.point import Point
from game.casting.label import Label
from game.scripting.action import Action
from game.scripting.add_obstacle import Add_Obstacle
from game.scripting.collide_brick_action import Collide_Brick_Action
from game.scripting.control_player_action import Control_Player_Action
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService

physics_service = RaylibPhysicsService()
keyboard_service = RaylibKeyboardService()
COLLIDE_BRICK_ACTION = Collide_Brick_Action(physics_service) 
CONTROL_PLAYER_ACTION = Control_Player_Action(keyboard_service)
ADD_OBSTACLE = Add_Obstacle()

class Do_Update(Action): 
    def __init__(self):
        pass
        
    def execute(self, cast):
        bricks = cast.get_actors(BRICK_GROUP)
        brick_length = len(bricks)
        if brick_length < STOP_X*(STOP_Y - START_Y):
            instrument_code = 0
            for y in range(START_Y, STOP_Y):
                if instrument_code%2 ==0:
                    ADD_OBSTACLE._add_line_of_bricks(cast, -STOP_X - 1, START_X - 1, y, Point(BRICK_VELOCITY,0))
                else:
                    ADD_OBSTACLE._add_line_of_bricks(cast, STOP_X + 1, 1+STOP_X*2, y, Point(-BRICK_VELOCITY,0))
                instrument_code+=1 

        for brick in bricks:
            brick.get_body().move_next(FIELD_RIGHT, FIELD_BOTTOM)
            if brick.get_body().get_velocity().get_x() == BRICK_VELOCITY and brick.get_body().get_position().get_x() == FIELD_RIGHT:
                cast.remove_actor(BRICK_GROUP, brick)

            elif brick.get_body().get_velocity().get_x() == -BRICK_VELOCITY and brick.get_body().get_position().get_x() == -BRICK_WIDTH:
                cast.remove_actor(BRICK_GROUP, brick)

        self._move_player(cast)
        self._is_win(cast)
        
        COLLIDE_BRICK_ACTION.execute(cast)
    def _move_player(self, cast):
        CONTROL_PLAYER_ACTION.execute(cast)
        player = cast.get_first_actor(PLAYER_GROUP)
        player.get_body().move_next(FIELD_RIGHT, FIELD_BOTTOM)

    def _is_win(self, cast):
        player = cast.get_first_actor(PLAYER_GROUP)
        if player.get_body().get_position().get_y() == FIELD_TOP:
            cast.clear_actors(BRICK_GROUP)
            x = int(SCREEN_WIDTH/3)
            y = int(SCREEN_HEIGHT/2)
            win = Label("YOU WIN", Point(x,y))
            win.set_font_size(FONT_SIZE)
            cast.add_actor(LABEL_GROUP, win)



