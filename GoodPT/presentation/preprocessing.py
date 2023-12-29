
import subprocess
def extractAudioFromVideo():
    input_video_path = "tmp/myvideo.mp4"
    output_audio_path = "tmp/myaudio.mp3"
    command = ['ffmpeg', '-i', input_video_path, output_audio_path]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if process.returncode == 0:
        print("Audio extracted successfully.")
    else:
        print(f"Error extracting audio: {process.stderr.decode('utf-8')}")



    