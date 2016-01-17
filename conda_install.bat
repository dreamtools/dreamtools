set CONDA_NAME=dreamtools_py2

echo Creating a new conda environment for DREAMTools
echo It will be called dreamtools_py2
echo If it exists already, its creation will be skipped

IF NOT EXIST anacondar\envs\dreamtools_py2 GOTO DIREXISTS
conda create --name dreamtools_py2 python=2.7 
:DIREXISTS


activate dreamtools_py2

conda install numpy scipy cython matplotlib pandas scikit-learn gevent numpexp ipython


pip install dreamtools

pip install -U --no-deps

set VERSION=1
echo 
echo 
echo Version of DREAMTools installed: %VERSION%
echo -n "Python version:"; echo " $(python --version)
echo 
echo PLEASE, close this terminal, open a new one and activate the conda environement, as follows:: 
echo 
echo    source activate %CONDA_NAME%
echo 
echo Once done, check that DREAMTools is available:\n\n
echo     dreamtools --help

