from email.iterators import body_line_iterator
from game.casting.cast import Cast
from game.scripting.prepare_new_game import Prepare_New_Game
from game.scripting.initialize import Initialize
from game.scripting.do_outputs_action import Do_Outputs_Action
from game.scripting.do_update import Do_Update

class Director():
    """The person in charge of setting up the cast t for each scene."""
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
        PREPARE_NEW_GAME = Prepare_New_Game()
        INITIALIZE = Initialize(self._video_service)
        DO_UPDATE = Do_Update()
        DO_OUTPUT = Do_Outputs_Action(self._video_service)
        INITIALIZE.execute()
        PREPARE_NEW_GAME.execute(self._cast)

        while self._video_service.is_window_open():
            DO_UPDATE.execute(self._cast)
            DO_OUTPUT.execute(self._cast)
                                                    
        self._video_service.unload_images()
        self._video_service.close_window()


     