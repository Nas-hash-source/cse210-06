from constants import *
from game.scripting.action import Action


class Initialize(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self):
        self._video_service.open_window()
        self._video_service.load_images("FCR/assets/images/")