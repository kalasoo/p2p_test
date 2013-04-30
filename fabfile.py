from fabric.api import *
from json import loads
from config import *

# global variables
sender = None
peers = None
env.roledefs = {
	'sender': [],
	'peers': []
}

@task
def run_sender():
	execute(setup_sender, role="sender")

def setup_sender():
	run('hostname')

@task
def run_peers():
	env.parallel = True
	execute(setup_peers, role="peers")

def setup_peers():
	run('hostname')

@task
def setup_config(t = 'nep2p', cf = 'config.json', d = False, l = False):
	global sender, peers
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
	sender = [config['sender']] + config['nodes'].pop(config['sender'])
	peers = [[k] + v for k, v in config['nodes'].iteritems()][:config['num_peer']]
	keys = []

	# add sender to roledefs
	res_sender = resolve(sender[0])
	if res_sender['type'] == 'password':
		env.passwords[res_sender['host']] = res_sender['pw']
	elif res_sender['type'] == 'key':
		keys.append(res_sender['key'])
	env.roledefs['sender'].append(res_sender['host'])
	
	# add peers to roledefs
	for p in peers:
		res = resolve(p[0])
		if res['type'] == 'password':
			env.passwords[res['host']] = res['pw']
		elif res['type'] == 'key' and res['key'] not in keys:
			keys.append(res['key'])
		env.roledefs['peers'].append(res['host'])
	# add keys
	env.key_filename = keys
	print '\tsender:'
	print '\t\t' + str(sender)
	print '\tpeers:'
	for p in peers:
		print '\t\t' + str(p)
	print '\tkey:'
	print '\t\t' + str(env.key_filename)
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



