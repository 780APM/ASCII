# 3D ASCII Cube Animation

A Python implementation of a 3D rotating cube rendered in ASCII characters, demonstrating fundamental concepts in computer graphics and mathematical visualization.

## 🔍 Technical Overview

This project showcases several key technical concepts and implementations:

### 3D Graphics Fundamentals
- Implementation of 3D to 2D projection mathematics
- Rotation matrix calculations for all three axes (X, Y, Z)
- Perspective projection with configurable field of view (FOV)
- Vector and point transformation in 3D space

### Computer Graphics Algorithms
- Bresenham's line algorithm for efficient line drawing
- Screen buffer management for frame rendering
- Point projection from 3D space to 2D screen coordinates
- Edge rendering with depth considerations

### Object-Oriented Programming
- Custom Point3D class implementation
- Encapsulation of 3D transformation methods
- Clean separation of concerns between rendering and geometry

### Mathematics Implementation
- Trigonometric calculations for rotation
- Matrix transformation operations
- Perspective projection mathematics
- Vector geometry and coordinate system transformations

### Performance Considerations
- Efficient screen buffer management
- Optimized line drawing algorithm
- Frame rate control for smooth animation
- Memory-efficient data structures

## 🛠 Technical Skills Demonstrated

- **Mathematical Modeling**: Implementation of 3D mathematical concepts
- **Algorithm Design**: Custom graphics rendering algorithms
- **Object-Oriented Design**: Clean, modular code architecture
- **Graphics Programming**: Basic 3D graphics pipeline implementation
- **Performance Optimization**: Efficient rendering techniques
- **Real-time Animation**: Frame-based animation system

## 🎮 Usage

```python
python spinning_cube.py
```

The animation will run until interrupted with Ctrl+C.

## ⚙️ Customization Parameters

```python
# Display settings
width = 30    # Screen width in characters
height = 15   # Screen height in characters

# 3D projection settings
cube_size = 3           # Size of the cube
fov = 50               # Field of view
viewer_distance = 10    # Distance from viewer to screen

# Animation settings
rotation_speed_x = 1.0  # Rotation speed around X axis
rotation_speed_y = 0.7  # Rotation speed around Y axis
rotation_speed_z = 0.5  # Rotation speed around Z axis
```

## 🔋 Requirements

- Python 3.x
- No external dependencies required

## 🎯 Future Improvements

- Color support for different cube faces
- Multiple shape support (pyramids, complex polyhedra)
- Depth shading for enhanced 3D effect
- Interactive controls for rotation and zoom
- Additional rendering characters for improved resolution

---
*This project demonstrates practical implementation of computer graphics concepts, mathematical modeling, and efficient algorithm design in Python.*
