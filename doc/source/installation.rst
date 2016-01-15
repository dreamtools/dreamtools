.. contents::

Installation
===============

Using Anaconda
------------------

Under Linux and Mac
^^^^^^^^^^^^^^^^^^^^^^

We provide a script called **conda_install.sh** in the source code. You can call it as follows:;

    sh conda_install.sh --python 2
    
or::

    sh conda_install.sh --python 2
    
The script creates a conda environment called **dreamtools_py2** (or **dreamtools_py3**) and installs the **dreamtools** package from Pypi (latest official release).

Under windows
^^^^^^^^^^^^^^^

**Tested under Windows 8 (64 bit)**

#. Install anaconda (https://www.continuum.io/downloads#_windows). We recommend to use Python2.7 (see choosing Python 2 or 3 section here below). 
#. For those who still want to use PYthon3, install git.
#. Install a compiler for windows: http://www.microsoft.com/en-us/download/details.aspx?id=44266

Conda provides pre-compiled packages (e.g., Cython) that used specific version of compiler (http://docs.continuum.io/anaconda/faq#how-did-you-compile-cpython). DREAMTools uses cython and therefore Python expects the compiler to be found on your system . You must install a compatible compiled. It appears to be Visual Studio version 2008 for Python 2.7 and is provided by Microsoft (http://www.microsoft.com/en-us/download/details.aspx?id=44266 ). For python3, we did not find the compiler but should be a VS version 2010 (http://stackoverflow.com/questions/29909330/microsoft-visual-c-compiler-for-python-3-4)


#. Start a new Anaconda shell: Start -> All Program -> Anaconda2 -> Anaconda Prompt
#. In the shell type::

    pip install dreamtools

#. Test if the installation worked::

    dreamtools --help

Choosing between Python2.7 or Python3.5
=======================================

DREAMTools is compatible with Python2 and Python3. More specifically, it is tested (under Travis) for Python 2.7, 3.3, 3.4 and 3.5. It may work for other versions of course. 

For new Python users, we would recommend to install Anaconda, which provides a bunch of packages already pre-compiled. This saves lost of time and technical issues. Yet, you will have to choose between Python2 or Python3. Under Linux or Mac, there is no preferences. However, under Windows, we would recommend Python2. Indeed, you will need a compiler and we easily found a compiler for Python2 (Visual C++ for Python2 provided by Microsoft -- see above) but it was not that obvious for Python3. 




