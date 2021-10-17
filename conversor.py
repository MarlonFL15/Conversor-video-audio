import os
import sys
from moviepy.editor import VideoFileClip


def video_to_audio(video_file):
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.mp3")


if __name__ == "__main__":
    video = sys.argv[1]
    video_to_audio(video)
