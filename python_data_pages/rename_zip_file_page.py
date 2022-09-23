import os
dir='F:\\Data\\officeallay_Encounters_sep_17_22\\officeallay_Encounters_sep_17_22'

class Rename_zip_file:
    def renam_zip_file(directory_path):
        os.chdir(directory_path)
        files=os.listdir(directory_path)
        print(len(files))
        for file in files:
            new_file=os.listdir(file)
            for i in new_file:
                r = i.replace(" ", "") #replace spaces
                src_path =os.path.join(directory_path,file,i) # original file name
                new_path=os.path.join(directory_path,file,r) #rename file name
                # new_path = os.path.join(directory_path,file, file+'.zip')  # rename file name
                print(src_path)
                print(new_path)
                #replace spaces in files
                # import os
                # for f in os.listdir("."):
                #     r = f.replace(" ", "")
                #     if (r != f):
                #         os.rename(f, r)
                os.rename(src_path,new_path) #renmae function. it will work only to the path define both until did not work this

Rename_zip_file.renam_zip_file(directory_path=dir)






