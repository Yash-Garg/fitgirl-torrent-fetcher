from pytube import YouTube
import time

def downloadVideo(videoURL):
    yt = YouTube(videoURL)
    for stream in yt.streams.filter(resolution="720p", fps=30, progressive=True):
        time.sleep(1)
        print('\nDownloading video at 720p...')
        stream.download(output_path="./downloads")
        print('\nVideo Downloaded Successfully!')