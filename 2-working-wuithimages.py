from PIL import Image, ImageEnhance

# Open and resize an image
image = Image.open('basic_shapes.png')
resized_image = image.resize((800, 600))

# Apply filters
enhancer = ImageEnhance.Brightness(resized_image)
brightened = enhancer.enhance(1.5)  # Increase brightness by 50%

enhancer = ImageEnhance.Contrast(brightened)
final_image = enhancer.enhance(1.2)  # Increase contrast by 20%

final_image.save('enhanced.jpg')