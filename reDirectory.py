#!/usr/bin/python3
"""reDirectory.

Usage:
  reDirectory.py <directoryPath>
  reDirectory.py (-h | --help)
  reDirectory.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
import os
import filetype
import re

#map of file classifications to folder names
folders = {
        'image':'Images',
        'video':'Videos',
        'audio':'Audio',
        'font':'Fonts',
        'archive':'Archives',
        'document':'Documents'
        }

if __name__ == '__main__':
    arguments = docopt(__doc__, version='reDirectory 0.1')
    workDir = arguments["<directoryPath>"]
    directory = os.fsencode(workDir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        fullPath = os.path.join(workDir, filename)
        #ignore hidden files and directories
        if(filename[0] != '.' and os.path.isfile(fullPath)):
            kind = filetype.guess(fullPath)
            if kind is None:
                folder = folders.get("Other", "Other")
            else:    
                category = (re.split("/", kind.mime))[0]
                folder = folders.get(category, "Other")
            folderPath = os.path.join(workDir, folder)
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
            #move file to directory
            os.rename(fullPath, os.path.join(folderPath, filename))
            print(filename," --> ", folder)
