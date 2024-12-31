from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import moviepy.config as mp_config

# Set the path to the ImageMagick binary
mp_config.change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16\\magick.exe"})

def create_animated_text(text, duration=5):
    # Create text clip
    txt_clip = TextClip(text, fontsize=70, color='white')
    txt_clip = txt_clip.set_position('center')

    # Add animation
    txt_clip = txt_clip.set_duration(duration)
    txt_clip = txt_clip.fadein(1).fadeout(1)

    # Create final video
    final_clip = CompositeVideoClip([txt_clip],
                                   size=(1920, 1080))
    final_clip.write_videofile("animated_text.mp4",
                             fps=24)

# Example usage
create_animated_text("Welcome to My Channel!")