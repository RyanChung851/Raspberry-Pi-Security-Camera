# Raspberry-Pi-Security-Camera

These are the relevant configuration settings for the motion.conf file that comes with the RPi motion package.

daemon on #default off

webcam_port 6789 #default 8081

framerate 30 #default 2 

width 320 #default 320 

height 240 #default 240 

threshold 1800 #default 1500 

pre_capture 0 #default 0 

post_capture 0 #default 0 

output_normal off #default on 

ffmpeg_video_codec msmpeg4 #default swf 

target_dir /home/pi/gdrive/Video #default /tmp/motion #default null

webcam_localhost off #default on      **on will only let the stream be viewed on the RPi**

gap 60 #default 60

on_motion_detected /usr/bin/python /home/pi/gdrive/Video/cam.py #default value

