import pyxel

class QuestSystem:
    """Tracks quests and displays quest menu"""
    
    def __init__(self):
        """Set up quest tracking"""
        self.quest_active = False
        self.quest_complete = False
        self.menu_open = False
    
    def toggle_menu(self):
        """Open or close the quest menu"""
        self.menu_open = not self.menu_open
    
    def start_quest(self):
        """Mark quest as active"""
        self.quest_active = True
    
    def complete_quest(self):
        """Mark quest as complete and return reward"""
        if not self.quest_complete:
            self.quest_complete = True
            return 5  # Reward: 5 poke bowls
        return 0
    
    def draw_menu(self):
        """Draw the quest menu if it's open"""
        if not self.menu_open:
            return
        
        # Draw background box
        pyxel.rect(20, 20, 120, 80, 1)
        pyxel.rectb(20, 20, 120, 80, 7)
        
        # Title
        pyxel.text(55, 25, "QUEST MENU", 10)
        pyxel.text(50, 32, "Press Q to close", 6)
        
        # Quest info
        if not self.quest_active:
            pyxel.text(25, 45, "Quest:", 11)
            pyxel.text(25, 53, "Talk to the yellow", 7)
            pyxel.text(25, 61, "NPC", 7)
            pyxel.text(25, 73, "Reward: 5 Poke Bowls", 6)
        elif self.quest_active and not self.quest_complete:
            pyxel.text(25, 45, "Active Quest:", 11)
            pyxel.text(25, 53, "Talk to NPC Again", 7)
            pyxel.text(25, 65, "Reward:", 10)
            pyxel.text(25, 73, "5 Poke Bowls", 7)
        else:
            pyxel.text(25, 45, "Quest Complete!", 10)
            pyxel.text(25, 53, "You talked to", 7)
            pyxel.text(25, 61, "the NPC and got", 7)
            pyxel.text(25, 69, "5 poke bowls!", 11)

