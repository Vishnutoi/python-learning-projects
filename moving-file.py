#This script help you move .jpg file from folder to another folder

import glob, os, shutil

source_dir = '/Users/vishnu/Desktop' #Path where your files are at the moment
dst = '/Users/vishnu/Desktop/screenshot-backup' #Path you want to move your files to
files = glob.iglob(os.path.join(source_dir, "*.jpg"))
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dst)