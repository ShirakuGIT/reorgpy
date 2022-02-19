# Works muliplatform on Windows/Mac/Linux
# Currently tested on Ubuntu 21.10

import pathlib
import os
import shutil

# List of file extensions to check
documents = [".pdf", ".txt", ".odt", ".xlsx", ".xcf", ".py", ".cs", ".sh", ".kdenlive", ".xml", ".odp", ".PDF"]
music = [".mp3", ".wav", ".aac", ".ogg", ".alac"]
video = [".mp4", ".mov", ".avi", ".webm", ".wmv", ".mkv", ".srt"]
downloads = [".deb", ".dmg", ".exe", ".app", ".zip", ".bz2", ".torrent"]
pics = [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".raw", ".svg", ".bmp", ".webp"]

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
length = read.split()
templist = read.split("\n")
# The following three lines is just for formatting
temp = ""
for x in templist:
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


def dir_check(dir_name):
	while True:
		dir_path = input(f"\t\t\tEnter path to {dir_name} folder\t\t\t")

		if os.path.exists(dir_path):
			break
		else:
			print("\n\t\t\tTry again, path doesn't exist\n")

	return dir_path


# List of user directories for the check
if read == "" or rewrite == "yes":
	user_dir = open('user_directories.txt', "w+")
	print("")

	user_doc = dir_check("Documents")
	user_mus = dir_check("Music")
	user_dow = dir_check("Downloads")
	user_pic = dir_check("Pictures")
	user_vid = dir_check("Videos")
	user_hom = dir_check("Home")

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
	dir_list = [user_doc, user_mus, user_dow, user_pic, user_vid, user_hom]

else:
	print("Error, try running the program again")


# List of all files' filepaths
all_dir = [user_hom + x for x in os.listdir(user_hom)] + [user_mus + x for x in os.listdir(user_mus)] + [user_pic + x for x in os.listdir(user_pic)] + [user_vid + x for x in os.listdir(user_vid)] + [user_dow + x for x in os.listdir(user_dow)] + [user_doc + x for x in os.listdir(user_doc)]


# Number of files in list
filelen = len(all_dir)

# Closing the file
user_dir.close()

def mover():
	skipped = 0
	moved = 0
	supported_extensions = documents + music + video + downloads + pics

	for i in all_dir:
		if pathlib.Path(i).suffix not in supported_extensions:
			skipped += 1

		elif pathlib.Path(i).suffix in documents and os.path.dirname(i) not in user_doc:
			print(os.path.dirname(i), user_doc)
			moved += 1
			shutil.move(i, user_doc + os.path.basename(i))


		elif pathlib.Path(i).suffix in music and os.path.dirname(i) not in user_mus:
			moved += 1
			shutil.move(i, user_mus + os.path.basename(i))
			

		elif pathlib.Path(i).suffix in video and os.path.dirname(i) not in user_vid:
			moved += 1
			shutil.move(i, user_vid + os.path.basename(i))


		elif pathlib.Path(i).suffix in downloads and os.path.dirname(i) not in user_dow:
			moved += 1
			shutil.move(i, user_dow + os.path.basename(i))


		elif pathlib.Path(i).suffix in pics and os.path.dirname(i) not in user_pic:
			moved += 1
			shutil.move(i, user_pic + os.path.basename(i))

		else:
			pass

	processed = filelen - skipped

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

			   Successfully read {filelen} files, processed {processed} and moved {moved} files
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

