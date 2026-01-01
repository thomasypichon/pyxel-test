import pyxel

class BulletManager:
    """Manages all bullets (poke bowls) flying around"""
    
    def __init__(self):
        """Set up empty bullet list"""
        self.bullets = []
    
    def shoot(self, x, y, direction):
        """Create a new bullet at the given position"""
        bullet = {
            "x": x,
            "y": y,
            "direction": direction
        }
        self.bullets.append(bullet)
    
    def update(self):
        """Move all bullets"""
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
        """Draw all bullets on screen"""
        for bullet in self.bullets:
            pyxel.circ(bullet["x"], bullet["y"], 2, 8)  # Small red circles

