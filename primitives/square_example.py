import OpenGL.GL as gl
import OpenGL.GLUT as glut

def draw_square():
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-0.5, -0.5)  # Bottom-left vertex
    gl.glVertex2f(0.5, -0.5)   # Bottom-right vertex
    gl.glVertex2f(0.5, 0.5)    # Top-right vertex
    gl.glVertex2f(-0.5, 0.5)   # Top-left vertex
    gl.glEnd()

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    draw_square()
    glut.glutSwapBuffers()

def reshape(width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-3, 3, -3, 3, -3, 3)
    gl.glMatrixMode(gl.GL_MODELVIEW)

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow(b"Square with PyOpenGL")
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
