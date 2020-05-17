"""reDirectory.

Usage:
  reDirectory.py <directoryPath> [--ignore <filetypes>]
  reDirectory.py (-h | --help)
  reDirectory.py --version

Options:
  --ignore <filetypes> files to ignore. [default=<>]
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
import os
import filetype
import re

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
    print(arguments)
    workDir = arguments["<directoryPath>"]
    directory = os.fsencode(workDir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        fullPath = os.path.join(workDir, filename)
        #ignore hidden files
        if(filename[0] != '.' and os.path.isfile(fullPath)):
            print(filename, end =" ")
            kind = filetype.guess(fullPath)
            if kind is None:
                print("idk filetype", end = " ")
                folder = folders.get("Other", "Other")
            else:    
                category = (re.split("/", kind.mime))[0]
                print(category, end = " ")
                folder = folders.get(category, "Other")
            print(folder)
            folderPath = os.path.join(workDir, folder)
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
            os.rename(fullPath, os.path.join(folderPath, filename))
