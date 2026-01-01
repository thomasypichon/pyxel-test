import pyxel

class World:
    """Background scenery and environment"""
    
    def __init__(self):
        """Set up world objects"""
        pass
    
    def draw(self):
        """Draw all background objects"""
        # Green circles (trees/landmarks)
        pyxel.circ(50, 50, 3, 3)
        pyxel.circ(100, 80, 3, 3)
        pyxel.circ(150, 30, 3, 11)
        
        # Gray road
        pyxel.rect(0, 90, 160, 10, 13)

