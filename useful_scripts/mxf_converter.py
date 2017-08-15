# ********************************************************************** #
###################################################################
##############################################

#          Author: DocSynaptogenesis
#          File Name: mxf_converter.py
#          Project: NA
#
#          Python Version: 3.6.1
#          Anaconda Version 4.4.0 (64-bit)
#
#          Description: converts .mxf video files to .mp4
#          Notes: resolution is scalable
#          Dependencies: 
#              - Requires FFmpeg added to Path

#####################
###################################################################
##########################################################################
# ********************************************************************** #

import ffmpy3
import os

os.chdir('  ')


ff = ffmpy3.FFmpeg(
    inputs = {'...file name...': None},
    outputs = {'...file name...': "-s 3840x2160" } # resolution ran successfully, resulting video played successfully
)

ff.run()
