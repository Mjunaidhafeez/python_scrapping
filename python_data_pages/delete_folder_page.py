import os
import shutil

def delete_index_folder():
    subfolders = [f.path for f in os.scandir("F:\\Data\\\officeallay_Encounters_sep_17_22") if f.is_dir()]
    for direc in subfolders:
        file_ = direc + '\\Signatures'
        if os.path.isdir(file_):
            shutil.rmtree(file_)

delete_index_folder()