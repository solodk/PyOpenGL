from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

from settings import Settings
from player import Player
from input import Input
from cube import Cube
from surface import Surface

class Game():
    def __init__(self):
        self.settings = Settings()
        self.player = Player(self)
        self.input = Input(self)
        self.cube = Cube()
        self.surface = Surface()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(self.player.eyeX, self.player.eyeY, self.player.eyeZ,           # Eye position
                self.player.centerX, self.player.centerY, self.player.centerZ,        # Center position (looking at)
                0, 1, 0)                                                              # Up vector
        
        self.surface.draw()
        self.cube.draw()

        glfw.swap_buffers(self.window)

    def reshape(self, window, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = width / height
        gluPerspective(45, aspect_ratio, self.settings.zNear, self.settings.zFar)  # Set up perspective projection
        glMatrixMode(GL_MODELVIEW)
    
    def idle(self):
        self.player.update()
        glfw.post_empty_event()
    
    def init_light(self):
        glEnable(GL_LIGHTING)     # Enable lighting calculations
        glEnable(GL_LIGHT0)      # Enable light source 0

        # Set light position and properties
        light_pos = (1.0, 1.0, 1.0, 1.0)
        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)  # Set light position
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))   # Set ambient light
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))   # Set diffuse light
        glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))  # Set specular light

    def play(self):
        glfw.init()
        
        self.window = glfw.create_window(
            self.settings.window_width, 
            self.settings.window_height, 
            "3D Game with PyOpenGL", 
            None, 
            None)
        glfw.make_context_current(self.window)
        glfw.set_window_size_callback(self.window, self.reshape)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        self.init_light()

        glfw.set_key_callback(self.window, self.input.key_callback)
        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        glfw.set_cursor_pos_callback(self.window, self.input.mouse_callback)

        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.idle()
            self.display()