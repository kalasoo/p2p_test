#!/usr/bin/python

from parser import *
from json import load, loads

print args
try:
	cfile = load(args.configfile)
except:
	print 'Incorrect config file'
	exit()

# read configuration file

# write sender_config.json

# write peer_config.json



