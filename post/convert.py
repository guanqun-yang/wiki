import pypandoc
import os

pwd = os.getcwd()
# delete all irrelevant files
delete_list = [".tex", ".tex~", ".org~", ".pdf"]
for item in os.listdir(pwd):
  if os.path.isfile(os.path.join(pwd, item)):
    root, ext = os.path.splitext(item)
    if ext in delete_list:
    	os.remove(item)

# converting .org to .rst
for item in os.listdir(pwd):
  if os.path.isfile(os.path.join(pwd, item)):
    root, ext = os.path.splitext(item)
    # prologue.org should not be updated so frequently
    if root == "prologue":
    	continue
    elif ext != ".rst" and ext != ".py":
      pypandoc.convert_file(item, "rst", outputfile=root+".rst", 
                                         extra_args=["-s"])
    else:
    	pass