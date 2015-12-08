"""
scan the current directory and all subdirectories and display the size.
"""

import os 														
import sys


directory = sys.argv[1]												
dir_size = 0	
# os.walk() return 3 tuple <current dir path, dir list, file list>												
for (path, dirs, files) in os.walk(directory):			
  for f in files:												
    filename = os.path.join(path, f)
    dir_size += os.path.getsize(filename)	

print "Folder Size in Bytes = %0.2f Bytes" % (dir_size)
print "Folder Size in Kilobytes = %0.2f KB" % (dir_size/1024.0)
print "Folder Size in Megabytes = %0.2f MB" % (dir_size/1024/1024.0)
print "Folder Size in Gigabytes = %0.2f GB" % (dir_size/1024/1024/1024.0)