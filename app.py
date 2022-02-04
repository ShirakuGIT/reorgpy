# Python program that reorgnizes directories
# Works muliplatform on Windows/Mac/Linux
# Currently tested on Ubuntu 21.10

import pathlib
import os
import shutil

# List of file extensions to check
documents = [".pdf", ".txt", ".odt", ".xlsx", ".xcf", ".py", ".cs"]
music = [".mp3", ".wav", ".aac", ".ogg", ".alac"]
video = [".mp4", ".mov", ".avi", ".webm", ".wmv"]
downloads = [".deb", ".dmg", ".exe", ".app", ".zip", ".bz2", ".torrent"]
pics = [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".raw", ".svg", ".bmp"]



# List of user directories for the check
user_doc = r'/home/shiraku/Documents/'
user_mus = r'/home/shiraku/Music/'
user_dow = r'/home/shiraku/Downloads/'
user_pic = r'/home/shiraku/Pictures/'
user_vid = r'/home/shiraku/Videos/'
user_hom = r'/home/shiraku/'
user_mis = r'/home/shiraku/Misc/'

# List of all files' filepaths
all_dir = [user_hom + x for x in os.listdir(user_hom)] + [user_mus + x for x in os.listdir(user_mus)] + [user_pic + x for x in os.listdir(user_pic)] + [user_vid + x for x in os.listdir(user_vid)] + [user_dow + x for x in os.listdir(user_dow)] + [user_doc + x for x in os.listdir(user_doc)]


# Number of files in list
filelen = len(all_dir)

# For loop iteration to move the files to their directories
def mover():
	for i in all_dir:

		
		if pathlib.Path(i).suffix in documents:
			shutil.move(i, user_doc + os.path.basename(i))


		elif pathlib.Path(i).suffix in music:
			shutil.move(i, user_mus + os.path.basename(i))
			

		elif pathlib.Path(i).suffix in video:
			shutil.move(i, user_vid + os.path.basename(i))


		elif pathlib.Path(i).suffix in downloads:
			shutil.move(i, user_dow + os.path.basename(i))


		elif pathlib.Path(i).suffix in pics:
			shutil.move(i, user_pic + os.path.basename(i))

		
		else:
			pass

	#Success statement
	print(fr"""
	___________________________________________
			
			   _
			  |)`
			  | |
			  | |_____
			 /    (]__)
			/    (]___)
		       /    (]___)
			  ___(]_)
			 /
			/

	   Successfully moved {filelen} files  
	___________________________________________
	 
	""")		

##################################################################
# The following code bit is just stylization, nothing too fancy  #
# The highlight of the code is the mover() function, so see that #
##################################################################

# Take user request
print("\n  Hey! Do you wanna organize your files?\n")
print("""
  Type the following numbers to execute the program:
	
	0 - Yes, you want to run the program
	1 - No, Maybe next time
""")
user_in = int(input("""
	Type your response here:
	
		"""))
# Driver code
if user_in == 0:
	print("\n")
	mover()
elif user_in == 1:
	print("""
	Okay, see you next time!
	""")


# Code by Shivaram Kumar


