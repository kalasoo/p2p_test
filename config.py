from json import loads

HOST_OPTIONS = ('setup', 'start', 'getlog')
P2P_SYS = ('nep2p', 'bt', 'libswft')
FILE_SIZE = ('1K', '10K', '100K', '1M', '10M')
DEFAULT_SENDER = 'p2plab'
CONFIG_PATH_BASE = '~/fyp/fyp_nep2p/'
LOG_PATH_BASE = 'log/'

pl_nodes = loads(open('nodes_addr.json', 'r').read())

print pl_nodes

resolver = {
	"p2plab": {
		"host": "yingshaun@137.189.97.35",
		"type": "password",
		"pw": "1991522"
	},
	"yxhaws": {
		"host": "ubuntu@54.248.144.148",
		"type": "key",
		"key": "yxhawsKey"
	},
	"ymaws": {
		"host": "ubuntu@122.248.235.241",
		"type": "key",
		"key": "ymawsKey"
	}
}

def resolve(host_name):
	if host_name not in resolver.keys():
		if host_name in pl_nodes:
			return {
				"host": "ubuntu@" + pl_nodes[host_name][0],
				"type": "key",
				"key": "PlanetLabKey"
			}
		else:
			print 'Wrong host name'
			return False
	return resolver[host_name]
