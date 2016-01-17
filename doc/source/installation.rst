.. contents::

Installation
===============

You know Python, you know what you're doing:
-----------------------------------------------

**DREAMTools** releases are posted on Pypi repository:: 

    pip install cython
    pip install dreamtools
    
If you have issues, please fill a report with the error message,  python version, platform (https://github.com/dreamtools/dreamtools/issues).    

Please see also the section here below about  "Choosing between Python2.7 or Python3.5", especially for Windows' users under Python3.


For others
------------------

For all platforms, we would recommend to use the Anaconda solution. Please visit https://www.continuum.io/downloads
Choose Python 2 or 3 but install only one version of Anaconda (form that version you can create environment for any Python version). For Window users, please choose Python2.

Under Linux and Mac
^^^^^^^^^^^^^^^^^^^^^^



Once Anaconda is installed, you can install DREAMTools. Ideally, you wish to create a specific environment, install DREAMTools and missing dependencies. Although it is not difficult, we provide a script called `conda_install.sh <https://github.com/dreamtools/dreamtools/blob/master/conda_install.sh>`_ in the source code. The script creates a conda environment called **dreamtools_py2** (or **dreamtools_py3**) and installs the **dreamtools** package from Pypi (latest official release). 

First let us download the script. Open a terminal (unix shell) and download the **conda_install.sh** script as follows::

    curl https://raw.githubusercontent.com/dreamtools/dreamtools/master/conda_install.sh >> conda_install.sh

You can then call it (for Python2 users)::

    sh conda_install.sh --python 2
    
or (for Python3 users)::

    sh conda_install.sh --python 3
    
Under windows
^^^^^^^^^^^^^^^

**Tested under Windows 8 (64 bit)**

#. Install anaconda (https://www.continuum.io/downloads#_windows). **We recommend to use Python2.7** (see 'Choose between Python 2 or 3' section here below). 
#. Install a compiler for windows: http://www.microsoft.com/en-us/download/details.aspx?id=44266


#. Start a new Anaconda shell: Start -> All Program -> Anaconda2 -> Anaconda Prompt
#. In the shell type::

    pip install dreamtools

#. Test if the installation worked::

    dreamtools --help

Choosing between Python2.7 or Python3.5
=======================================

DREAMTools is compatible with Python2 and Python3. More specifically, it is tested (under Travis) for Python 2.7, 3.3, 3.4 and 3.5 under a Linux distribution (Ubuntu).

:Short answer: If you are under Windows, choose 2.7. If you are under Linux or
Mac, keep the one provided with your system. If you know what you are doing
choose a version greater or equal to 2.7

:Long answer: whatever you choose, you would need a compiler. Under Mac and
              Linux, this is generally not an issue since it would be g++. 
              Under Windows, you would need to figure out the best choice. 
              It could be  Visual C or mingw. If you go for the Anaconda
              solution, again under Mac or Linux, **DRFEAMTools** would work
              under Pyhton2 or 3. However, under Windows, we would recommend 
              Python2. Here is the reason: Conda provides pre-compiled packages (e.g., Cython) that use specific version of a compiler (http://docs.continuum.io/anaconda/faq#how-did-you-compile-cpython). No compilers are required for pure Python packages or pre-compiled packages available on Conda. Since DREAMTools uses cython, you should also install a compatible compilee. It appears to be Visual Studio version 2008 for Python 2.7 and is provided by Microsoft (http://www.microsoft.com/en-us/download/details.aspx?id=44266) for free. For python3, so we would recommend to use Python2 under windows. If you still want to go for Python3, you should get Visual C version 2010 (http://stackoverflow.com/questions/29909330/microsoft-visual-c-compiler-for-python-3-4).
