# Thomas's Pyxel Game Project

## About This Project
This is a game project by Thomas and Derin!
- Thomas: Coding
- Derin: Artwork

## What is Pyxel?
Pyxel is a retro game engine for Python. It lets you make games that look like old-school video games!

## Getting Started

### Setup (Already Done! ✅)
- Virtual environment created
- Pyxel installed
- Cursor configured

### How to Run Your Game in Cursor

**Method 1: Use the Play Button (Easy!)** 🎮
1. Open `my_first_game.py`
2. Look for the play button (▶️) in the top-right corner
3. Click it and select "Run My Game"
4. Your game window will open!

**Method 2: Use the Terminal**
```bash
python my_first_game.py
```

### Controls
- Use arrow keys (←↑↓→) to move the blue circle
- The circle is your character!

## 🌐 Deploy to Web

Want to share your game on the internet? You can export it to run in a web browser!

### Export Your Game
```bash
./script_export_to_web.sh
```

This creates an `index.html` file that can run in any web browser.

### Deploy Online (Free!)

Your game is just a single `index.html` file, so it can be hosted on any static website service!

**Option 1: GitHub Pages (Recommended)**
1. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Add web version of game"
   git push origin main
   ```
2. Go to your repo on GitHub.com → **Settings** → **Pages** (in sidebar)
3. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/ (root)`
   - Click **Save**
4. Wait a few minutes, then visit: `https://[username].github.io/pyxel-test/`

**Other Options:**
- **Netlify** - Drag and drop the `index.html` file
- **Vercel** - Connect your GitHub repo for automatic deploys
- **Any static hosting** - Just upload `index.html`!

To update your live game: Edit `my_first_game.py`, run `./script_export_to_web.sh`, commit, and push!

## Auto-Save Setting
To set up auto-save in Cursor:
1. Go to Cursor Settings (Cmd + ,)
2. Search for "auto save"
3. Change "Auto Save" to "afterDelay"
4. Set "Auto Save Delay" to 1000 (that's 1 second)

## Disabling AI Autocomplete
AI autocomplete can be confusing when learning to code. Here's how to turn it off completely:

**The Only Method That Works:**
1. Press `Cmd + Shift + P` (Mac)
2. Type: `Disable Cursor Tab`
3. Hit Enter

This turns off Cursor's AI autocomplete so you can think through the code yourself!

## 📚 Learning Notes

The `notes/` folder contains short explanations of concepts you're learning!

- Each note explains one concept in simple terms
- Look back at notes when you need a refresher
- As you learn new things, new notes will be added
- Think of it as your personal programming reference book!

**Current Notes:**
- `01-what-is-a-class.md` - Understanding classes and objects

## Ideas for the Game
(Write down ideas here!)

