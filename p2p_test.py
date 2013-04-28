#!/usr/bin/python

from parser import *
from json import load, loads

print args

# read configuration file
try:
	config = load(args.configfile)
except:
	print 'Incorrect config file'
	exit()

# write sender_config.json
sender = {
	'ip': config.nodes['p2plab'],
	'asid': config.asid,
	'ext_port': config.ext_port
}

# write peer_config.json