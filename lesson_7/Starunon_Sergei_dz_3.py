import os
import shutil


path = os.path.join('my_project', 'templates')

for root, dirs, files in os.walk('my_project'):
    if 'templates' in root:
        for file in files:
            path_file = os.path.join(root, file)
            end_dir = os.path.join(path, os.path.split(root)[-1])
            os.makedirs(end_dir, exist_ok=True)
            try:
                shutil.copy2(path_file, os.path.join(end_dir, file))
            except shutil.SameFileError:
                print(f'file {os.path.join(end_dir, file)} exists')
