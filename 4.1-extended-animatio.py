from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip, ImageClip, vfx
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

def add_audio_to_video(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    video_with_audio = video.set_audio(audio)
    video_with_audio.write_videofile(output_path, fps=24)

def join_videos(video_paths, output_path):
    clips = [VideoFileClip(path) for path in video_paths]
    final_clip = concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile(output_path, fps=24)

def apply_transition_between_videos(video_paths, output_path, transitions):
    clips = [VideoFileClip(path) for path in video_paths]
    transition_duration = 1

    def crossfade(clip1, clip2):
        return CompositeVideoClip([
            clip1.crossfadeout(transition_duration),
            clip2.crossfadein(transition_duration).set_start(clip1.duration - transition_duration)
        ])

    def blur_transition(clip1, clip2):
        blurred_clip1 = clip1.fx(vfx.blur, transition_duration)
        blurred_clip2 = clip2.fx(vfx.blur, transition_duration)
        return concatenate_videoclips([blurred_clip1, blurred_clip2], method='compose')

    final_clip = clips[0]
    for i, next_clip in enumerate(clips[1:]):
        if transitions[i] == "crossfade":
            final_clip = crossfade(final_clip, next_clip)
        elif transitions[i] == "blur":
            final_clip = blur_transition(final_clip, next_clip)

    final_clip.write_videofile(output_path, fps=24)

def create_video_from_image_with_effects(image_path, output_path, effect):
    img_clip = ImageClip(image_path, duration=10)

    if effect == "zoom_in":
        final_clip = img_clip.fx(vfx.resize, lambda t: 1 + 0.02 * t)
    elif effect == "pan_clip_right":
        final_clip = img_clip.set_position(lambda t: (100 + 30 * t, 'center'))
    elif effect == "zoom_and_pan":
        zoom_clip = img_clip.fx(vfx.resize, lambda t: 1 + 0.02 * t)
        final_clip = zoom_clip.set_position(lambda t: (100 + 30 * t, 'center'))
    else:
        final_clip = img_clip  # Default effect (no transformation)

    final_clip.write_videofile(output_path, fps=24)

def overlay_videos_with_transparency(background_video_path, overlay_video_path, output_path, transparency):
    background_clip = VideoFileClip(background_video_path)
    overlay_clip = VideoFileClip(overlay_video_path).set_opacity(transparency)
    final_clip = CompositeVideoClip([background_clip, overlay_clip.set_position('center')])
    final_clip.write_videofile(output_path, fps=24)

# Example usage
create_animated_text("Welcome to My Channel!")
add_audio_to_video("animated_text.mp4", "background_audio.mp3", "final_with_audio.mp4")
join_videos(["video1.mp4", "video2.mp4"], "joined_videos.mp4")
apply_transition_between_videos(["video1.mp4", "video2.mp4", "video3.mp4"], "videos_with_transitions.mp4", ["crossfade", "blur"])
create_video_from_image_with_effects("example_image.jpg", "image_to_video.mp4", "pan_clip_right")
overlay_videos_with_transparency("background.mp4", "overlay.mp4", "video_with_overlay.mp4", 0.5)
