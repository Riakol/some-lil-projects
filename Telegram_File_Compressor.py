import os
import zipfile
import re


folder_path = 'C:\\test'
files = sorted(list(filter(lambda word: word.split('.')[-1] != 'zip', os.listdir(folder_path))))

#Существует ли архив. Если да, увеличивает цифру в имени на 1. 
#Имя архива - папка с документами
def is_file_exist(path):
    file = sorted(list(filter(lambda word: word.split('.')[-1] == 'zip', os.listdir(path))), key=lambda x: int((x.split('.')[0]).split('_')[-1]))
    if file:
        match = re.search(r'\d+', file[-1])
        if match:
            num = int(match.group())
            res = re.sub(r'\d+', str(num + 1), file[-1])
            return '\\' + res
    else:
        return '\\' + path.split('\\')[-1] + "_1.zip"


len_files = len(files)
last_file = files[:]

while len_files > 0:
    total_size, len_files = 0, len(last_file)
    zip_file_name = folder_path + is_file_exist(folder_path)
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        try:
            for file_name in last_file:
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    total_size += os.path.getsize(file_path)
                    if total_size <= 2e+9:
                        zipf.write(file_path, arcname=file_name)
                    else:
                        last_file = files[files.index(file_name):]
                        break
                len_files -= 1
        except:
            break

