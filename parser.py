import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
	'-t', 
	'--type', 
	choices = ('nep2p', 'bt', 'libswift'), 
	default = 'nep2p',
	help='specify the type of p2p system (default: nep2p)'
)
parser.add_argument(
	'-cf', 
	'--configfile', 
	type = argparse.FileType('r'), 
	default = 'config.json',
	help ='specify the configuration file (default: config.json)'
)
parser.add_argument(
	'-d', 
	'--debug', 
	help='enable debug mode', 
	action='store_true'
)
parser.add_argument(
	'-l', 
	'--log', 
	help='enable log mode', 
	action='store_true'
)
args = parser.parse_args()