import pyray
from game.services.keyboard_service import KeyboardService


class RaylibKeyboardService(KeyboardService):
    """A Raylib implementation of KeyboardService."""

    def __init__(self):
        self._keys = {}
        self._keys["left"] = pyray.KEY_LEFT
        self._keys["right"] = pyray.KEY_RIGHT
        self._keys["up"] = pyray.KEY_UP
        self._keys["down"] = pyray.KEY_DOWN
        self._keys["enter"] = pyray.KEY_ENTER
        self._keys["space"] = pyray.KEY_SPACE

    def is_key_down(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_down(raylib_key)
    
    def is_key_pressed(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_pressed(raylib_key)
    
    def is_key_released(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_released(raylib_key)
    
    def is_key_up(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_up(raylib_key)