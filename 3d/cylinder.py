import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math

rotate_angle = 0

def draw_cylinder(radius, num_segments):

    def get_coordinates(segment):
        theta = 2.0 * math.pi * segment / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        return x, y

    gl.glBegin(gl.GL_POLYGON)

    # Top face
    gl.glColor3f(0.0, 0.0, 1.0)  # Blue
    for i in range(num_segments):
        x, y = get_coordinates(i)
        gl.glVertex3f(x, y, 0.5)

    gl.glEnd()
    gl.glBegin(gl.GL_POLYGON)

    # Bottom face
    gl.glColor3f(1.0, 1.0, 0.0)  # Yellow
    for i in range(num_segments):
        x, y = get_coordinates(i)
        gl.glVertex3f(x, y, -0.5)

    gl.glEnd()
    
    # Surface
    gl.glBegin(gl.GL_POLYGON)
    gl.glColor3f(1, 0, 1) # Green
    z = 0.5
    for i in range(num_segments):
        x, y = get_coordinates(i)
        gl.glVertex3f(x, y, z)
        gl.glVertex3f(x, y, -z)
        x, y = get_coordinates(i+1)
        gl.glVertex3f(x, y, -z)
        gl.glVertex3f(x, y, z)
        gl.glEnd()
        gl.glBegin(gl.GL_POLYGON)

    gl.glEnd()

def display():
    global rotate_angle
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -3.0)  # Move the cube back along the z-axis
    gl.glRotatef(rotate_angle, 1, 1, 1)  # Rotate the cube
    draw_cylinder(0.5, 8)
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
    glut.glutCreateWindow(b"3D Cylinder with PyOpenGL")
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutIdleFunc(idle)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
