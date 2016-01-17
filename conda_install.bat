@echo off

@echo: Creating a new conda environment for DREAMTools
@echo: It will be called dreamtools_py2
@echo: If it exists already, its creation will be skipped

IF NOT EXIST Anaconda2\envs\dreamtools_py2 conda create --name dreamtools_py2 python=2.7 

call activate dreamtools_py2

conda install numpy scipy cython matplotlib pandas scikit-learn gevent numpexpr ipython


pip install dreamtools
pip install -U --no-deps

dreamtools --version > version.txt
set /p VERSION=<version.txt

@echo off
@echo Version of DREAMTools %VERSION%
@echo:

python --version>version.txt
set /p VERSION=<version.txt
@echo: %PYTHON%
@echo:
@echo PLEASE, close this terminal, open a new one and activate the conda environement, as follows:: 
@echo:
@echo:
@echo:    activate dreamtools_py2
@echo:
@echo: Once done, check that DREAMTools is available
@echo:
@echo    dreamtools --help
@echo:
pause

