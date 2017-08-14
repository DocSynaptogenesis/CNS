import ffmpy3
import os

os.chdir('  ')


ff = ffmpy3.FFmpeg(
    inputs = {'...file name...': None},
    outputs = {'...file name...': "-s 3840x2160" } 
)

ff.run()
