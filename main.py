__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from genericpath import isfile
import os
import shutil
os.chdir('files')

# 1
def clean_cache():
    if not os.path.exists('cache'):
        os.mkdir('cache')
    else:
        shutil.rmtree('cache')
        os.mkdir('cache')


# 2
def cache_zip(path,cache):
    shutil.unpack_archive(path, cache)

# 3
def cached_files():
    files_path = []
    for file in os.listdir('cache'):
        path = os.path.join(os.path.abspath('cache'), file)
        if os.path.isfile(path):
            files_path.append(path)
    return files_path


#4
def find_password(files_path):
    for file in files_path:
        with open(file, 'r') as file:
            for line in file:
                if 'password' in line:
                    return line[line.find(' ') + 1: -1]



print(os.getcwd())
#clean_cache()
#cache_zip("data.zip", 'cache')
#print(cached_files())
#print(os.listdir('cache'))
print(find_password(cached_files()))
