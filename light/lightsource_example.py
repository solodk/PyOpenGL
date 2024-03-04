import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from input import Input
from player import Player
from settings import Settings

class Game():
    # Light position
    light_pos = (1.0, 1.0, 1.0, 0.0)  # Last component 0 indicates it's a positional light

    # Cube position
    cube_pos = [0.0, 0.0, 0.0]
    camera_pos = [3.0, 3.0, 3.0]
    camera_lookat = [0.0, 0.0, 0.0]

    def __init__(self):
        self.settings = Settings()
        self.player = Player(self)
        self.player.eyeX = 3.0
        self.player.eyeY = 3.0
        self.player.eyeZ = 3.0
        #self.player.centerRecalcFunc()
        self.input = Input(self)

        light_pos = (1.0, 1.0, 1.0, 0.0)  # Last component 0 indicates it's a positional light


    def init(self):
        glEnable(GL_DEPTH_TEST)  # Enable depth testing
        glEnable(GL_LIGHTING)     # Enable lighting calculations
        glEnable(GL_LIGHT0)      # Enable light source 0

        # Set light position and properties
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_pos)  # Set light position
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))   # Set ambient light
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))   # Set diffuse light
        glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))  # Set specular light

    def draw_cube(self):
        # Draw a cube
        glPushMatrix()
        #glTranslatef(cube_pos[0], cube_pos[1], cube_pos[2])

        # Front face
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glEnd()

        # Back face
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, -1.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glEnd()

        # Top face
        glBegin(GL_QUADS)
        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glEnd()

        # Bottom face
        glBegin(GL_QUADS)
        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glEnd()

        # Right face
        glBegin(GL_QUADS)
        glNormal3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glEnd()

        # Left face
        glBegin(GL_QUADS)
        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glEnd()

        glPopMatrix()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(self.player.eyeX, self.player.eyeY, self.player.eyeZ,           # Eye position
                self.player.centerX, self.player.centerY, self.player.centerZ,        # Center position (looking at)
                0, 1, 0) 

        self.draw_cube()

        glFlush()
        glfw.swap_buffers(window)

    def reshape(self, window, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (width/height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def key_callback(window, key, scancode, action, mods):
        global camera_pos
        if key == glfw.KEY_UP and action == glfw.PRESS:
            camera_pos[2] += 0.1
        elif key == glfw.KEY_DOWN and action == glfw.PRESS:
            camera_pos[2] -= 0.1
        elif key == glfw.KEY_LEFT and action == glfw.PRESS:
            camera_pos[0] -= 0.1
        elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
            camera_pos[0] += 0.1

    def main(self):
        if not glfw.init():
            return

        width, height = 800, 600
        global window
        window = glfw.create_window(width, height, "PyOpenGL with GLFW Light Source", None, None)

        if not window:
            glfw.terminate()
            return

        glfw.make_context_current(window)
        self.init()
        glfw.set_window_size_callback(window, self.reshape)
        glfw.set_key_callback(window, self.input.key_callback)
        glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        glfw.set_cursor_pos_callback(window, self.input.mouse_callback)

        while not glfw.window_should_close(window):
            glfw.poll_events()
            self.player.update()
            self.display()

        glfw.terminate()

if __name__ == "__main__":
    game = Game()
    game.main()
