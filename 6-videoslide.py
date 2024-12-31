from moviepy.editor import ImageClip, concatenate_videoclips

def create_slideshow(image_files, duration_per_image=3):
    # Create clips from images
    clips = [ImageClip(img).set_duration(duration_per_image)
             for img in image_files]

    # Concatenate clips
    final_clip = concatenate_videoclips(clips,
                                      method="compose")

    # Write final video
    final_clip.write_videofile("slideshow.mp4", fps=24)

# Example usage
images = ['basic_shapes.png', 'text_overlay.png', 'enhanced.jpg']
create_slideshow(images)