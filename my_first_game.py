import pyxel

class Game:
    """This is our main game class"""
    
    def __init__(self):
        """This runs once when the game starts"""
        # Create a window that is 160 pixels wide and 120 pixels tall
        pyxel.init(160, 120, title="My First Game")
        
        # Starting position of our character
        self.x = 80  # middle of screen horizontally
        self.y = 60  # middle of screen vertically
        
        # Start the game - this will call update() and draw() repeatedly
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """This runs every frame to update the game"""
        # Check if player pressed arrow keys and move character
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x - 2  # Move left
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = self.x + 2  # Move right
        if pyxel.btn(pyxel.KEY_UP):
            self.y = self.y - 2  # Move up
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = self.y + 2  # Move down
    
    def draw(self):
        """This runs every frame to draw everything on screen"""
        # Clear the screen with color 0 (black)
        pyxel.cls(0)
        
        # Draw a circle at position (x, y) with radius 8 and color 11 (light blue)
        pyxel.circ(self.x, self.y, 8, 11)
        
        # Draw some text at the top
        pyxel.text(10, 10, "Use arrow keys to move!", 7)

# Start the game!
Game()

