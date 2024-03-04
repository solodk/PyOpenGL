class Settings():

    def __init__(self):
        self.window_width = 400
        self.window_height = 400
        self.zNear = 0.1
        self.zFar = 10
        self.playerMoveSpeed = 0.1
        self.playerViewRadius = self.playerMoveSpeed
        self.playerAcceleration = 0.001
        self.playerHorizontalViewSpeed = 5
        self.playerVerticalViewSpeed = self.playerMoveSpeed/10
        self.mouseHorizontalSpeed = 0.1
        self.mouseVerticalSpeed = -self.mouseHorizontalSpeed/1000
        self.colors = {
            'Red':(1.0, 0.0, 0.0),
            'Green':(0.0, 1.0, 0.0),
            'Blue':(0.0, 0.0, 1.0),
            'Yellow':(1.0, 1.0, 0.0),
            'Magenta':(1.0, 0.0, 1.0),
            'Cyan':(0.0, 1.0, 1.0),
        }
        
        self.resetMoveRadius()

    def resetMoveRadius(self):
        self.playerMoveRadius = 0