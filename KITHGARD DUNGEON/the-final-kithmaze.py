loop:
    self.moveRight()
    self.moveUp()
    enemy = self.findNearestEnemy()
    self.attack(enemy);
    self.moveRight()
    self.moveDown()
    self.moveDown()
    self.moveUp()