from constants import *
from game.casting.point import Point
from game.casting.rectangle import Rectangle


class Body:
    """A rigid body used for physics operations."""
    
    def __init__(self, position = Point(), size = Point(), velocity = Point()):
        """Constructs a new Body."""
        self._position = position
        self._size = size
        self._velocity = velocity
    
    def get_position(self):
        """Gets the body's position.
        
        Returns:
            An instance of Point containing the x and y coordinates.
        """
        return self._position

    def get_size(self):
        """Gets the body's size.
        
        Returns:
            An instance of Point containing the width and height.
        """
        return self._size

    def get_velocity(self):
        """Gets the body's velocity.
        
        Returns:
            An instance of Point containing the horizontal and vertical speed.
        """
        return self._velocity

    def get_rectangle(self):
        """Gets the rectangle enclosing the body.
        
        Returns:
            An instance of Rectangle.
        """
        return Rectangle(self._position, self._size)
        
    def set_position(self, position):
        """Sets the position to the given value.
        
        Args:
            position: An instance of Point.
        """
        self._position = position

    def set_size(self, size):
        """Sets the size to the given value.
        
        Args:
            size: An instance of Point.
        """
        self._size = size

    def set_velocity(self, velocity):
        """Sets the velocity to the given value.
        
        Args:
            velocity: An instance of Point.
        """
        self._velocity = velocity

    def move_next(self, MAX_X, MAX_Y):
        """Moves the actor to its next position according to its velocity. the actor cannot move
        from screen side to side
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = self._position.get_x() + self._velocity.get_x()
        y = self._position.get_y() + self._velocity.get_y()
        if y >= MAX_Y - PLAYER_HEIGHT:
            y = MAX_Y - PLAYER_HEIGHT

        self._position = Point(x, y)

    def move_left(self):
        """move the actor especially the player in the left"""
        velocity = Point(-PLAYER_VELOCITY, 0)
        self.set_velocity(velocity)
        
    def move_right(self):
        """move the actor especially the player in the right"""
        velocity = Point(PLAYER_VELOCITY, 0)
        self.set_velocity(velocity)

    def move_up(self):
        """move the actor especially the player up"""
        velocity = Point(0, -PLAYER_VELOCITY)
        self.set_velocity(velocity)
        
    def move_down(self):
        """move the actor especially the player down"""
        velocity = Point(0, PLAYER_VELOCITY)
        self.set_velocity(velocity)    
        
    def stop_moving(self):
        """Stops the actor (player) from moving."""
        velocity = Point(0, 0)
        self.set_velocity(velocity)