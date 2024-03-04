from OpenGL.GL import *
from settings import Settings

class Surface():
    def __init__(self):
        self.settings = Settings()
        self.color = self.settings.colors['Yellow']

    def draw(self):
        glBegin(GL_QUADS)

        glColor3f(*self.color)
        glVertex3f(-10, -0.5, -10)
        glVertex3f(10, -0.5, -10)
        glVertex3f(10, -0.5, 10)
        glVertex3f(-10, -0.5, 10)

        glEnd()
