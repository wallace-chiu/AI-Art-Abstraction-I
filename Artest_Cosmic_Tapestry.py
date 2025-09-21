import numpy as np
from PIL import Image, ImageDraw
import random

# Set the image dimensions
WIDTH, HEIGHT = 1920, 1080

# Create a new image with black background
img = Image.new('RGB', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

# Function to draw complex shapes with randomized size, color and position
def complex_shape(x, y):
    # Randomize fill color
    colors = [(random.randint(100, 150), random.randint(50, 100), 80),
              (random.randint(120, 180), random.randint(60, 140), 110)]
    draw_color = tuple(colors[random.randint(0, len(colors)-1)])

    # Randomize shape parameters
    radius = random.uniform(10, 50)
    num_points = int(random.uniform(5, 20))
    points = []
    for i in range(num_points):
        angle = 2 * np.pi * random.random()
        distance_from_center = radius + (random.random() - 0.5) * 100
        points.append((x + int(np.round(np.cos(angle) * distance_from_center)),
                        y + int(np.round(np.sin(angle) * distance_from_center))))

    draw.polygon(points, fill=draw_color)
    return points

# Function to draw fluid lines with randomized control points
def bezier_curve_random(points, num_points=100):
    curves = []
    for _ in range(10):
        x1 = random.randint(0, WIDTH-10)
        y1 = random.randint(0, HEIGHT-10)
        x2 = random.randint(x1+10, x1+150)
        y2 = random.randint(y1+10, y1+150)

        curve = bezier_curve([x1, y1], control_point_1=np.array([x1+50, y1+50]), control_point_2=np.array([x2, 

y2]))
        curves.append(curve)
    return curves

# Function to draw Bezier curves
def bezier_curve(points, control_point_1=np.array([100, 100]), control_point_2=np.array([200, 300])):
    curve = []
    for t in np.linspace(0, 1, 150):
        point_x = int(np.round(float(points[0][0]) * (1-t)**2 + float(control_point_1[0]) * 2*(1-t)*t + 
float(control_point_2[0])* t**2))
        point_y = int(np.round(float(points[0][1]) * (1-t)**2 + float(control_point_1[1]) * 2*(1-t)*t + 
float(control_point_2[1])* t**2))

        curve.append((point_x, point_y))

    return curve

# Function to draw long Bezier curves with muted colors
def bezier_curve_long(points):
    color = (random.randint(120, 180), random.randint(60, 140), 110)
    width = int(random.uniform(1, 5))
    curve = bezier_curve(points, control_point_1=np.array([points[0][0]-50, points[0][1]]), 
                           control_point_2=np.array([points[1][0]+50, points[1][1]]))
    draw.line(curve, fill=color, width=width)
    return curve

# Draw the artwork
for _ in range(100):
    x = random.randint(0, WIDTH-10)
    y = random.randint(0, HEIGHT-10)
    complex_shape(x, y)

# Draw long Bezier curves
bezier_curves = []
for i in range(20):
    points = bezier_curve_long([(random.randint(0,WIDTH), random.randint(0,HEIGHT)),
                                (random.randint(0,WIDTH), random.randint(0,HEIGHT))])
    for point in points:
        draw.line([point], fill=(random.randint(120, 180), random.randint(60, 140), 110), width=1)
    bezier_curves.append(points)

# Save the image
img.save('Artes_Cosmic_Tapestry.png')