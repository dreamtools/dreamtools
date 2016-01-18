.. contents::


.. _installation:

Installation
===============

You know Python, you know what you're doing:
-----------------------------------------------

**DREAMTools** releases are posted on Pypi repository. It your system is already configured (you have **pip** and all libraries for development), these commands should install dreamtools and its dependencies (e.g., numpy, scipy, pandas...)::

    pip install cython
    pip install dreamtools

If you have issues, please fill a report with the error message,  python version, platform (https://github.com/dreamtools/dreamtools/issues).

Please see also the section here below about  "Choosing between Python2.7 or Python3.5", especially for Windows' users under Python3.


You are a Python's beginner or use Anaconda:
---------------------------------------------------

For all platforms, we would recommend to use the Anaconda solution. Please visit https://www.continuum.io/downloads
Choose Python 2 or 3 but install only one version of Anaconda (from that version you can create environments for any Python version). For Window users, please choose Python2.

Under Linux and Mac
^^^^^^^^^^^^^^^^^^^^^^

Once Anaconda is available, you can install DREAMTools within a new **conda** environment.

There are 3 steps to follow:

#. create a specific environment and activate it
#. install dependencies
#. install DREAMTools

Here below are the instructions for a Python2.7 environment.

Open a shell and then type::

    conda create -n dreamtools_py2 python=2.7

Then, activate the environment (you would need to type that command each time you open a new anaconda prompt)::

    source activate dreamtools_py2

Install some dependencies::

    conda install matplotlib numpy scipy cython matplotlib pandas scikit-learn numexpr ipython

Note that for python2, you should also install gevent::

    conda install gevent

Finally, install **DREAMTools** itself::

    pip install dreamtools

Type this command to check that the standalone application is available::

    dreamtools --help

We also provide a script called `conda_install.sh <https://github.com/dreamtools/dreamtools/blob/master/conda_install.sh>`_ in the source code that does the installation for you. The script creates a conda environment called **dreamtools_py2** (or **dreamtools_py3**) and installs the **dreamtools** package from Pypi (latest official release). For Mac or Linux users save the following file in your home directory: `conda_install.sh <https://raw.githubusercontent.com/dreamtools/dreamtools/master/conda_install.sh>`_.

You can then call it (for Python2 users)::

    sh conda_install.sh --python 2

or (for Python3 users)::

    sh conda_install.sh --python 3


Under windows
^^^^^^^^^^^^^^^

**Tested under Windows 8 (64 bit) with Anaconda for Python2.7**

#. Install a compiler for windows that is compatible with Python2.7 provided in Anaconda2: http://www.microsoft.com/en-us/download/details.aspx?id=44266


#. Download the following script: `conda_install.bat <https://raw.githubusercontent.com/dreamtools/dreamtools/master/conda_install.bat>`_.

#. Start a new Anaconda shell: Start -> All Program -> Anaconda2 -> Anaconda Prompt

#. Execute the script::

   conda_install.bat

The instructions are equivalent to the Linux/Mac case::

    conda create --name dreamtools_py2 python=2.7
    activate dreamtools_py2
    conda install numpy scipy cython matplotlib pandas scikit-learn gevent
    conda install numpexpr ipython
    pip install dreamtools
    pip install -U --no-deps
    activate dreamtools_py2

Each time you open a new shell, you will need to activate the conda
environment::

    activate dreamtools_py2



Choosing between Python2.7 or Python3.5
=======================================

**DREAMTools** is compatible with Python2 and Python3. More specifically, it is tested (under Travis) for Python 2.7, 3.3, 3.4 and 3.5 under a Linux distribution (Ubuntu).

If you know Python, you can choose either Python2 or Python3.

Otherwise, if you decided to go for Anaconda (highly recommended), then 
you can choose Python2 or Python3 except for Window's user who should 
use Python2.

In addition, you will need to install a compiler that is compatible with what
was used by Anaconda to compile the libraries such as numpy. This should not
be a worry under Linux or Mac platforms. However, under Windows, pre-compiled 
packages (e.g., Cython) used a specific version of 
a compiler (http://docs.continuum.io/anaconda/faq#how-did-you-compile-cpython).
It appears to be Visual Studio version 2008 for Python 2.7 and is provided by Microsoft (http://www.microsoft.com/en-us/download/details.aspx?id=44266) for free. For python3, there is no specific compiled provided (Jan 2016).  If you still want to go for Python3, you should get Visual C version 2010 (http://stackoverflow.com/questions/29909330/microsoft-visual-c-compiler-for-python-3-4).


Note for Python3.X
==========================

**DREAMTools** is compatible with Python2 and Python3. However, **DREAMTools** depends on a package (synapseclient) that is currently not available for Python3 on Pypi website (pip won't provide a Python3-compatible package). As a temporary
solution, we forked this package and provide a compatible version.  You will need to install it manually as follows::

    pip install git+https://git@github.com/cokelaer/synapsePythonClient.git@v1.4.0_py3_dreamtools#egg=synapsePythonClient








