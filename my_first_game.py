import pyxel
import os
from player import Player
from bullets import BulletManager
from npc import NPC
from quests import QuestSystem
from menus import MenuSystem
from world import World

class Game:
    """Main game coordinator - brings everything together"""
    
    def __init__(self):
        """Set up the game and create all systems"""
        pyxel.init(160, 120, title="My First Game", quit_key=pyxel.KEY_NONE)
        if os.getenv("PYXEL_SHOW_CURSOR") == "1":
            pyxel.mouse(True)
        
        self.game_state = "start_screen"
        self.player = Player()
        self.bullets = BulletManager()
        self.npc = NPC(120, 70, "Cheeseburger Fan")
        self.quests = QuestSystem()
        self.menus = MenuSystem()
        self.world = World()
        self.ammo = 0
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """Main game update - runs every frame"""
        pyxel.mouse(self.game_state != "playing")
        
        if self.game_state == "credits_screen":
            if self.menus.update_credits_screen() == "back":
                self.game_state = "start_screen"
            return
        
        if self.game_state == "start_screen":
            action = self.menus.update_start_screen()
            if action == "play":
                self.game_state = "playing"
            elif action == "credits":
                self.game_state = "credits_screen"
            elif action == "quit":
                pyxel.quit()
            return
        
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self.game_state = "start_screen"
            return
        
        if pyxel.btnp(pyxel.KEY_Q):
            self.quests.toggle_menu()
        
        self.player.update()
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and self.ammo > 0:
            self.bullets.shoot(self.player.x, self.player.y, self.player.direction)
            self.ammo = self.ammo - 1
        
        self.bullets.update()
        
        npc_result = self.npc.update(self.player.x, self.player.y)
        if npc_result == "reward":
            self.ammo = self.ammo + self.quests.complete_quest()
        
        if self.npc.quest_given and not self.quests.quest_active:
            self.quests.start_quest()
    
    def draw(self):
        """Main game draw - runs every frame"""
        pyxel.cls(0)
        
        if self.game_state == "start_screen":
            self.menus.draw_start_screen()
            return
        
        if self.game_state == "credits_screen":
            self.menus.draw_credits()
            return
        
        self.world.draw()
        self.player.draw()
        self.npc.draw()
        self.npc.draw_dialogue(self.player.x, self.player.y)
        self.bullets.draw()
        pyxel.text(10, 10, "derinmon, the game", 7)
        pyxel.text(10, 20, "Poke Bowls: " + str(self.ammo), 7)
        self.quests.draw_menu()

# Start the game!
Game()
