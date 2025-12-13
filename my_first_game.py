import pyxel

class Game:
    """This is our main game class"""
    
    def __init__(self):
        """This runs once when the game starts"""
        # Create a window that is 160 pixels wide and 120 pixels tall
        pyxel.init(160, 120, title="My First Game")
        
        # Game state - what screen are we on?
        self.game_state = "start_screen"  # Can be "start_screen" or "playing"
        
        # Menu selection - which button is highlighted?
        self.selected_button = 0  # 0 = PLAY button, 1 = CREDITS button
        
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
        # If we're on the credits screen, check for button to go back
        if self.game_state == "credits_screen":
            # Press SPACE or A button to go back to start screen
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.game_state = "start_screen"  # Go back to menu!
            
            # Mouse click on BACK button (x: 50-110, y: 100-112)
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                mouse_x = pyxel.mouse_x
                mouse_y = pyxel.mouse_y
                if 50 <= mouse_x <= 110 and 100 <= mouse_y <= 112:
                    self.game_state = "start_screen"  # BACK clicked!
            
            return  # Don't do anything else on credits screen
        
        # If we're on the start screen, check for button to start game
        if self.game_state == "start_screen":
            # Mouse hover detection - check if mouse is over a button
            mouse_x = pyxel.mouse_x
            mouse_y = pyxel.mouse_y
            
            # Check if mouse is over PLAY button (x: 50-110, y: 50-62)
            if 50 <= mouse_x <= 110 and 50 <= mouse_y <= 62:
                self.selected_button = 0  # Highlight PLAY button
            # Check if mouse is over CREDITS button (x: 50-110, y: 70-82)
            elif 50 <= mouse_x <= 110 and 70 <= mouse_y <= 82:
                self.selected_button = 1  # Highlight CREDITS button
            
            # Use UP/DOWN arrows to move between menu buttons
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                self.selected_button = self.selected_button - 1  # Move up
                if self.selected_button < 0:
                    self.selected_button = 1  # Wrap to bottom button
            
            if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                self.selected_button = self.selected_button + 1  # Move down
                if self.selected_button > 1:
                    self.selected_button = 0  # Wrap to top button
            
            # Press SPACE or A button to select the highlighted button
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                if self.selected_button == 0:
                    self.game_state = "playing"  # PLAY button selected!
                elif self.selected_button == 1:
                    self.game_state = "credits_screen"  # CREDITS button selected!
            
            # Mouse click to select button
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                # Check if click is on PLAY button
                if 50 <= mouse_x <= 110 and 50 <= mouse_y <= 62:
                    self.game_state = "playing"  # PLAY clicked!
                # Check if click is on CREDITS button
                elif 50 <= mouse_x <= 110 and 70 <= mouse_y <= 82:
                    self.game_state = "credits_screen"  # CREDITS clicked!
            
            return  # Don't do anything else on start screen
        
        # If we get here, we're in "playing" mode
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
        
        # If we're on the start screen, show that instead
        if self.game_state == "start_screen":
            # Draw title
            pyxel.text(40, 25, "DERINMON", 10)
            pyxel.text(42, 33, "the game", 7)
            
            # Draw PLAY button (centered at y=50)
            play_color = 11 if self.selected_button == 0 else 5  # Light blue if selected, dark gray if not
            pyxel.rect(50, 50, 60, 12, play_color)  # Button background
            pyxel.text(70, 54, "PLAY", 0)  # Button text (black)
            
            # Draw CREDITS button (centered at y=70)
            credits_color = 11 if self.selected_button == 1 else 5  # Light blue if selected, dark gray if not
            pyxel.rect(50, 70, 60, 12, credits_color)  # Button background
            pyxel.text(62, 74, "CREDITS", 0)  # Button text (black)
            
            return  # Don't draw the game stuff
        
        # If we're on the credits screen, show that instead
        if self.game_state == "credits_screen":
            # Draw title
            pyxel.text(55, 20, "CREDITS", 10)
            
            # Draw contributors
            pyxel.text(30, 40, "Game Dev:", 7)
            pyxel.text(30, 48, "Thomas Pichon", 11)
            
            pyxel.text(30, 60, "Art:", 7)
            pyxel.text(30, 68, "Derin Balci", 11)
            
            pyxel.text(30, 80, "Extra Credits:", 7)
            pyxel.text(30, 88, "(coming soon!)", 6)
            
            # Draw BACK button
            pyxel.rect(50, 100, 60, 12, 11)  # Button background
            pyxel.text(68, 104, "BACK", 0)  # Button text
            
            return  # Don't draw the game stuff
        
        # If we get here, we're playing the game
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