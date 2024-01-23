import time
import os
import shutil

path = 'file2.txt'  
days = 30 

seconds = days * 24 * 60 * 60


time_in_seconds = time.time() - seconds

if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            file_path = os.path.join(root, name)
            ctime = os.stat(file_path).st_ctime
            
            if ctime < time_in_seconds:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"File {file_path} removed")
                else:
                    shutil.rmtree(file_path)
                    print(f"Directory {file_path} removed")
else:
    print("Path not found")
