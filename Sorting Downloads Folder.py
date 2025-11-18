import os
import shutil

a = os.getcwd()
print("The current working directory is",a)
home_folder = os.path.expanduser('~')
dpath = os.path.join(home_folder, 'Downloads')
path = "C:\Books\College"
os.chdir(dpath)
b = os.getcwd()
print("Now the current working directory is",b)
files = os.listdir()
result={"Moved":0,"Deleted":0,"Space_Saved":0}
for i in files:
    if i.endswith(('.jpg','.png','.jpeg','.gif')):
        if not os.path.exists('Images'):
            os.makedirs('Images')
        shutil.move(i,f'Images/{i}')
        print(f"Moved {i} to Images")
        result['Moved']+=1

    elif i.endswith(('.pdf','.docx','.txt')):
        if not os.path.exists('Documents'):
            os.makedirs("Documents")
        shutil.move(i,f'Documents/{i}')
        print(f"Moved {i} to Documents")
        result['Moved'] += 1


    elif i.endswith(('.exe','.zip','.dmg')):
        if not os.path.exists('Installations'):
            os.makedirs("Installations")
        shutil.move(i,f'Installations/{i}')
        print(f"Moved {i} to Installations")
        result['Moved'] += 1

    elif i.endswith(('.mp4','.mkv','.webm')):
        if not os.path.exists('Videos'):
            os.makedirs("Videos")
        shutil.move(i,f"Videos/{i}")
        print(f"Moved {i} to Videos")
        result['Moved'] += 1

    elif i.endswith(('.temp','.tmp','.log')):
        os.remove(i)
        size = os.path.getsize(i)/(1024*1024)
        result['Deleted'] += 1
        result['Space_Saved']+= size

print("\n" + "="*30)
print(" CLEANUP REPORT ")
print("="*30)
print("Files Moved:",result['Moved'])
print("Files Deleted:",result['Deleted'])
print(f"Disk Space Saved: {result['Space_Saved']:.2f} MB")
print("="*30)















