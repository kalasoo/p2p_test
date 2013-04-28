from fabric.api import *
from json import loads
from config import *

def p2p_test(t = 'nep2p', cf = 'config.json', d = False, l = False):
	# check input
	print 'Check input ...'
	if t not in P2P_SYS:
		print 'Wrong P2P system type'
		return
	try:
		f = open(cf, 'r')
		config = loads(f.read())
	except:
		print 'Wrong configuration file'
		return

	d = d if bool(d) else False;
	l = l if bool(l) else False;
	print 'Valid input\n'

	# parse configuration
	print 'Check configuration file...'
	if not check_config(config):
		print 'Configuration file is invalid'
		return
	else:
		print 'Configuration file is valid\n'

	# setup roles
	print 'Setup roles...'
	# sender & peers
	sender = config['nodes'].pop(config['sender'])
	peers = [v for v in config['nodes'].values()][:config['num_peer']]
	# roles
	env.roledef = {
		'sender': sender[0],
		'peers': [p[0] for p in peers]
	}
	print env.roledef
	print 'Roles are deployed\n'



def check_config(config):
	if config['file_size'] not in FILE_SIZE:
		print 'file_size'
		return False
	if config['num_init_peer'] <= 0:
		print 'num_init_peer'
		return False
	if config['num_peer'] <= 0:
		print 'num_peer'
		return False
	if len(config['nodes']) <= 1:
		print 'nodes'
		return False
	if config['sender'] == None:
		config['sender'] = DEFAULT_SENDER
	elif config['sender'] not in config['nodes'].keys():
		print 'sender'
		return False 
	return True
