from fabric.api import *
from json import loads

def p2p_test(t = 'nep2p', cf = 'config.json', d = False, l = False):
	#check input
	if t not in ('nep2p', 'bt', 'libswift'):
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

	print t, cf, d, l 
	print config
