class Settings():

    def __init__(self):
        self.window_width = 400
        self.window_height = 400
        self.zNear = 0.1
        self.zFar = 10
        self.playerMoveSpeed = 0.025
        self.playerViewRadius = self.playerMoveSpeed
        self.playerAcceleration = 0.001
        self.playerHorizontalViewSpeed = 5
        self.playerVerticalViewSpeed = self.playerMoveSpeed/10
        
        self.resetMoveRadius()

    def resetMoveRadius(self):
        self.playerMoveRadius = 0