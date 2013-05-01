from json import loads

P2P_SYS = ('nep2p', 'bt', 'libswft')
FILE_SIZE = ('1K', '10K', '100K', '1M', '10M')
DEFAULT_SENDER = 'p2plab'

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
	},
	"s1": {
		"host": "cuhk_inc_01@planetlab4.williams.edu",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s2": {
		"host": "cuhk_inc_01@planetlab2.fri.uni-lj.si",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s3": {
		"host": "cuhk_inc_01@planetlab2-santiago.lan.redclara.net",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s4": {
		"host": "cuhk_inc_01@pl1snu.koren.kr",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s5": {
		"host": "cuhk_inc_01@plab3.eece.ksu.edu",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s6": {
		"host": "cuhk_inc_01@planetlab-3.cmcl.cs.cmu.edu",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s7": {
		"host": "cuhk_inc_01@planetlab-03.cs.princeton.edu",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s8": {
		"host": "cuhk_inc_01@planet-lab2.itba.edu.ar",
		"type": "key",
		"key": "PlanetLabKey"
	},
	"s9": {
		"host": "cuhk_inc_01@pl02.comp.polyu.edu.hk",
		"type": "key",
		"key": "PlanetLabKey"
	}
}

def resolve(host_name):
	if host_name not in resolver.keys():
		print 'Wrong host name'
		return False
	return resolver[host_name]
