import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math

rotate_angle = 0

def draw_cube():
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

def display():
    global rotate_angle
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -3.0)  # Move the cube back along the z-axis
    gl.glRotatef(rotate_angle, 0, 1, 1)  # Rotate the cube
    draw_cube()
    glut.glutSwapBuffers()

def reshape(width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

def idle():
    global rotate_angle
    rotate_angle += 0.5
    if rotate_angle > 360:
        rotate_angle -= 360
    glut.glutPostRedisplay()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow(b"3D Cube with PyOpenGL")
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutIdleFunc(idle)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
