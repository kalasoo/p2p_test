from fabric.api import *
from json import loads
from config import *
from genfile import *

# global variablesi
p2p_type = None 
config = None
sender = None 	# [NAME, PORT, ASID, HOST]
peers = None 	# [NAME, PORT, ASID, HOST]
env.roledefs = {
	'sender': [],
	'peers': []
}

@task
def s(option = 'setup', job = 'all'): 
	#setup => job = ('putfile', 'update', 'all')
	if option not in HOST_OPTIONS:
		print 'Wrong option'
		return
	if option == 'setup':
		gen_nep2p_files([(x[3].split('@')[1], x[2]) for x in peers], sender[1], sender[2], config['log_file'])
		execute(setup_sender, job,  role="sender")
	elif option == 'start':
		execute(start_sender, role="sender")
	elif option == 'check':
		execute(check_host, role="sender")
	elif option == 'end':
		execute(end_host, role="sender")
	elif option == 'getlog':
		execute(getlog, 'sender', sender[0], role="sender")	

def setup_sender(job):
	if job == 'putfile' or job == 'all':
		put('genfiles/*', CONFIG_PATH_BASE)
		with cd(CONFIG_PATH_BASE):
			run('dd if=/dev/urandom of=./{0}.dat bs={1} count=1'.format(config['file_size'], config['file_size']))
	if job == 'update' or job == 'all':
		with cd(CONFIG_PATH_BASE):
			run('python control.py update -v ' + config['version'])

def start_sender():
	with cd(CONFIG_PATH_BASE):
		run('python control.py start -f ' + config['file_size'] + '.dat')
@task
def p(option = 'setup', job = 'all'): 
	#setup => job = ('putfile', 'update', 'all')
	if option not in HOST_OPTIONS:
		print 'Wrong option'
		return
	if option == 'setup':
		for p in peers:
			gen_nep2p_files([], p[1], p[2], config['log_file'])
			execute(setup_peer, job, host=p[3])
	elif option == 'start':
		execute(start_peer, role="peers")
	elif option == 'check':
		execute(check_host, role="peers")
	elif option == 'end':
		execute(end_host, role="peers")
	elif option == 'getlog':
		for p in peers:
			execute(getlog, 'peer', p[0], host=p[3])

def setup_peer(job):
	if job == 'putfile' or job == 'all':
		put('genfiles/*', CONFIG_PATH_BASE)
	if job == 'update' or job == 'all':
		with cd(CONFIG_PATH_BASE):
			run('python control.py update -v ' + config['version'])
@parallel
def start_peer():
	with cd(CONFIG_PATH_BASE):
		run('python control.py start')

@parallel
def check_host():
	with cd(CONFIG_PATH_BASE):
		run('python control.py check')

@parallel
def end_host():
	with cd(CONFIG_PATH_BASE):
		run('python control.py end -r s')

def getlog(r='sender', n=''):
	with cd(CONFIG_PATH_BASE):
		run('python control.py stat')
	if r == 'sender':
		get(CONFIG_PATH_BASE + LOG_PATH_BASE + config['log_file'] + 'stat.json', 'getfiles/' + config['log_file'] + 'stat_sender_'+ n + '.json')
	elif r == 'peer':
		get(CONFIG_PATH_BASE + LOG_PATH_BASE + config['log_file'] + 'stat.json', 'getfiles/' + config['log_file'] + 'stat_peer_' + n + '.json')

@task
def setup(t = 'nep2p', cf = 'config.json', d = False, l = False):
	global p2p_type, config, sender, peers
	# check input
	print 'Check input...'
	if t not in P2P_SYS:
		print 'Wrong P2P system type'
		return
	else:
		p2p_type = t;
		print '\tP2P type:', p2p_type
	try:
		f = open(cf, 'r')
		config = loads(f.read())
		print '\tConfig file:', cf
	except:
		print 'Wrong configuration file'
		return

	d = d if bool(d) else False;
	l = l if bool(l) else False;

	# parse configuration
	print '\nCheck configuration file...'
	if not check_config(config):
		print 'Configuration file is invalid'
		return

	# setup roles
	print '\nSetup roles...'
	# sender & peers
	sender = [config['sender']] + config['nodes'].pop(config['sender'])
	peers = [[k] + v for k, v in config['nodes'].iteritems()][:config['num_peer']]
	keys = []

	# add sender to roledefs
	res_sender = resolve(sender[0])
	sender.append(res_sender['host'])
	if res_sender['type'] == 'password':
		env.passwords[res_sender['host']] = res_sender['pw']
	elif res_sender['type'] == 'key':
		keys.append(res_sender['key'])
	env.roledefs['sender'].append(res_sender['host'])
	
	# add peers to roledefs
	for p in peers:
		res = resolve(p[0])
		p.append(res['host'])
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

def check_config(config):
	if p2p_type == 'nep2p' and config['version'] not in NEP2P_VERSIONS:
		print 'nep2p_version'
		return False
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


