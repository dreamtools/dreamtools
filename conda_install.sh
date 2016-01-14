#!/bin/sh
# For linux and Mac

# Usage: 
#
# sh conda_install_python2.sh
#

# Default python version to be used within conda
PYVER=2
while [[ "$#" > 1 ]]; do case $1 in
    --python) PYVER="$2";;
    *);;
esac; shift
done

CONDA_NAME=dreamtools_py$PYVER

echo "Python version to be used $PYVER"
echo $CONDA_NAME

# If you use sh, then you will need to activate the conda environment manually
cd

echo "Creating a new conda environment for DREAMTools"
echo "It will be called '$CONDA_NAME'"
echo "If it exists already, its creation will be skipped"

if [ ! -d "anaconda/envs/$CONDA_NAME" ]; then
    conda create --name $CONDA_NAME python=$PYVER 
fi

source activate $CONDA_NAME

# Install relevant dependencies that are available on cond
conda install matplotlib cython numpy pandas scipy scikit-learn 

if [ $PYVER == 2 ]
then
    conda install gevent
else
    pip install git+https://git@github.com/cokelaer/synapsePythonClient.git@v1.4.0_py3_dreamtools#egg=synapsePythonClient    
fi

# install DREAMTools itself with dependencies available on pypi
pip install dreamtools 
# Let us make sure the latest version of dreamtools is installed.
pip install dreamtools -U --no-deps


VERSION=$(dreamtools --version)
echo ""
echo ""
echo "Version of DREAMTools installed: $VERSION"
echo -n "Python version:"; echo " $(python --version)"
echo ""
echo "PLEASE, close this terminal, open a new one and activate the conda environement, as follows:: "
echo ""
echo "    source activate $CONDA_NAME"
echo ""
echo "Once done, check that DREAMTools is available:\n\n"
echo "    dreamtools --help"




