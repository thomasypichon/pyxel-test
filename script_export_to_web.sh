#!/bin/bash
# Export Pyxel game to web format

echo "Exporting game (7 Python files) to web..."

# Activate virtual environment
source venv/bin/activate

# Create a temporary directory with all the game files
mkdir -p game_temp
cp my_first_game.py game_temp/
cp player.py game_temp/
cp bullets.py game_temp/
cp npc.py game_temp/
cp quests.py game_temp/
cp menus.py game_temp/
cp world.py game_temp/

# Package the game from the temp directory
# Note: The .pyxapp file will be named after the directory (game_temp.pyxapp)
cd game_temp
pyxel package . my_first_game.py
cd ..

# Move and rename the .pyxapp file
mv game_temp/game_temp.pyxapp my_first_game.pyxapp

# Clean up temp directory
rm -rf game_temp

# Convert to HTML
pyxel app2html my_first_game.pyxapp

# Rename to index.html so it loads at localhost:8000 with no path
if [ -f "my_first_game.html" ]; then
    mv my_first_game.html index.html
    echo ""
    echo "✅ Done! The web version is saved as index.html"
    echo ""
    echo "Now commit and push to deploy to GitHub Pages!"
else
    echo ""
    echo "❌ Error: Failed to create HTML file"
    echo "Check the output above for errors"
fi
