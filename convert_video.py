import os
import subprocess

input_dir = 'static/videos/comparsion'
output_dir = 'static/videos_compress/comparsion'
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.mp4'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        command = [
            'ffmpeg', '-i', input_path,
            '-b:v', '256k', '-vf', 'scale=426:240',
            output_path
        ]
        
        subprocess.run(command, check=True)