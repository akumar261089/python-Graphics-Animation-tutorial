from PIL import Image, ImageDraw, ImageFont

def create_text_overlay(text, font_size=60):
    # Create image
    img = Image.new('RGB', (800, 400), 'white')
    draw = ImageDraw.Draw(img)

    # Load font (use a system font or download custom ones)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate text size and position for center alignment
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (800 - text_width) // 2
    y = (400 - text_height) // 2

    # Draw text
    draw.text((x, y), text, font=font, fill='black')
    return img

# Example usage
text_image = create_text_overlay("Hello World!")
text_image.save('text_overlay.png')