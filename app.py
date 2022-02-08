# Works muliplatform on Windows/Mac/Linux
# Currently tested on Ubuntu 21.10

import pathlib
import os
import shutil

# List of file extensions to check
documents = [".pdf", ".txt", ".odt", ".xlsx", ".xcf", ".py", ".cs", ".sh", ".kdenlive", ".xml", ".odp"]
music = [".mp3", ".wav", ".aac", ".ogg", ".alac"]
video = [".mp4", ".mov", ".avi", ".webm", ".wmv"]
downloads = [".deb", ".dmg", ".exe", ".app", ".zip", ".bz2", ".torrent"]
pics = [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".raw", ".svg", ".bmp"]

# Introductory code to ask for rewriting text file
print("""
					PYTHON FILE ORGANIZER v1.1
			-----------------------------------------------------------
	""")


# Open a text file if not exists to save user directories
try:
	user_dir = open('user_directories.txt', "r")
except:
	user_dir = open('user_directories.txt', "w+")

# User directory strings
read = user_dir.read()
# For reading no. of directories
length = read.split("\n")
# The following three lines is just for formatting
temp = ""
for x in length:
	temp += "\t\t\t" + x + "\n"

print(f"""
			List of user directories: 
{temp}
			{str(len(length))} directories present
	""")

print("""
			If you want to rewrite/create your directories,
			type "yes",

			however, if you don't want to do that,
			type "no"
	""")

# Checks if user wants to rewrite his directories
rewrite = input("\t\t\tType here: ")

# List of user directories for the check
if read == "" or rewrite == "yes":
	user_dir = open('user_directories.txt', "w+")
	print("")

	user_doc = input("Enter path to documents folder       ")
	user_mus = input("Enter path to music folder           ")
	user_dow = input("Enter path to downloads folder       ")
	user_pic = input("Enter path to pictures folder        ")
	user_vid = input("Enter path to videos folder          ")
	user_hom = input("Enter path to home directory         ")

	dir_list = [user_doc, user_mus, user_dow, user_pic, user_vid, user_hom]
	# Writes the directories to text file
	for i in dir_list:
		user_dir.write(i + "\n")

	user_dir.close()

elif rewrite == "no":
	read = read.split("\n")
	user_doc = read[0]
	user_mus = read[1]
	user_dow = read[2]
	user_pic = read[3]
	user_vid = read[4]
	user_hom = read[5]

else:
	print("Error, try running the program again")


# List of all files' filepaths
all_dir = [user_hom + x for x in os.listdir(user_hom)] + [user_mus + x for x in os.listdir(user_mus)] + [user_pic + x for x in os.listdir(user_pic)] + [user_vid + x for x in os.listdir(user_vid)] + [user_dow + x for x in os.listdir(user_dow)] + [user_doc + x for x in os.listdir(user_doc)]


# Number of files in list
filelen = len(all_dir)

# Closing the file
user_dir.close()

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
			-----------------------------------------------------------
					
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
			-----------------------------------------------------------
	 
	""")		

##################################################################
# The following code bit is just stylization, nothing too fancy  #
# The highlight of the code is the mover() function, so see that #
##################################################################


# Driver code

print("""
			-----------------------------------------------------------
			Type the following numbers to execute the program:
		
			0 - Yes, you want to run the program
			1 - No, Maybe next time
	""")
user_in = int(input("\t\t\tEnter input here: "))	

if user_in == 0:
	print("\n")
	mover()
elif user_in == 1:
	print("""
			Okay, see you next time!
	""")


# Code by Shivaram Kumar


