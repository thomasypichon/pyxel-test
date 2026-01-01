import pyxel

class MenuSystem:
    """Handles start screen, credits, and menu navigation"""
    
    def __init__(self):
        """Set up menu state"""
        self.selected_button = 0  # 0=PLAY, 1=CREDITS, 2=QUIT
    
    def update_start_screen(self):
        """Handle input on start screen, returns action to take"""
        mouse_x = pyxel.mouse_x
        mouse_y = pyxel.mouse_y
        
        # Mouse hover detection
        if 40 <= mouse_x <= 120 and 50 <= mouse_y <= 62:
            self.selected_button = 0
        elif 40 <= mouse_x <= 120 and 70 <= mouse_y <= 82:
            self.selected_button = 1
        elif 40 <= mouse_x <= 120 and 90 <= mouse_y <= 102:
            self.selected_button = 2
        
        # Arrow key navigation
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.selected_button = self.selected_button - 1
            if self.selected_button < 0:
                self.selected_button = 2
        
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.selected_button = self.selected_button + 1
            if self.selected_button > 2:
                self.selected_button = 0
        
        # Selection (keyboard or mouse)
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            if self.selected_button == 0:
                return "play"
            elif self.selected_button == 1:
                return "credits"
            elif self.selected_button == 2:
                return "quit"
        
        # Mouse clicks
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 40 <= mouse_x <= 120 and 50 <= mouse_y <= 62:
                return "play"
            elif 40 <= mouse_x <= 120 and 70 <= mouse_y <= 82:
                return "credits"
            elif 40 <= mouse_x <= 120 and 90 <= mouse_y <= 102:
                return "quit"
        
        return None
    
    def update_credits_screen(self):
        """Handle input on credits screen"""
        # Press SPACE or A to go back
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            return "back"
        
        # Click BACK button
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mouse_x = pyxel.mouse_x
            mouse_y = pyxel.mouse_y
            if 40 <= mouse_x <= 120 and 100 <= mouse_y <= 112:
                return "back"
        
        return None
    
    def draw_start_screen(self):
        """Draw the start menu"""
        pyxel.text(40, 25, "DERINMON", 10)
        pyxel.text(42, 33, "the game", 7)
        
        # Draw buttons
        buttons = [
            (0, 50, "PLAY", 70),
            (1, 70, "CREDITS", 62),
            (2, 90, "QUIT", 68)
        ]
        for btn_id, y, text, text_x in buttons:
            color = 11 if self.selected_button == btn_id else 5
            pyxel.rect(40, y, 80, 12, color)
            pyxel.text(text_x, y + 4, text, 0)
    
    def draw_credits(self):
        """Draw the credits screen"""
        pyxel.text(55, 20, "CREDITS", 10)
        pyxel.text(30, 40, "Game Dev:", 7)
        pyxel.text(30, 48, "Thomas Pichon", 11)
        pyxel.text(30, 60, "Art:", 7)
        pyxel.text(30, 68, "Abidin 'Derin' Balci", 11)
        pyxel.text(30, 80, "Extra Credits:", 7)
        pyxel.text(30, 88, "(coming soon!)", 6)
        
        # BACK button
        pyxel.rect(40, 100, 80, 12, 11)
        pyxel.text(68, 104, "BACK", 0)

