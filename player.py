import math

class Player():
    def __init__(self, game_instance):
        self.settings = game_instance.settings
        self.X = 0.0
        self.Y = 0.0
        self.Z = -3.0
        self.eyeX = 0.0
        self.eyeY = 0.0
        self.eyeZ = -3.0
        self.centerX = 0.0
        self.centerY = 0.0
        self.centerZ = 0.0
        self.vertical_rotation = 0
        self.horisontal_rotation = 0
        self.currentMoveSpeed = 0
        self.moveForward = False
        self.moveLeftward = False
        self.moveRightward = False
        self.moveBackward = False

        self.centerRecalcFunc()


    def centerRecalcFunc(self):
        self.centerX = self.settings.playerViewRadius * math.cos(
            math.radians(self.horisontal_rotation)) + self.eyeX
        self.centerZ = self.settings.playerViewRadius * math.sin(
            math.radians(self.horisontal_rotation)) + self.eyeZ
    
    def xyzRecalcFunc(self, direction):
        angle = direction + math.radians(self.horisontal_rotation)
        self.eyeX += self.settings.playerMoveRadius * math.cos(angle)
        self.eyeZ += self.settings.playerMoveRadius * math.sin(angle)

    def update(self):
        dx = 0
        dy = 0

        if self.moveForward:
            dx += 1
        if self.moveLeftward:
            dy -= 1
        if self.moveRightward:
            dy += 1
        if self.moveBackward:
            dx -= 1

        if dx or dy:
            angle = math.atan2(dy, dx)
            if self.settings.playerMoveRadius < self.settings.playerMoveSpeed:
                self.settings.playerMoveRadius += self.settings.playerAcceleration
            self.xyzRecalcFunc(angle)
            self.centerRecalcFunc()
        else:
            self.settings.resetMoveRadius()

    def jump(self):
        pass