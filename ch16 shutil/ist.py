import shutil

# make a copy of this file  with same content
shutil.copy("ist.py", "main2.py") 

# for copy folder with same content
shutil.copytree(".tutorial","mytutorial")

# movefile
import shutil
shutil.move(".tutorial/myfile.txt","myfile.txt")