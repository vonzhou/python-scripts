"""
Rename files with old_ext extension in a dir  to new_ext extension
"""
import os														
import sys															

work_dir=sys.argv[1]										
old_ext=sys.argv[2]										
new_ext=sys.argv[3]										

files = os.listdir(work_dir)	# file name list
# print files								
for filename in files:											
  file_ext = os.path.splitext(filename)[1]	# Get the file extension
  if old_ext == file_ext:										
    newfile = filename.replace(old_ext, new_ext)	
    os.rename(													
	    os.path.join(work_dir, filename),
		os.path.join(work_dir, newfile))