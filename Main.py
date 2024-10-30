import math
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def rotate_x(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
    
    def rotate_y(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
    
    def rotate_z(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

def project(point, width, height, fov, viewer_distance):
    factor = fov / (viewer_distance + point.z)
    x = point.x * factor + width / 2
    y = -point.y * factor + height / 2
    return int(x), int(y)

def create_cube(size):
    points = []
    s = size / 2
    # Front face
    points.append(Point3D(-s, -s, -s))
    points.append(Point3D(s, -s, -s))
    points.append(Point3D(s, s, -s))
    points.append(Point3D(-s, s, -s))
    # Back face
    points.append(Point3D(-s, -s, s))
    points.append(Point3D(s, -s, s))
    points.append(Point3D(s, s, s))
    points.append(Point3D(-s, s, s))
    return points

def draw_line(screen, x1, y1, x2, y2, char='█'):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    
    if dx > dy:
        err = dx / 2
        while x != x2:
            if 0 <= y < len(screen) and 0 <= x < len(screen[0]):
                screen[y][x] = char
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2
        while y != y2:
            if 0 <= y < len(screen) and 0 <= x < len(screen[0]):
                screen[y][x] = char
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    if 0 <= y < len(screen) and 0 <= x < len(screen[0]):
        screen[y][x] = char

def render_frame(points, width, height, fov, viewer_distance, angle_x, angle_y, angle_z):
    # Create empty screen buffer
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Define cube edges
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Front face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Back face
        (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
    ]
    
    # Project points
    projected = []
    for point in points:
        rotated = point.rotate_x(angle_x).rotate_y(angle_y).rotate_z(angle_z)
        x, y = project(rotated, width, height, fov, viewer_distance)
        projected.append((x, y))
    
    # Draw edges
    for edge in edges:
        draw_line(screen, 
                 projected[edge[0]][0], projected[edge[0]][1],
                 projected[edge[1]][0], projected[edge[1]][1],
                 '█')
    
    return '\n'.join([''.join(row) for row in screen])

def main():
    # Smaller dimensions for the display
    width = 30
    height = 15
    
    # Adjusted parameters for a smaller cube
    cube_size = 3
    fov = 50
    viewer_distance = 10
    
    points = create_cube(cube_size)
    angle_x = angle_y = angle_z = 0
    
    try:
        while True:
            clear_screen()
            # Slower rotation for better visibility
            angle_x += 1.0
            angle_y += 0.7
            angle_z += 0.5
            
            frame = render_frame(points, width, height, fov, viewer_distance,
                               angle_x, angle_y, angle_z)
            print(frame)
            
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAnimation stopped")

if __name__ == "__main__":
    main()