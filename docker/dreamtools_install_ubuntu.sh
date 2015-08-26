#!/bin/bash
# instructions to use dreamtools inside a Fedora docker (22)

apt-get update
apt-get -y install python-dev
apt-get -y install python-virtualenv
apt-get -y install numpy
apt-get -y install python-matplotlib


apt-get -y install  scipy
apt-get -y install  python-pip
# 
pip install --upgrade pip

apt-get -y install  python-pandas


#pip install pandas
pip install cython
pip install ipython

apt-get -y install  gcc # required to compile the cython code

# pandas 0.13 is installed with apt-get but we want Pandas 0.16
pip install pandas --upgrade

pip install dreamtools --no-cache
# test it starting a ipython session
