#!/bin/bash

mkdir genfiles
mkdir getfiles

wget https://www.dropbox.com/s/pa7syp5krrymhsu/Key.zip
unzip Key.zip
rm Key.zip

wget -O genfiles/control.py https://raw.github.com/xuancaishaun/fyp_test/master/control.py
