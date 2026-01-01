import pyxel

class Player:
    """Player character that you control"""
    
    def __init__(self):
        """Set up the player at the starting position"""
        self.x = 80  # middle of screen horizontally
        self.y = 60  # middle of screen vertically
        self.color = 11  # light blue
        self.speed = 1
        self.direction = "right"  # Which way we're facing
    
    def update(self):
        """Handle player movement and controls"""
        # Check if player pressed arrow keys and move character
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.direction = "left"
            self.x = self.x - 2
            if self.x < 0:
                self.x = 160  # Screen wrap: appear on right
        
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.direction = "right"
            self.x = self.x + 2
            if self.x > 160:
                self.x = 0  # Screen wrap: appear on left
        
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.direction = "up"
            self.y = self.y - 2
            if self.y < 0:
                self.y = 120  # Screen wrap: appear on bottom
        
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.direction = "down"
            self.y = self.y + 2
            if self.y > 120:
                self.y = 0  # Screen wrap: appear on top
        
        # Left click changes color
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.color = self.color + 1
            if self.color == 16:
                self.color = 0
    
    def draw(self):
        """Draw the player on screen"""
        pyxel.circ(self.x, self.y, 5, self.color)

