import subprocess
import os
import sys

source = 'Source'
photo_size = sys.argv[1]

current_dir = os.path.dirname(os.path.abspath(__file__))
search_folder_path = os.path.join(current_dir, source)
photo_list = list(os.walk(search_folder_path).__next__()[2])

subprocess.call('mkdir Result', shell=True)
subprocess.call('cp -a Source/. Result/', shell=True)


def resize_photos(files, size):
    for file in files:
        file_path = 'Result/{}'.format(file)
        command = 'sips --resampleWidth' + ' ' + size + ' ' + file_path
        subprocess.call(command, shell=True)


resize_photos(photo_list, photo_size)
