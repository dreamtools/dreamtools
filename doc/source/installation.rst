.. contents::


.. _installation:

Installation
===============

Familiar with Python ecosystem ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are familiar with Python and the **pip** application and your system
is already configured (compilers, development libraries available)), these
two commands should install **DREAMTools** and its dependencies (in unix or
windows terminal)::

    pip install cython
    pip install dreamtools

If you do not have dependencies installed yet (e.g pandas, numpy, scipy), this
make take a while (e.g., 10-15 minutes). If you are in a hurry, see the Anaconda
solution here below.

If you are new to Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are not familiar with Python, or have issues with the previous method
(e.g., compilation failure), or do not have root access, we would recommend to
use the `Anaconda <https://www.continuum.io/downloads>`_ solution.

Anaconda is a free Python distribution. It includes most popular Python packages
for science and data analysis and has dedicated channels. One such channel is
called **bioconda** and complements the default channel (conda) with a set of 
packages dedicated to life science.

We have included **DREAMTools** in **bioconda**. So, once Anaconda is installed, 
you first need to add **bioconda** channel to your environment (and R)::

    conda config --add channels r
    conda config --add channels bioconda

This should be done only once. Then, install **DREAMTools** itself::

    conda install dreamtools

This command should install **DREAMTools** in your default conda environment. If
you wish
to try **DREAMTools** in another environment (e.g different python version), you
would need to create a new one and then install **DREAMTools** in that
environment::

    conda create --name test_dreamtools --python 3.5
    source activate test_dreamtools
    conda install dreamtools


If there is an issue, please visit the :ref:`installation` page
(doc/source/installation.rst) where details about the installation scripts can
be found.


Installation from source
~~~~~~~~~~~~~~~~~~~~~~~~~

The command::

    pip install dreamtools

install the latest release of **DREAMTools**. If you prefer to use the
source code, you can also get     the github repository and install
**DREAMTools** as
follows (dependencies such as numpy or scipy will need to be compiled if
not found)::


   git clone git@github.com:dreamtools/dreamtools.git
   cd dreamtools
   python setup.py install



Note for Windows
=======================================

If you decide to compile the source yourself under windows, you will 
have to install a compiler that is compatible with what
was used by Anaconda to compile the libraries such as numpy. This should not
be a worry under Linux or Mac platforms. However, under Windows, pre-compiled 
packages (e.g., Cython) used a specific version of 
a compiler (http://docs.continuum.io/anaconda/faq#how-did-you-compile-cpython).

It appears to be Visual Studio version 2008 for Python 2.7 and is provided by Microsoft (http://www.microsoft.com/en-us/download/details.aspx?id=44266) for free. However, for python3, there is no specific compiled provided (Jan 2016). If you still want to go for Python3, you should get Visual C version 2010 (http://stackoverflow.com/questions/29909330/microsoft-visual-c-compiler-for-python-3-4).


Note for Python2.X and Python3.X
==================================

**DREAMTools** is compatible with Python2.7, Python3.4, Python3.5. The
**bioconda** channel provide these 3 versions. If you still want to use
Python2.6 or 3.3, **DREAMTools** may work as well but you would need to compile
the dependencies yourself.

