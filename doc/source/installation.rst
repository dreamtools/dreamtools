.. contents::


.. _installation:

Installation
===============

Familiar with Python ecosystem ?
-----------------------------------

If you are familiar with Python and the **pip** application and your system
is already configured (compilers, development libraries available), these
two commands should install **DREAMTools** and its dependencies (in unix or
windows terminal)::

    pip install cython
    pip install dreamtools

If you do not have dependencies installed yet (e.g., pandas, numpy, scipy), this
may take a while depending on your system (typically 10-15 minutes). If you are 
in a hurry or do not want to compile libraries, see the Anaconda solution here below.

If you are new to Python
-----------------------------------

If you are not familiar with Python, or have issues with the previous method
(e.g., compilation failure), or do not have root access, we would recommend to
use the `Anaconda <https://www.continuum.io/downloads>`_ solution.

Anaconda is a free Python distribution. It includes most popular Python packages
for science and data analysis and has dedicated channels. One such channel is
called `bioconda >https://bioconda.github.io/>`_ and complements the default
channel (conda) with a set of packages dedicated to life science.

We have included **DREAMTools** in **bioconda** channel. So, once Anaconda is installed,
you first need to add the **bioconda** channel to your environment (and R
channel)::

    conda config --add channels r
    conda config --add channels bioconda

This should be done only once. Then, install **DREAMTools** itself::

    conda install dreamtools

This command should install **DREAMTools** in your default conda environment. If
you wish to try **DREAMTools** in another (independent) environment (e.g., a 
different python version), you would need to create and activate the environment first::

    conda create --name test_dreamtools python=3.5
    source activate test_dreamtools
    conda install dreamtools



Installation from source
-----------------------------------

The previous methods relies on released versions of **DREAMTools**. If a new
feature is only available in the source code, then you will need to get the
source code, which is available in the github repository::

   git clone git@github.com:dreamtools/dreamtools.git
   cd dreamtools
   python setup.py install

Dependencies (e.g. Pandas) will need to be compiled or pre-installed (see
above).


Note for Windows and Anaconda
-----------------------------------

We do not provide any DREAMTools package on **bioconda** for Windows.

However, if you use Anaconda and decide to compile the source yourself under Windows, then you will
have to install a compiler that is compatible with Anaconda. In other words, you will have to use the same compiled as the one used by Anaconda.


For Python 2.7, compilation should work easily. You need to know that pre-compiled  packages (e.g., Cython) used a specific version of a compiler (http://docs.continuum.io/anaconda/faq#how-did-you-compile-cpython), which is Visual Studio version 2008  and is provided by Microsoft (http://www.microsoft.com/en-us/download/details.aspx?id=44266) for free.

For Python3.4 and 3.5, this is a bit more difficult. You should get Visual C version 2010 (http://stackoverflow.com/questions/29909330/microsoft-visual-c-compiler-for-python-3-4) or for Python 3.5 another Visual C version 2015. This may change with time but this information was found on Anaconda documentation (March 2016). You may found useful information here as well for VS2015:  http://www.microsoft.com/en-us/download/details.aspx?id=44266


Note for Python2.X and Python3.X
-----------------------------------

**DREAMTools** is compatible with Python2.7, Python3.4, Python3.5. The
**bioconda** channel provide these 3 versions. If you still want to use
Python2.6 or 3.3, **DREAMTools** may work as well but you would need to compile
the dependencies yourself.

