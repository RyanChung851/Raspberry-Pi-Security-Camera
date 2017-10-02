import os

"""
    Created by Ryan Chung 4/20/2017

    This program will only run on a raspberry pi that has motion package and odeke-em/drive Filesystem in Userspace installed.
    Credits to odeke-em/drive: https://github.com/odeke-em/drive
    This program will only run when motion is detected through a functional USB camera connected to the raspberry pi.
    
"""

"""
    The main function will push the gdrive/Video folder content to the google drive account that is connected to the
    fuse filesystem.

    If the current directory isn't gdrive/Video, the function will move into that directory.

    If the current directory is /home/pi/gdrive/Video then the function will push all recorded video footage to the
    google drive.

"""

def main():
    print("Starting upload to gdrive..")
    if os.getcwd() != "/home/pi/gdrive/Video":
        print("Redirecting to gdrive/Video")
        os.chdir("/home/pi/gdrive/Video")
    os.system("drive push -no-prompt")
    print("Success!")

main()
