import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math

def draw_circle(radius, num_segments):
    gl.glBegin(gl.GL_POLYGON)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        gl.glVertex2f(x, y)
    gl.glEnd()

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    draw_circle(0.5, 100)
    glut.glutSwapBuffers()

def reshape(width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-1, 1, -1, 1, -1, 1)
    gl.glMatrixMode(gl.GL_MODELVIEW)

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow(b"Circle with PyOpenGL")
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
