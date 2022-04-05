import os

find_in_folder = './some_data/'
result_dict = {}

for root, dirnames, filenames in os.walk(find_in_folder):
    for filename in filenames:
        path_file = os.path.join(root, filename)
        digits = len(str(os.stat(path_file).st_size))
        result_dict[10 ** digits] = result_dict.get(10 ** digits, 0) + 1

print(result_dict)
