import os

structure = {
    'my_project2': ['settings', 'mainapp', 'adminapp', 'authapp']
}

for root, dirs in structure.items():
    os.makedirs(root, exist_ok=True)
    os.chdir(root)
    for fol in dirs:
        os.makedirs(fol, exist_ok=True)
    os.chdir('..')
