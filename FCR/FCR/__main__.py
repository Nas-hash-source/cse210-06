from constants import *
from game.directing.director import Director
from game.services.raylib.raylib_video_service import RaylibVideoService


def main():
    video_service = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    director = Director(video_service)
    director.start_game()

if __name__ == "__main__":
    main()