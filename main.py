import os

os.chdir('/Users/taeyoungkim/Downloads')

print(os.listdir())

for file in os.listdir():
    if file == '.DS_Store':
        continue
    if file[:3] == 'lab':
        os.rename(f'/Users/taeyoungkim/Downloads/{file}', f'/Users/taeyoungkim/data100/labs/{file}')
    if file[:2] == 'hw':
        os.rename(f'/Users/taeyoungkim/Downloads/{file}', f'/Users/taeyoungkim/data100/hw/{file}')
    