#!/usr/bin/env python3
"""Simple script to test mobile version with one click"""

import os
import subprocess
import time
import signal
import sys

def main():
    print("🎮 Preparing mobile test...")
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    game_file = os.path.join(script_dir, "my_first_game.py")
    temp_game_file = os.path.join(script_dir, "my_first_game_temp.py")
    
    # Read the game file and modify it to keep cursor visible
    print("\n📝 Creating test version with visible cursor...")
    with open(game_file, 'r') as f:
        game_code = f.read()
    
    # Add pyxel.mouse(True) call after pyxel.init
    # Look for the line after pyxel.init and add the mouse call
    if "pyxel.mouse(True)" not in game_code:
        # Find where we check for the environment variable
        if 'os.getenv("PYXEL_SHOW_CURSOR")' in game_code:
            # Replace the conditional with just the call
            game_code = game_code.replace(
                '        # Keep mouse cursor visible when testing mobile controls\n        # (Only when PYXEL_SHOW_CURSOR environment variable is set)\n        if os.getenv("PYXEL_SHOW_CURSOR") == "1":\n            pyxel.mouse(True)',
                '        # Keep mouse cursor visible for mobile testing\n        pyxel.mouse(True)'
            )
        else:
            # If the env check isn't there, add it after pyxel.init
            game_code = game_code.replace(
                'pyxel.init(160, 120, title="My First Game")',
                'pyxel.init(160, 120, title="My First Game")\n        pyxel.mouse(True)  # Keep cursor visible for testing'
            )
    
    # Write temporary game file
    with open(temp_game_file, 'w') as f:
        f.write(game_code)
    
    # Export to web using the temp file
    print("\n📦 Exporting game to web format...")
    try:
        # Activate venv and run pyxel commands
        subprocess.run(["bash", "-c", f"""
            source venv/bin/activate
            mkdir -p game_temp
            cp my_first_game_temp.py game_temp/my_first_game.py
            cd game_temp
            pyxel package . my_first_game.py
            cd ..
            mv game_temp/game_temp.pyxapp my_first_game.pyxapp
            rm -rf game_temp
            pyxel app2html my_first_game.pyxapp
            if [ -f "my_first_game.html" ]; then
                mv my_first_game.html index.html
                echo "✅ Done! The web version is saved as index.html"
            fi
        """], cwd=script_dir, check=True)
    finally:
        # Clean up temp file
        if os.path.exists(temp_game_file):
            os.remove(temp_game_file)
    
    # Kill any existing web servers on port 8000
    try:
        subprocess.run(["lsof", "-ti:8000"], capture_output=True, check=False)
        subprocess.run("lsof -ti:8000 | xargs kill -9", shell=True, capture_output=True, check=False)
    except:
        pass
    
    # Start web server
    print("\n🌐 Starting web server on port 8000...")
    server_process = subprocess.Popen(
        ["python3", "-m", "http.server", "8000"],
        cwd=script_dir
    )
    
    # Wait for server to start
    time.sleep(2)
    
    # Open browser
    subprocess.run(["open", "http://localhost:8000"])
    
    print("\n✅ Game is running at http://localhost:8000")
    print("\n📱 To see mobile controls:")
    print("   1. Press Cmd+Option+I (Firefox/Chrome)")
    print("   2. Press Cmd+Option+M for mobile mode (Firefox)")
    print("      OR click the phone icon (Chrome)")
    print("   3. Select iPad or iPhone")
    print("   4. Refresh the page")
    print("\nPress Ctrl+C to stop the server when done testing.")
    
    # Handle Ctrl+C gracefully
    def signal_handler(sig, frame):
        print("\n\n👋 Stopping server...")
        server_process.terminate()
        server_process.wait()
        print("Server stopped!")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    # Wait for server process
    try:
        server_process.wait()
    except KeyboardInterrupt:
        signal_handler(None, None)

if __name__ == "__main__":
    main()

