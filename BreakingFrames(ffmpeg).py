import subprocess
import time;

start_time= time.time()

subprocess.call('ffmpeg.exe -ss 00:00:00 -t 00:00:43 -i main.mp4 -qscale:v 2 -r 5.0 MainVideoFrames/output_image-%0d.jpg', shell = True)
# subprocess.call('ffmpeg.exe -ss 00:00:00 -t 00:00:02 -i main-1.mp4 -qscale:v 2 -r 5.0 Add1Frames/output_image-%0d.jpg', shell = True)
# subprocess.call('ffmpeg.exe -ss 00:00:00 -t 00:00:03 -i main-2.mp4 -qscale:v 2 -r 5.0 Add2Frames/output_image-%0d.jpg', shell = True)
# subprocess.call('ffmpeg.exe -ss 00:00:00 -t 00:00:04 -i main-3.mp4 -qscale:v 2 -r 5.0 Add3Frames/output_image-%0d.jpg', shell = True)
print("Frame Breaking takes ",(time.time()-start_time));