import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import glfw

from settings import Settings
from player import Player
from input import Input

class Game():
    def __init__(self):
        self.settings = Settings()
        self.player = Player(self)
        self.input = Input(self)

    def draw_surface(self):
        gl.glBegin(gl.GL_QUADS)

        gl.glColor3f(1.0, 1.0, 0.0)  # Yellow
        gl.glVertex3f(-100, 0, -100)
        gl.glVertex3f(100, 0, -100)
        gl.glVertex3f(100, 0, 100)
        gl.glVertex3f(-100, 0, 100)

        gl.glEnd()

    def draw_cube(self):
        gl.glBegin(gl.GL_QUADS)

        # Front face
        gl.glColor3f(1.0, 0.0, 0.0)  # Red
        gl.glVertex3f(-0.5, -0.5, 0.5)
        gl.glVertex3f(0.5, -0.5, 0.5)
        gl.glVertex3f(0.5, 0.5, 0.5)
        gl.glVertex3f(-0.5, 0.5, 0.5)

        # Back face
        gl.glColor3f(0.0, 1.0, 0.0)  # Green
        gl.glVertex3f(-0.5, -0.5, -0.5)
        gl.glVertex3f(-0.5, 0.5, -0.5)
        gl.glVertex3f(0.5, 0.5, -0.5)
        gl.glVertex3f(0.5, -0.5, -0.5)

        # Top face
        gl.glColor3f(0.0, 0.0, 1.0)  # Blue
        gl.glVertex3f(-0.5, 0.5, -0.5)
        gl.glVertex3f(-0.5, 0.5, 0.5)
        gl.glVertex3f(0.5, 0.5, 0.5)
        gl.glVertex3f(0.5, 0.5, -0.5)

        # Bottom face
        gl.glColor3f(1.0, 1.0, 0.0)  # Yellow
        gl.glVertex3f(-0.5, -0.5, -0.5)
        gl.glVertex3f(0.5, -0.5, -0.5)
        gl.glVertex3f(0.5, -0.5, 0.5)
        gl.glVertex3f(-0.5, -0.5, 0.5)

        # Right face
        gl.glColor3f(1.0, 0.0, 1.0)  # Magenta
        gl.glVertex3f(0.5, -0.5, -0.5)
        gl.glVertex3f(0.5, 0.5, -0.5)
        gl.glVertex3f(0.5, 0.5, 0.5)
        gl.glVertex3f(0.5, -0.5, 0.5)

        # Left face
        gl.glColor3f(0.0, 1.0, 1.0)  # Cyan
        gl.glVertex3f(-0.5, -0.5, -0.5)
        gl.glVertex3f(-0.5, -0.5, 0.5)
        gl.glVertex3f(-0.5, 0.5, 0.5)
        gl.glVertex3f(-0.5, 0.5, -0.5)

        gl.glEnd()

    def display(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()
        glu.gluLookAt(self.player.eyeX, self.player.eyeY, self.player.eyeZ,           # Eye position
                self.player.centerX, self.player.centerY, self.player.centerZ,        # Center position (looking at)
                0, 1, 0)                                                              # Up vector
        gl.glTranslatef(0.0, 0.0, -3.0)  # Move the cube back along the z-axis
        self.draw_cube()
        glfw.swap_buffers(self.window)

    def reshape(self, window, width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        aspect_ratio = width / height
        glu.gluPerspective(45, aspect_ratio, self.settings.zNear, self.settings.zFar)  # Set up perspective projection
        gl.glMatrixMode(gl.GL_MODELVIEW)
    
    def idle(self):
        self.player.update()
        glfw.post_empty_event()
    
    def play(self):
        glfw.init()
        self.window = glfw.create_window(
            self.settings.window_width, 
            self.settings.window_height, 
            "Procedural 3D Game with PyOpenGL", 
            None, 
            None)
        glfw.make_context_current(self.window)
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        gl.glEnable(gl.GL_DEPTH_TEST)
        glfw.set_key_callback(self.window, self.input.key_callback)
        glfw.set_window_size_callback(self.window, self.reshape)
        while not glfw.window_should_close(self.window):
            self.idle()
            glfw.poll_events()
            self.display()