from PIL import Image, ImageDraw

# Create a new image with white background
img = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(img)

# Draw shapes
draw.rectangle([100, 100, 200, 200], fill='red')           # Square
draw.ellipse([250, 100, 350, 200], fill='blue')           # Circle
draw.polygon([(400, 100), (450, 200), (350, 200)],
            fill='green')                                  # Triangle

img.save('basic_shapes.png')