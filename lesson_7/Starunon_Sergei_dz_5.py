import os
import json

find_in_folder = './some_data/'
result_dict = {}

for root, dirnames, filenames in os.walk(find_in_folder):
    for filename in filenames:
        path_file = os.path.join(root, filename)
        digits = len(str(os.stat(path_file).st_size))
        file_extension = os.path.splitext(filename)[-1]
        file_quantity, extensions = result_dict.get(10 ** digits, (0, []))
        file_quantity += 1
        if not (file_extension in extensions):
            extensions.append(file_extension)
        result_dict[10 ** digits] = (file_quantity, extensions)


with open(f'{os.path.split(os.getcwd())[-1]}_summary.json', 'w', encoding='utf-8') as file:
    json.dump(result_dict, file)
