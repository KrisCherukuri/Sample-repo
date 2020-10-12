from pathlib import Path
import subprocess
import json
def video_length_seconds(filename):
    result = subprocess.run(['ffprobe', filename, '-print_format', 'json', '-show_streams', '-loglevel', 'quiet'], capture_output=True, text=True)
    return float(json.loads(result.stdout)['streams'][0]['duration'])

# all mp4 files in the current directory in seconds
print(sum(video_length_seconds(f) for f in Path('.').glob('*.mp4')))

# all files in the current directory
print(sum(video_length_seconds(f) for f in Path('.').iterdir() if f.is_file()))