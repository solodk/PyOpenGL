import OpenGL.GLUT as glut

class Keyboard():
    def __init__(self, game_instance):
        self.settings = game_instance.settings
        self.player = game_instance.player
        self.window = game_instance.window


    def keyboard_callback(self, key, x, y):
        #print(key) #DEBUG
        movement_keys = [b'w', b'W', b'a', b'A', b's', b'S', b'd', b'D']
        ESC = b'\x1b'
        SPACE = b' '

        if key == ESC:
            glut.glutDestroyWindow(self.window)
        elif key == b'w' or key == b'W':
            self.player.moveForward = True
            print('w') #DEBUG
        elif key == b's' or key == b'S':
            self.player.moveBackward = True
            print('s') #DEBUG
        elif key == b'a' or key == b'A':
            self.player.moveLeftward = True
            print('a') #DEBUG
        elif key == b'd' or key == b'D':
            self.player.moveRightward = True
            print('d') #DEBUG
        
    def special_key_callback(self, key, x, y):
        #print(key) #DEBUG
        SHIFT = 112
        UP = 101
        DOWN = 103
        RIGHT = 102
        LEFT = 100

        if key == UP:
            self.player.centerY += self.settings.playerVerticalViewSpeed
            print('UP') #DEBUG
        elif key == DOWN:
            self.player.centerY -= self.settings.playerVerticalViewSpeed
            print('DOWN') #DEBUG
        elif key == LEFT:
            #LookAt_xyz[0] += step
            self.player.horisontal_rotation -= self.settings.playerHorizontalViewSpeed
            self.player.centerRecalcFunc()
            print('LEFT') #DEBUG
        elif key == RIGHT:
            self.player.horisontal_rotation += self.settings.playerHorizontalViewSpeed
            self.player.centerRecalcFunc()
            print('RIGHT') #DEBUG
        elif key == SHIFT:
            self.player.eyeY -= self.settings.playerMoveSpeed
            self.player.centerY -= self.settings.playerMoveSpeed
            print('SHIFT') #DEBUG
        
        elif key == 115: #DEBUG
            print(f'Player: {[self.player.eyeX, self.player.eyeY, self.player.eyeZ]}')
            print(f'Look at: {[self.player.centerX, self.player.centerY, self.player.centerZ]}')
            print(f'Horisontal rotation: {self.player.horisontal_rotation}')

    def keyboard_release_callback(self, key, x, y):
        #print(key) #DEBUG
        ESC = b'\x1b'
        SPACE = b' '

        if key == b'w' or key == b'W':
            self.player.moveForward = False
            print('w RELEASE') #DEBUG
        elif key == b's' or key == b'S':
            self.player.moveBackward = False
            print('s RELEASE') #DEBUG
        elif key == b'a' or key == b'A':
            self.player.moveLeftward = False
            print('a RELEASE') #DEBUG
        elif key == b'd' or key == b'D':
            self.player.moveRightward = False
            print('d RELEASE') #DEBUG
        elif key == SPACE:

            print('SPACE')
            