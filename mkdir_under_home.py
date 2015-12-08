"""
Checks if a directory exists in the user home directory, if not then create it
""" 

import os			
import sys		
import exceptions													

new_dir = sys.argv[1]	
try:
  	home = os.path.expanduser("~")		# HOME var, or linux command #pwd#
  	print home	
  	path = home + '/' + new_dir											
  	if not os.path.exists(path):
  		print 'make dir', path
    	os.makedirs(path) 
except Exception as e:
	print e