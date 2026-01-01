# Code Organization Guide

Your game is now split into **7 organized files**, each with a specific purpose!

## File Structure

### 1. **player.py** (50 lines)
Everything about the player character you control.
- Movement (arrow keys, gamepad)
- Direction tracking
- Color changing (left click)
- Screen wrapping
- Drawing the player

### 2. **bullets.py** (38 lines)
The shooting system for poke bowls.
- Creating bullets when you shoot
- Moving bullets in the right direction
- Removing bullets that go off screen
- Drawing bullets

### 3. **npc.py** (80 lines)
The friendly NPC character and dialogue system.
- NPC position and appearance
- Talking to the NPC (press SPACE when close)
- Dialogue box with different messages
- Quest interaction

### 4. **quests.py** (56 lines)
Quest tracking and the quest menu (press Q).
- Tracking which quests are active/complete
- Drawing the quest menu
- Handling quest rewards

### 5. **menus.py** (98 lines)
Start screen and credits screen.
- Main menu with PLAY/CREDITS/QUIT buttons
- Mouse and keyboard navigation
- Credits screen

### 6. **world.py** (19 lines)
Background scenery.
- Green circles (trees/landmarks)
- Gray road
- Any other background objects

### 7. **my_first_game.py** (93 lines)
Main coordinator that brings everything together.
- Initializes Pyxel
- Creates all the systems (player, bullets, NPCs, etc.)
- Main game loop
- Manages game state (menu vs playing)

## How It Works

```
my_first_game.py imports:
├── player.py
├── bullets.py
├── npc.py
├── quests.py
├── menus.py
└── world.py

Each file has a CLASS:
- Player
- BulletManager
- NPC
- QuestSystem
- MenuSystem
- World

Main game creates instances of each class and coordinates them!
```

## Benefits

1. **Easy to Find Things** - All NPC code is in npc.py!
2. **Easy to Add Features** - Want a new NPC? Just add to npc.py!
3. **Short Files** - No more scrolling through 300+ lines
4. **Professional** - This is how real games are organized
5. **Learn Classes** - Each file teaches you about object-oriented programming

## Running the Game

Just run the main file like before:
```bash
python my_first_game.py
```

All the other files are imported automatically!

## Adding New Features

**Want a new quest?** → Edit `quests.py`
**Want a new NPC?** → Edit `npc.py`
**Want to change player speed?** → Edit `player.py`
**Want new background objects?** → Edit `world.py`

Each file is focused on ONE thing, making it easy to work with!

