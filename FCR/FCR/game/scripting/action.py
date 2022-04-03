class Action:
    """A thing that is done.
    
    The responsibility of action is to do something that is important in the game. Thus, it has one
    method, execute(), which should be overridden by derived classes.
    """

    def execute(self, cast):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast: An instance of Cast containing the actors in the game.
        """
        raise NotImplementedError("execute not implemented in base class")