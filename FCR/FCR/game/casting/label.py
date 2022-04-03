from constants import *
from game.casting.actor import Actor
from game.casting.color import Color

class Label(Actor):
    """A label to be displayed."""
 
    def __init__(self, text, position, debug = False):
        """Constructs a new Label.
        
        Args:
            text: An instance of Text.
            position: An instance of Point.
        """
        super().__init__(debug)
        self._text = text
        self._position = position
        self._font_size = 0
        self._stats = 0
        self._color = DEFAULT_COLOR
        
    def get_position(self):
        """Gets the label's position.
        
        Returns:
            An instance of Point.
        """
        return self._position

    def get_color(self):
        """Gets the label's color.
        Returns:
            An instance of color
        """
        return self._color

    def get_text(self):
        """Gets the label's text.
        
        Returns:
            An instance of Text.
        """
        return self._text    

    def get_font_size(self):
        """Gets the font size of the text.
        
        Returns:
        An instance of font size
        """
        return self._font_size 

    def get_stats(self):
        """Gets the stats particularly for the lives labelling
        
        Returns:
        An instance of the stats
        """
        return self._stats 

    def set_color(self, color):
        """set the color of the text"""
        self._stats = stats

    def set_font_size(self, font_size):
        """set the font size of the text."""

        self._font_size  = font_size

    def set_stats(self, stats):
        """set the stats of the text"""
        self._stats = stats