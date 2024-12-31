from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip, ImageClip, vfx
import moviepy.config as mp_config
from moviepy.editor import *
from moviepy.editor import concatenate_videoclips, vfx
import cv2
import numpy as np
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

    def blur_transition(clip1, clip2, transition_duration):
        # Apply Gaussian blur to both clips
        blurred_clip1 = clip1.fx(vfx.gaussian_blur, radius=5)  # Adjust the radius as needed
        blurred_clip2 = clip2.fx(vfx.gaussian_blur, radius=5)  # Adjust the radius as needed
        
        # Concatenate the clips with a smooth transition
        return concatenate_videoclips([blurred_clip1, blurred_clip2], method='compose')


    final_clip = clips[0]
    for i, next_clip in enumerate(clips[1:]):
        if transitions[i] == "crossfade":
            final_clip = crossfade(final_clip, next_clip)
        elif transitions[i] == "blur":
            final_clip = blur_transition(final_clip, next_clip)

    final_clip.write_videofile(output_path, fps=24)

def Zoom(clip,mode='in',position='center',speed=1):
    fps = clip.fps
    duration = clip.duration
    total_frames = int(duration*fps)
    def main(getframe,t):
        frame = getframe(t)
        h,w = frame.shape[:2]
        i = t*fps
        if mode == 'out':
            i = total_frames-i
        zoom = 1+(i*((0.1*speed)/total_frames))
        positions = {'center':[(w-(w*zoom))/2,(h-(h*zoom))/2],
                     'left':[0,(h-(h*zoom))/2],
                     'right':[(w-(w*zoom)),(h-(h*zoom))/2],
                     'top':[(w-(w*zoom))/2,0],
                     'topleft':[0,0],
                     'topright':[(w-(w*zoom)),0],
                     'bottom':[(w-(w*zoom))/2,(h-(h*zoom))],
                     'bottomleft':[0,(h-(h*zoom))],
                     'bottomright':[(w-(w*zoom)),(h-(h*zoom))]}
        tx,ty = positions[position]
        M = np.array([[zoom,0,tx], [0,zoom,ty]])
        frame = cv2.warpAffine(frame,M,(w,h))
        return frame
    return clip.fl(main)
def create_video_from_image_with_effects(image_path, output_path, effect):
    #img_clip = ImageClip(image_path, duration=10)
    clip = ImageClip(image_path).set_fps(30).set_duration(10)
    clip = Zoom(clip,mode='in',position='center',speed=1) #zoom function above

    clip.write_videofile(output_path,preset='superfast')

    # if effect == "zoom_in":
        #img_clip = img_clip.set_position('center')
        # final_clip = img_clip.fx(vfx.resize, lambda t: (1 + 0.01 * t / 10, 1 + 0.01 * t / 10)) 
    # elif effect == "pan_clip_right":
    #     final_clip = img_clip.set_position(lambda t: (100 + 30 * t, 'center'))
    # elif effect == "zoom_and_pan":
    #     zoom_clip = img_clip.fx(vfx.resize, lambda t: 1 + 0.02 * t)
    #     final_clip = zoom_clip.set_position(lambda t: (100 + 30 * t, 'center'))
    # else:
    #     final_clip = img_clip  # Default effect (no transformation)

    #final_clip.write_videofile(output_path, fps=24)

def overlay_videos_with_transparency(background_video_path, overlay_video_path, output_path, transparency):
    background_clip = VideoFileClip(background_video_path)
    overlay_clip = VideoFileClip(overlay_video_path).set_opacity(transparency)
    final_clip = CompositeVideoClip([background_clip, overlay_clip.set_position('center')])
    final_clip.write_videofile(output_path, fps=24)

# Example usage
# create_animated_text("Welcome to My Channel!")
# add_audio_to_video("animated_text.mp4", "output.mp3", "final_with_audio.mp4")
# join_videos(["animated_text.mp4", "final_with_audio.mp4"], "joined_videos.mp4")
# apply_transition_between_videos(["final_with_audio.mp4", "animated_text.mp4", "joined_videos.mp4"], "videos_with_transitions.mp4", ["crossfade", "crossfade"])
create_video_from_image_with_effects("extended_pil_practice.png", "image_to_video.mp4", "zoom_in")
overlay_videos_with_transparency("image_to_video.mp4", "final_with_audio.mp4", "video_with_overlay.mp4", 0.5)
