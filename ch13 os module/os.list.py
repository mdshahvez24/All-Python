# exploring folders

import os 

folders = os.listdir("data")
print(os.folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))