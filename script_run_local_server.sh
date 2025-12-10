#!/bin/bash
# Run a local web server to test the game

echo "Starting local web server..."
echo ""
echo "🎮 Game is running at: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python -m http.server 8000
