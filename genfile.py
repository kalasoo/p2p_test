from config import *
from json import dumps, loads

def gen_nep2p_files(nodes, port, asid, log_path):
	gen_nodes(nodes)
	gen_nep2p(port)
	gen_config(asid, log_path)

def gen_nodes(nodes): # n in nodes == [IP, ASID]
	d = {}
	for n in nodes:
		d[n[0]] = n[1]
	json = dumps(d)
	# write to nodes.json
	f = open('genfiles/nodes.json', 'w')
	f.write(json)
	f.close()

def gen_nep2p(port):
	f = open('nep2p/nep2p.json', 'r')
	d = loads(f.read())
	d['external_port'] = port
	json = dumps(d)
	f.close()
	# write to nep2p.json
	f = open('genfiles/nep2p.json', 'w')
	f.write(json)
	f.close()

def gen_config(asid, log_path):
	f = open('nep2p/config.json', 'r')
	d = loads(f.read())
	d['asid'] = asid
	d['log_file_base'] = LOG_PATH_BASE + log_path
	json = dumps(d)
	f.close()
	# write to config.json
	f = open('genfiles/config.json', 'w')
	f.write(json)
	f.close()
