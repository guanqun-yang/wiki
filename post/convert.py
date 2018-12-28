import pypandoc
import subprocess
import os
import re

pwd = os.getcwd()
# convert all .org files into .tex files using emacs command line tool
for item in os.listdir(pwd):
    if os.path.isfile(os.path.join(pwd, item)):
        root, ext = os.path.splitext(item)
        if ext == ".org":
            subprocess.run(["emacs", "--batch", item, "-f", "org-latex-export-to-latex"])
            
# converting .org to .rst
for item in os.listdir(pwd):
    if os.path.isfile(os.path.join(pwd, item)):
        root, ext = os.path.splitext(item)
        # prologue should not be updated so frequently
        if root == "prologue":
            continue 

        if ext == ".tex":
            pypandoc.convert_file(item, "rst", outputfile=root+".rst", 
                                               extra_args=["-s"])

# delete all irrelevant files
delete_list = [".tex", ".tex~", ".org~", ".pdf"]
for item in os.listdir(pwd):
    if os.path.isfile(os.path.join(pwd, item)):
        root, ext = os.path.splitext(item)
        if ext in delete_list:
    	    os.remove(item)

# remove section reference to avoid errors
for item in os.listdir(pwd):
    if os.path.isfile(os.path.join(pwd, item)):
        root, ext = os.path.splitext(item)
        if ext == ".rst":
        	line_list = []
        	with open(item, "r") as file_object:
        		lines = file_object.readlines()
        		for line in lines:
	        		if re.match(r"^.. _sec", line) == None:
	        			line_list.append(line)

        	with open(item, "w") as file_object:
        		for line in line_list:
        			file_object.write(line)