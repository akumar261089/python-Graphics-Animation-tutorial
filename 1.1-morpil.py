from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

# Create a new image with white background
img = Image.new('RGB', (800, 800), 'white')
draw = ImageDraw.Draw(img)

# Draw basic shapes
draw.rectangle([100, 100, 200, 200], fill='red', outline='black')           # Square
draw.ellipse([250, 100, 350, 200], fill='blue', outline='black')           # Circle
draw.polygon([(400, 100), (450, 200), (350, 200)], fill='green', outline='black') # Triangle

# Draw lines and arcs
draw.line([50, 300, 750, 300], fill='purple', width=5)                    # Horizontal line
draw.arc([100, 350, 300, 550], start=0, end=180, fill='orange', width=3)  # Arc

# Add text
try:
    font = ImageFont.truetype("arial.ttf", size=24)  # Adjust font path if needed
except IOError:
    font = ImageFont.load_default()
draw.text((50, 600), "Hello, PIL!", fill='black', font=font)

# Paste an image onto the canvas
try:
    small_img = Image.open("example.png")  # Replace with an actual image path
    small_img_resized = small_img.resize((100, 100))
    img.paste(small_img_resized, (600, 600))
except FileNotFoundError:
    print("example.png not found; skipping paste operation.")

# Apply filters
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred_image.png")

# Flip and rotate
flipped = ImageOps.flip(img)
flipped.save("flipped_image.png")
rotated = img.rotate(45)
rotated.save("rotated_image.png")

# Crop a region
cropped = img.crop((100, 100, 300, 300))
cropped.save("cropped_image.png")

# Save the final image
img.save('extended_pil_practice.png')

# Show the image
img.show()
