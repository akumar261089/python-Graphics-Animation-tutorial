# Python Graphics and Animation Tutorial

A comprehensive guide to creating Canva-like graphics and animations using Python

## Table of Contents

1. [Setup and Installation](#setup-and-installation)
2. [Basic Shapes and Images](#basic-shapes-and-images)
3. [Text and Typography](#text-and-typography)
4. [Animations and Motion](#animations-and-motion)
5. [Creating Logos](#creating-logos)
6. [Video Generation](#video-generation)
7. [Exercises and Projects](#exercises-and-projects)
8. [Social Media Platform Requirements](#social-media-platform-requirements)
9. [Video Optimization](#video-optimization)
10. [Platform Integration](#platform-integration)
11. [Automated Posting](#automated-posting)
12. [Analytics Tracking](#analytics-tracking)

## Setup and Installation

First, we'll need to install the required libraries:

```python
python3 -m venv pygraphicstut
source pygraphicstut/Scripts/activate
pip install -r requirements.txt
pip install pillow           # For image processing
pip install moviepy          # For video creation
pip install cairo           # For vector graphics
pip install svgwrite        # For SVG creation
pip install numpy           # For numerical operations
```

## Basic Shapes and Images

### Drawing Basic Shapes

Let's start with creating basic shapes using Pillow (PIL):

```python
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
```

### Working with Images

```python
from PIL import Image, ImageEnhance

# Open and resize an image
image = Image.open('input.jpg')
resized_image = image.resize((800, 600))

# Apply filters
enhancer = ImageEnhance.Brightness(resized_image)
brightened = enhancer.enhance(1.5)  # Increase brightness by 50%

enhancer = ImageEnhance.Contrast(brightened)
final_image = enhancer.enhance(1.2)  # Increase contrast by 20%

final_image.save('enhanced.jpg')
```

## Text and Typography

### Adding Text to Images

```python
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
```

## Animations and Motion

### Creating Simple Animations with MoviePy

```python
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

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
```

## Creating Logos

### Vector-based Logo Creation

```python
import svgwrite

def create_simple_logo():
    # Create new SVG drawing
    dwg = svgwrite.Drawing('logo.svg', size=(200, 200))

    # Add background circle
    dwg.add(dwg.circle(center=(100, 100), r=80,
            fill='#2196F3'))

    # Add text
    dwg.add(dwg.text('LOGO', insert=(50, 110),
            fill='white', font_size=40))

    dwg.save()

create_simple_logo()
```

## Video Generation

### Creating a Simple Video Slideshow

```python
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
images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
create_slideshow(images)
```

## Exercises and Projects

### Exercise 1: Social Media Banner Creator

Create a program that generates social media banners with custom text and background patterns.

```python
def create_social_banner(text, size=(1200, 630),
                        bg_color='blue', text_color='white'):
    # Your code here
    pass

# Template solution:
from PIL import Image, ImageDraw, ImageFont

def create_social_banner(text, size=(1200, 630),
                        bg_color='blue', text_color='white'):
    # Create base image
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)

    # Add text
    font = ImageFont.truetype("arial.ttf", 60)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2

    draw.text((x, y), text, font=font, fill=text_color)
    return img
```

### Exercise 2: Animated Logo Generator

Create a program that generates an animated version of a logo with rotating or pulsing effects.

```python
def create_animated_logo(logo_path, duration=5):
    # Your code here
    pass

# Template solution:
from moviepy.editor import ImageClip, vfx

def create_animated_logo(logo_path, duration=5):
    # Load logo
    logo = ImageClip(logo_path)

    # Add rotation animation
    animated_logo = logo.resize(0.5).set_duration(duration)
    animated_logo = animated_logo.set_position('center')
    animated_logo = animated_logo.rotate(
        lambda t: 360*t/duration)

    # Write final video
    animated_logo.write_videofile("animated_logo.mp4",
                                fps=24)
```

### Exercise 3: Video Title Generator

Create a program that generates professional-looking video titles with animations and effects.

### Project Ideas:

1. YouTube Thumbnail Generator
2. Instagram Story Creator
3. Animated Infographic Generator
4. Logo Animation Suite
5. Social Media Content Calendar Generator

## Advanced Topics for Further Exploration

1. Working with 3D graphics using libraries like VPython or PyOpenGL
2. Creating interactive graphics with Pygame
3. Implementing complex animations using mathematical functions
4. Adding audio to videos using MoviePy
5. Creating data visualizations with Matplotlib or Plotly

## Tips for Better Graphics

1. Always use high-resolution images
2. Maintain aspect ratios when resizing
3. Use appropriate color schemes
4. Consider accessibility in text size and contrast
5. Test outputs on different devices and platforms

## Social Media Platform Requirements

### Platform Specifications

```python
PLATFORM_SPECS = {
    'instagram': {
        'feed_video': {
            'aspect_ratios': [(1.91, 1), (4, 5), (1, 1)],
            'max_duration': 60,  # seconds
            'min_duration': 3,   # seconds
            'max_size': 100,     # MB
            'formats': ['mp4'],
            'codecs': ['h264'],
            'max_resolution': (1920, 1080)
        },
        'story': {
            'aspect_ratio': (9, 16),
            'max_duration': 15,
            'formats': ['mp4'],
            'max_resolution': (1080, 1920)
        }
    },
    'youtube': {
        'standard': {
            'aspect_ratios': [(16, 9)],
            'max_duration': 43200,  # 12 hours
            'formats': ['mp4'],
            'max_resolution': (3840, 2160)  # 4K
        }
    },
    'tiktok': {
        'standard': {
            'aspect_ratio': (9, 16),
            'max_duration': 180,
            'formats': ['mp4'],
            'max_resolution': (1080, 1920)
        }
    },
    'twitter': {
        'standard': {
            'max_duration': 140,
            'max_size': 512,
            'formats': ['mp4'],
            'max_resolution': (1920, 1080)
        }
    }
}
```

## Video Optimization

### Universal Video Optimizer

```python
from moviepy.editor import VideoFileClip
import os

class VideoOptimizer:
    def __init__(self, video_path):
        self.video = VideoFileClip(video_path)

    def optimize_for_platform(self, platform, post_type='standard'):
        specs = PLATFORM_SPECS[platform][post_type]

        # Check and adjust duration
        if hasattr(specs, 'max_duration'):
            self.video = self._adjust_duration(specs['max_duration'])

        # Resize for platform
        if 'max_resolution' in specs:
            self.video = self._resize_video(specs['max_resolution'])

        # Adjust aspect ratio
        if 'aspect_ratio' in specs:
            self.video = self._adjust_aspect_ratio(specs['aspect_ratio'])

        return self

    def _adjust_duration(self, max_duration):
        if self.video.duration > max_duration:
            return self.video.subclip(0, max_duration)
        return self.video

    def _resize_video(self, max_resolution):
        current_res = (self.video.w, self.video.h)
        if current_res[0] > max_resolution[0] or current_res[1] > max_resolution[1]:
            resize_factor = min(max_resolution[0]/current_res[0],
                              max_resolution[1]/current_res[1])
            new_size = (int(current_res[0]*resize_factor),
                       int(current_res[1]*resize_factor))
            return self.video.resize(new_size)
        return self.video

    def _adjust_aspect_ratio(self, target_ratio):
        current_ratio = self.video.w / self.video.h
        target_ratio_float = target_ratio[0] / target_ratio[1]

        if abs(current_ratio - target_ratio_float) < 0.01:
            return self.video

        # Add letterboxing/pillarboxing
        def add_padding(t):
            frame = self.video.get_frame(t)
            if current_ratio > target_ratio_float:
                # Add letterboxing (black bars on top and bottom)
                new_height = int(self.video.w / target_ratio_float)
                pad_height = (new_height - self.video.h) // 2
                return np.pad(frame, ((pad_height, pad_height), (0, 0), (0, 0)),
                            mode='constant', constant_values=0)
            else:
                # Add pillarboxing (black bars on sides)
                new_width = int(self.video.h * target_ratio_float)
                pad_width = (new_width - self.video.w) // 2
                return np.pad(frame, ((0, 0), (pad_width, pad_width), (0, 0)),
                            mode='constant', constant_values=0)

        return self.video.fl(add_padding)

# Example usage
optimizer = VideoOptimizer('my_video.mp4')
instagram_video = optimizer.optimize_for_platform('instagram', 'feed_video')
instagram_video.write_videofile('instagram_ready.mp4')
```

## Platform Integration

### Instagram API Integration

```python
from instabot import Bot
import os

class InstagramPublisher:
    def __init__(self, username, password):
        self.bot = Bot()
        self.bot.login(username=username, password=password)

    def post_video(self, video_path, caption=''):
        # Optimize video first
        optimizer = VideoOptimizer(video_path)
        optimized_video = optimizer.optimize_for_platform('instagram', 'feed_video')
        optimized_path = 'temp_optimized.mp4'
        optimized_video.write_videofile(optimized_path)

        # Post to Instagram
        try:
            self.bot.upload_video(optimized_path, caption=caption)
            return True
        except Exception as e:
            print(f"Error posting to Instagram: {e}")
            return False
        finally:
            if os.path.exists(optimized_path):
                os.remove(optimized_path)
```

### YouTube API Integration

```python
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class YouTubePublisher:
    def __init__(self, client_secrets_file):
        self.SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
        self.credentials = self._get_credentials(client_secrets_file)
        self.youtube = build('youtube', 'v3', credentials=self.credentials)

    def _get_credentials(self, client_secrets_file):
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, self.SCOPES)
        return flow.run_local_server(port=0)

    def upload_video(self, video_path, title, description, privacy_status='private'):
        # Optimize video
        optimizer = VideoOptimizer(video_path)
        optimized_video = optimizer.optimize_for_platform('youtube')
        optimized_path = 'temp_youtube.mp4'
        optimized_video.write_videofile(optimized_path)

        try:
            body = {
                'snippet': {
                    'title': title,
                    'description': description,
                    'tags': []
                },
                'status': {
                    'privacyStatus': privacy_status,
                    'selfDeclaredMadeForKids': False
                }
            }

            media = MediaFileUpload(
                optimized_path,
                mimetype='video/mp4',
                resumable=True
            )

            request = self.youtube.videos().insert(
                part=','.join(body.keys()),
                body=body,
                media_body=media
            )

            response = request.execute()
            return response

        finally:
            if os.path.exists(optimized_path):
                os.remove(optimized_path)
```

### TikTok API Integration

```python
from TikTokApi import TikTokApi

class TikTokPublisher:
    def __init__(self, api_key):
        self.api = TikTokApi.get_instance(custom_verifyFp=api_key)

    def post_video(self, video_path, description=''):
        # Optimize video
        optimizer = VideoOptimizer(video_path)
        optimized_video = optimizer.optimize_for_platform('tiktok')
        optimized_path = 'temp_tiktok.mp4'
        optimized_video.write_videofile(optimized_path)

        try:
            # Note: TikTok's API has limitations for video uploads
            # This is a simplified example
            response = self.api.upload_video(
                video_path=optimized_path,
                description=description
            )
            return response

        finally:
            if os.path.exists(optimized_path):
                os.remove(optimized_path)
```

## Automated Posting

### Social Media Manager

```python
class SocialMediaManager:
    def __init__(self, credentials):
        self.instagram = InstagramPublisher(
            credentials['instagram']['username'],
            credentials['instagram']['password']
        )
        self.youtube = YouTubePublisher(
            credentials['youtube']['client_secrets_file']
        )
        self.tiktok = TikTokPublisher(
            credentials['tiktok']['api_key']
        )

    def post_to_all_platforms(self, video_path, metadata):
        results = {}

        # Post to Instagram
        if metadata.get('instagram'):
            results['instagram'] = self.instagram.post_video(
                video_path,
                caption=metadata['instagram'].get('caption', '')
            )

        # Post to YouTube
        if metadata.get('youtube'):
            results['youtube'] = self.youtube.upload_video(
                video_path,
                title=metadata['youtube'].get('title', ''),
                description=metadata['youtube'].get('description', ''),
                privacy_status=metadata['youtube'].get('privacy', 'private')
            )

        # Post to TikTok
        if metadata.get('tiktok'):
            results['tiktok'] = self.tiktok.post_video(
                video_path,
                description=metadata['tiktok'].get('description', '')
            )

        return results

# Example usage
credentials = {
    'instagram': {
        'username': 'your_username',
        'password': 'your_password'
    },
    'youtube': {
        'client_secrets_file': 'path/to/client_secrets.json'
    },
    'tiktok': {
        'api_key': 'your_api_key'
    }
}

metadata = {
    'instagram': {
        'caption': 'Check out my new video! #python #coding'
    },
    'youtube': {
        'title': 'Amazing Python Tutorial',
        'description': 'Learn how to code in Python',
        'privacy': 'public'
    },
    'tiktok': {
        'description': 'Coding tutorial #pythoncode #programming'
    }
}

manager = SocialMediaManager(credentials)
results = manager.post_to_all_platforms('my_video.mp4', metadata)
```

## Analytics Tracking

```python
from datetime import datetime, timedelta
import pandas as pd

class SocialMediaAnalytics:
    def __init__(self, social_media_manager):
        self.manager = social_media_manager
        self.metrics = {}

    def gather_metrics(self, video_id, platforms=['instagram', 'youtube', 'tiktok']):
        metrics = {}

        for platform in platforms:
            if platform == 'youtube':
                metrics['youtube'] = self._get_youtube_metrics(video_id)
            elif platform == 'instagram':
                metrics['instagram'] = self._get_instagram_metrics(video_id)
            elif platform == 'tiktok':
                metrics['tiktok'] = self._get_tiktok_metrics(video_id)

        self.metrics[video_id] = metrics
        return metrics

    def _get_youtube_metrics(self, video_id):
        # Example YouTube metrics retrieval
        response = self.manager.youtube.youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        if 'items' in response:
            stats = response['items'][0]['statistics']
            return {
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0))
            }
        return {}

    def generate_report(self, video_id):
        if video_id not in self.metrics:
            self.gather_metrics(video_id)

        report = {
            'video_id': video_id,
            'timestamp': datetime.now(),
            'metrics': self.metrics[video_id]
        }

        # Convert to DataFrame for easy analysis
        df = pd.DataFrame([report])
        return df

# Example usage
analytics = SocialMediaAnalytics(manager)
metrics = analytics.gather_metrics('video_id_123')
report = analytics.generate_report('video_id_123')
```

## Exercise: Multi-Platform Content Manager

Create a program that:

1. Takes a video file as input
2. Optimizes it for different platforms
3. Adds platform-specific overlays (watermarks, handles, hashtags)
4. Posts to multiple platforms
5. Tracks performance metrics

```python
def create_multi_platform_content(video_path, metadata):
    # Your code here
    pass

# Template solution structure:
def create_multi_platform_content(video_path, metadata):
    # 1. Initialize manager
    manager = SocialMediaManager(credentials)

    # 2. Create platform-specific versions
    versions = {}
    optimizer = VideoOptimizer(video_path)

    for platform in ['instagram', 'youtube', 'tiktok']:
        if platform in metadata:
            optimized = optimizer.optimize_for_platform(platform)
            versions[platform] = optimized

    # 3. Add overlays
    for platform, video in versions.items():
        add_platform_overlays(video, platform, metadata[platform])

    # 4. Post to platforms
    results = manager.post_to_all_platforms(versions, metadata)

    # 5. Track metrics
    analytics = SocialMediaAnalytics(manager)
    metrics = analytics.gather_metrics(results)

    return results, metrics
```

Remember to:

- Keep API credentials secure
- Handle rate limits and API restrictions
- Implement proper error handling
- Monitor API usage and costs
- Follow platform-specific guidelines and terms of service
