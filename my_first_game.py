import pyxel

class Game:
    """This is our main game class"""
    
    def __init__(self):
        """This runs once when the game starts"""
        # Create a window that is 160 pixels wide and 120 pixels tall
        pyxel.init(160, 120, title="My First Game")
        
        # Starting position of our character
        self.x = 80  # middle of screen horizontally
        self.y = 60
        self.color = 11         
        # Start the game - this will call update() and draw() repeatedly
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """This runs every frame to update the game"""
        # Check if player pressed arrow keys and move character
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x - 2  #move lef
            if self.x < 0:
                self.x = 160  # Went off left, appear on right
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = self.x + 2  # Move right
            if self.x > 160:
                self.x = 0  # Went off right, appear on left        # Wrap around screen edges

        if pyxel.btn(pyxel.KEY_UP):
            self.y = self.y - 2  # Move  # Went off left, appear on right
            if self.y < 0:
                self.y = 120  # Went off top, appear on bottom   
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = self.y + 2  # Move down
            if self.y > 120:
                self.y = 0  # Went off bottom, appear on top
                    # Check if mouse button is pressed
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.color = self.color + 1  # Add 1 to color
        if self.color==16 :
            self.color = 0

        
        


    
    def draw(self):
        """This runs every frame to draw everything on screen"""
        # Clear the screen with color 0 (black)
        pyxel.cls(0)
        pyxel.circ(50, 50, 3, 3)    # A green circle
        pyxel.circ(100, 80, 3, 3)   # Another green circle
        pyxel.circ(150, 30, 3, 11)
                # Draw a road
        pyxel.rect(0, 90, 160, 10, 13)  # A gray road

        

        # Draw a circle at position (x, y) with radius 8 and color 11 (light blue)
        pyxel.circ(self.x, self.y, 5, self.color)
        
        # Draw some text at the top
        pyxel.text(10, 10, "Herro!", 7)


# Start the game!
Game()


