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
        self.speed = 1
        self.direction = "right"  # Which way we're facing
        self.bullets = []  # List to store all bullets
        self.ammo = 200  # How many lasers you have left
        # Start the game - this will call update() and draw() repeatedly
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """This runs every frame to update the game"""
        # Check if player pressed arrow keys and move character
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.direction = "left"  # Remember we're facing left
            self.x = self.x - 2  #move left
            if self.x < 0:
                self.x = 160  # Went off left, appear on right
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.direction = "right"  # Remember we're facing right
            self.x = self.x + 2  # Move right
            if self.x > 160:
                self.x = 0  # Went off right, appear on left

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.direction = "up"  # Remember we're facing up
            self.y = self.y - 2  # Move up
            if self.y < 0:
                self.y = 120  # Went off top, appear on bottom   
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.direction = "down"  # Remember we're facing down
            self.y = self.y + 2  # Move down
            if self.y > 120:
                self.y = 0  # Went off bottom, appear on top
        # Check if mouse button is pressed
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.color = self.color + 1  # Add 1 to color
        if self.color==16 :
            self.color = 0
        
        # Shoot bullet on right click (only if you have ammo!)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and self.ammo > 0:
            bullet = {
                "x": self.x,
                "y": self.y,
                "direction": self.direction
            }
            self.bullets.append(bullet)
            self.ammo = self.ammo - 1  # Use up one laser
        
        # Update all bullets (move them)
        for bullet in self.bullets:
            if bullet["direction"] == "left":
                bullet["x"] = bullet["x"] - 3
            elif bullet["direction"] == "right":
                bullet["x"] = bullet["x"] + 3
            elif bullet["direction"] == "up":
                bullet["y"] = bullet["y"] - 3
            elif bullet["direction"] == "down":
                bullet["y"] = bullet["y"] + 3 
        
        # Remove bullets that went off screen
        self.bullets = [b for b in self.bullets if b["x"] > 0 and b["x"] < 160 and b["y"] > 0 and b["y"] < 120]



    
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
        
        # Draw all bullets
        for bullet in self.bullets:
            pyxel.circ(bullet["x"], bullet["y"], 2, 8)  # Small red circles
        
        # Draw some text at the top
        pyxel.text(10, 10, "derinmon, the game", 7)
        pyxel.text(10, 20, "Ammo: " + str(self.ammo), 7)  # Show how much ammo left


# Start the game!
Game()


