import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', choices = ('nep2p', 'bt', 'libswift'), help='specify the type of p2p system')
parser.add_argument('-cf', '--configfile', type=argparse.FileType('r'), help='specify the configuration file')
parser.add_argument('-d', '--debug', help='enable debug mode', action='store_true')
parser.add_argument('-l', '--log', help='enable log mode', action='store_true')
args = parser.parse_args()

print args