#! /usr/bin/env python

"""
Copyright 2016-2019 Louis Moresi

"""

from distutils import dir_util as _dir_util
from distutils import file_util as _file_util

import os

# Copy material from locations in the container to the user's home directory

# 1 - config files
Source_Path = "/user_data/configs/@jupyterlab"
Destination_Path = "/home/jovyan/.jupyter/lab/user-settings/@jupyterlab"

# Note: Update=True only overwrites files that are older (caution if updating files in the container)
try:
    ct = _dir_util.copy_tree(Source_Path, Destination_Path, preserve_mode=1, preserve_times=1, preserve_symlinks=1, update=True, verbose=True, dry_run=0)
except:
    print("Installing / updating settings failed !!")

# 2 - unspecified content (generic - a unique directory name for the content would be helpful if multiple images are likely to be launched)
Source_Path = "/user_data/1_UserContent"
Destination_Path = "/home/jovyan"

ct = _dir_util.copy_tree(Source_Path, Destination_Path, preserve_mode=1, preserve_times=1, preserve_symlinks=1, update=True, verbose=True, dry_run=0)
