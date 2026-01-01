import pyxel

class NPC:
    """A friendly NPC character that can talk and give quests"""
    
    def __init__(self, x, y, name):
        """Create an NPC at the given position"""
        self.x = x
        self.y = y
        self.name = name
        self.showing_dialogue = False
        self.quest_given = False
        self.quest_complete = False
    
    def update(self, player_x, player_y):
        """Check if player is near and wants to talk"""
        # Calculate distance to player
        distance_x = abs(player_x - self.x)
        distance_y = abs(player_y - self.y)
        
        # If player is close (within 20 pixels)
        if distance_x < 20 and distance_y < 20:
            # Check if they press spacebar to talk
            if pyxel.btnp(pyxel.KEY_SPACE):
                if not self.quest_given and not self.quest_complete:
                    # First interaction
                    if not self.showing_dialogue:
                        self.showing_dialogue = True
                    else:
                        self.showing_dialogue = False
                        self.quest_given = True
                elif self.quest_given and not self.quest_complete:
                    # Second interaction - complete quest
                    self.quest_complete = True
                    self.showing_dialogue = True
                    return "reward"  # Signal to give reward
                else:
                    # After quest done
                    self.showing_dialogue = not self.showing_dialogue
        else:
            # Player walked away
            if self.showing_dialogue and not self.quest_given:
                self.quest_given = True
            self.showing_dialogue = False
        
        return None
    
    def draw(self):
        """Draw the NPC and dialogue"""
        # Draw NPC as yellow circle
        pyxel.circ(self.x, self.y, 5, 10)
        
        # Show indicator if player is close
        # (This is handled in the game's draw method for distance check)
    
    def draw_dialogue(self, player_x, player_y):
        """Draw dialogue box if showing"""
        # Check distance for indicator
        distance_x = abs(player_x - self.x)
        distance_y = abs(player_y - self.y)
        
        if distance_x < 20 and distance_y < 20:
            pyxel.text(self.x - 2, self.y - 15, "!", 11)
        
        if self.showing_dialogue:
            # Draw dialogue box
            pyxel.rect(10, 95, 140, 20, 5)
            pyxel.rectb(10, 95, 140, 20, 7)
            
            # Show different text based on quest status
            if self.quest_given and not self.quest_complete:
                pyxel.text(15, 100, "Here's 5 poke bowls!", 10)
                pyxel.text(15, 107, "Quest complete!", 11)
            elif self.quest_complete:
                pyxel.text(15, 100, "Thanks for talking", 7)
                pyxel.text(15, 107, "to me earlier!", 7)
            else:
                pyxel.text(15, 100, "can i haz a", 7)
                pyxel.text(15, 107, "chezbugers pleaz?", 7)

