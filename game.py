import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

from settings import Settings
from player import Player
from keyboard import Keyboard

class Game():
    def __init__(self):
        self.settings = Settings()
        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(self.settings.window_width, self.settings.window_height)
        self.window = glut.glutCreateWindow(b"Procedural 3D Game with PyOpenGL")
        self.player = Player(self)
        self.keyboard = Keyboard(self)

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
        glut.glutSwapBuffers()

    def reshape(self, width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        aspect_ratio = width / height
        glu.gluPerspective(45, aspect_ratio, self.settings.zNear, self.settings.zFar)  # Set up perspective projection
        gl.glMatrixMode(gl.GL_MODELVIEW)
    
    def idle(self):
        self.player.update()
        glut.glutPostRedisplay() # Request a redraw to continuously update the display
    
    def play(self):        
        # Movement
        glut.glutIgnoreKeyRepeat(True)
        glut.glutKeyboardFunc(self.keyboard.keyboard_callback)
        glut.glutKeyboardUpFunc(self.keyboard.keyboard_release_callback) #not done
        glut.glutSpecialFunc(self.keyboard.special_key_callback)
        #glut.glutSpecialFunc(self.keyboard.special_key_release_callback) #not done
        #glutMouseFunc(mouse_callback) #not done
        #glutMotionFunc(motion_callback) #not done
        

        gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        gl.glEnable(gl.GL_DEPTH_TEST)
        glut.glutDisplayFunc(self.display)
        glut.glutReshapeFunc(self.reshape)
        glut.glutIdleFunc(self.idle) #shoud i keep this?
        glut.glutMainLoop()