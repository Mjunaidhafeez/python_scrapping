import os
#move files of a folder to another folder one by one

source_folder = r'F:\Data\Encounters_sep_17_22' + '\\'
targe_folder=r'F:\Data\officeallay_Encounters_sep_17_22' + '\\'

def move_files(source_folder,targe_folder):
    try:
        for path, dir, files in os.walk(source_folder):
            if files:
                for file in files:
                    if not os.path.isfile(targe_folder + file):
                        os.rename(path + '\\' + file, targe_folder + file)
        print('All Files Moved Successfully..........')

    except Exception as e:
        print(e)
move_files(source_folder,targe_folder)











