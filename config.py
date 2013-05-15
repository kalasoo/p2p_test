from json import loads

HOST_OPTIONS = ('setup', 'start', 'getlog', 'end', 'check', 'putfile')
P2P_SYS = ('nep2p', 'bt', 'libswft')
FILE_SIZE = ('1K', '10K', '100K', '1M', '5M', '10M', '20M', '30M', '40M', '50M', '100M')
NEP2P_VERSIONS = ('a13', 'a16', 'a16_rudp')
DEFAULT_SENDER = 's8'

CONFIG_PATH_BASE = '~/fyp/fyp_nep2p/'
LOG_PATH_BASE = 'log/'

pl_nodes = loads(open('nodes_addr.json', 'r').read())

resolver = {
	"s8": {
		"host": "cuhk_inc_01@ricepl-1.cs.rice.edu",
		"type": "key",
		"key": "PlanetLabKey",
	},

	"s3": {
		"host": "cuhk_inc_01@plab3.eece.ksu.edu",
		"type": "key",
		"key": "PlanetLabKey",
	},

	"s2": {
		"host": "cuhk_inc_01@planetlab2-santiago.lan.redclara.net",
		"type": "key",
		"key": "PlanetLabKey",
	},

	"s1": {
		"host": "cuhk_inc_01@planetlab4.williams.edu",
		"type": "key",
		"key": "PlanetLabKey",
	},

	"s7": {
		"host": "cuhk_inc_01@planetlab-4.eecs.cwru.edu",
		"type": "key",
		"key": "PlanetLabKey",
	},

	"s6": {
		"host": "cuhk_inc_01@planet3.cs.ucsb.edu",
		"type": "key",
		"key": "PlanetLabKey",
	},

	"s5": {
		"host": "cuhk_inc_01@planetlab2.comp.nus.edu.sg",
		"type": "key",
		"key": "PlanetLabKey",
	},

	"s4": {
		"host": "cuhk_inc_01@planetlab1.eee.hku.hk",
		"type": "key",
		"key": "PlanetLabKey",
	}
}

def resolve(host_name):
	if host_name not in resolver.keys():
		if host_name in pl_nodes:
			return {
				"host": "cuhk_inc_01@" + pl_nodes[host_name][1],
				"type": "key",
				"key": "PlanetLabKey"
			}
		else:
			print 'Wrong host name'
			return False
	return resolver[host_name]
