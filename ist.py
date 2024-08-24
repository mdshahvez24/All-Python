import shutil

# make a copy of this file  with same content
shutil.copy("ist.py", "main2.py") 

# for copy folder with same content
shutil.copytree(".tutorial","mytutorial")

# import shutil
# shutil.move(".tutorial/file.file","file.file")

# for remove a folder 
import shutil
shutil.rmtree("tutorial")