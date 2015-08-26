#!/bin/bash
# instructions to use dreamtools inside a Fedora docker (22)

dnf -y install  python-virtualenv
dnf -y install  numpy
dnf -y install  python-matplotlib
dnf -y install  scipy
dnf -y install  python-pip
# 
pip install --upgrade pip


dnf -y install  python-pandas


#pip install pandas
pip install cython
pip install ipython

dnf -y install  gcc # required to compile the cython code
pip install dreamtools --no-cache
# test it starting a ipython session
