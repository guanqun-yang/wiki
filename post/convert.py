import pypandoc
import os

pwd = os.getcwd()
for item in os.listdir(pwd):
  if os.path.isfile(os.path.join(pwd, item)):
    root, ext = os.path.splitext(item)
    if ext != ".rst" and ext != ".py":
      pypandoc.convert_file(item, "rst", outputfile=root+".rst", 
                                         extra_args=["-s"])