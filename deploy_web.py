#!/usr/bin/env python
from json import loads, dumps
import shutil

f = open('config.json', 'r')

config = loads(f.read())

src = 'getfiles/' + config['log_file']
dst = '/home/ubuntu/fyp/fyp_demo/data/' + config['log_file']

shutil.copytree(src, dst)
