import os

path = (r"/Users/haley.karp/Desktop/vscode/socialcyber/Reachability")

dirp_list = []
for dirpath, subdirs, files in os.walk(path):
    dirp_list.append(dirpath)

print(dirp_list)