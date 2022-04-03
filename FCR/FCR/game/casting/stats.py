from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._lives = DEFAULT_LIVES

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._lives = DEFAULT_LIVES