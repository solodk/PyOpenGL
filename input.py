import glfw

class Input():
    def __init__(self, game_instance):
        self.settings = game_instance.settings
        self.player = game_instance.player


    def key_callback(self, window, key, scancode, action, mods):
        #print(key) #DEBUG
        SPACE = b' '

        if key == glfw.KEY_W:
            if action == glfw.PRESS:
                self.player.moveForward = True
                print(f'Key {key} pressed') #debug
            elif action == glfw.RELEASE:
                self.player.moveForward = False
                print(f'Key {key} released') #debug
        elif key == glfw.KEY_S:
            if action == glfw.PRESS:
                self.player.moveBackward = True
                print(f'Key {key} pressed') #debug
            elif action == glfw.RELEASE:
                self.player.moveBackward = False
                print(f'Key {key} released') #debug
        elif key == glfw.KEY_A:
            if action == glfw.PRESS:
                self.player.moveLeftward = True
                print(f'Key {key} pressed') #debug
            elif action == glfw.RELEASE:
                self.player.moveLeftward = False
                print(f'Key {key} released') #debug
        elif key == glfw.KEY_D:
            if action == glfw.PRESS:
                self.player.moveRightward = True
                print(f'Key {key} pressed') #debug
            elif action == glfw.RELEASE:
                self.player.moveRightward = False
                print(f'Key {key} released') #debug
        elif key == glfw.KEY_UP:
            self.player.centerY += self.settings.playerVerticalViewSpeed
            print(f'Key {key} pressed') #debug
        elif key == glfw.KEY_DOWN:
            self.player.centerY -= self.settings.playerVerticalViewSpeed
            print(f'Key {key} pressed') #debug
        elif key == glfw.KEY_LEFT:
            self.player.horisontal_rotation -= self.settings.playerHorizontalViewSpeed
            self.player.centerRecalcFunc()
            print(f'Key {key} pressed') #debug
        elif key == glfw.KEY_RIGHT:
            self.player.horisontal_rotation += self.settings.playerHorizontalViewSpeed
            self.player.centerRecalcFunc()
            print(f'Key {key} pressed') #debug
        elif key == glfw.KEY_SPACE:
            self.player.eyeY += self.settings.playerMoveSpeed
            self.player.centerY += self.settings.playerMoveSpeed
            print(f'Key {key} pressed') #debug
        elif key == glfw.KEY_LEFT_SHIFT:
            self.player.eyeY -= self.settings.playerMoveSpeed
            self.player.centerY -= self.settings.playerMoveSpeed
            print(f'Key {key} pressed') #debug
        elif key == glfw.KEY_RIGHT_CONTROL:
            print(f'Player: {[self.player.eyeX, self.player.eyeY, self.player.eyeZ]}')
            print(f'Look at: {[self.player.centerX, self.player.centerY, self.player.centerZ]}')
            print(f'Horisontal rotation: {self.player.horisontal_rotation}')