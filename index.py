from pytube import YouTube

                               #100 bytes 90 80 70 0
def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    #100
    total_size = stream.filesize
                       #100       - 20             = 80 ja baixado
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(pct_completed)
    
VIDEO_URL = 'https://www.youtube.com/watch?v=gBJ37ES-qNk'
yt = YouTube(VIDEO_URL, on_progress_callback=on_progress)

# for stream in yt.streams:
#     print(stream)

video = yt.streams.get_highest_resolution()
video.download()

