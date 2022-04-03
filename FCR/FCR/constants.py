import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Frog Crossy River"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
CELL_SIZE = 32
FONT_SIZE = 48

# SOUND

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
DEFAULT_COLOR = WHITE

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3


# PLAYER
PLAYER_GROUP = "player"
PLAYER_IMAGE = "FCR/assets/images/player.png"
PLAYER_WIDTH = 18
PLAYER_HEIGHT = 18
PLAYER_VELOCITY= 2


# OBSTACLES
BRICK_GROUP = "bricks"
BRICK_IMAGE = "FCR/assets/images/brick.png"
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_VELOCITY = 1

#The start_y and stop_y delimit the extent of the obstacles from the top to bottom
START_Y = 1
STOP_Y = 20
START_X = FIELD_LEFT
STOP_X = 13

# DIALOG
LABEL_GROUP = "dialogs"