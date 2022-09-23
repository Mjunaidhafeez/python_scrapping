import os

def delete_index_file():
    subfolders = [f.path for f in os.scandir("F:\\Data\\\officeallay_Encounters_sep_17_22") if f.is_dir()]
    for direc in subfolders:
        file_ = direc + '\\index.htm'
        if os.path.isfile(file_):
            os.remove(file_)

delete_index_file()