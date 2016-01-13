#!/bin/sh

# For linux and Mac

cd

if [ -d "anaconda/envs/dreamtools_conda" ]; then
    conda create --name dreamtools_conda python=2 
fi

source activate dreamtools_conda

# Install relevant dependencies that are available on cond
conda install matplotlib cython numpy pandas scipy scikit-learn gevent

# install DREAMTools itself with dependencies available on pypi
pip install dreamtools  -U --no-deps



export PYTHONPATH=$CONDA_ENV_PATH/lib/python2.7/site-packages

VERSION = $(dreamtools --version)
echo "Version of DREAMTools installed: $VERSION"




