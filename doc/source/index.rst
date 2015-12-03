


############################################################################
DREAMTools
############################################################################

.. image:: https://badge.fury.io/py/dreamtools.svg
    :target: https://pypi.python.org/pypi/dreamtools

.. image:: https://secure.travis-ci.org/dreamtools/dreamtools.png
     :target: http://travis-ci.org/dreamtools/dreamtools

.. image:: https://coveralls.io/repos/dreamtools/dreamtools/badge.png?branch=master
    :target: https://coveralls.io/r/dreamtools/dreamtools?branch=master

.. image::  https://badge.waffle.io/dreamtools/dreamtools.png?label=issues&title=issues
    :target: https://waffle.io/dreamtools/dreamtools
        
.. image:: https://zenodo.org/badge/18543/dreamtools/dreamtools.svg
    :target: https://zenodo.org/badge/latestdoi/18543/dreamtools/dreamtools

:Note: DREAMTools is tested for Python 2.7
:Contributions: Please join https://github.com/dreamtools/dreamtools and share
  your notebooks https://github.com/dreamtools/dreamtools/notebooks
:Online documentation: 
    `On pypi website <http://pythonhosted.org/dreamtools/>`_
:Issues and bug reports: 
    `On github <https://github.com/dreamtools/dreamtools/issues>`_
:How to cite: Cokelaer T, Bansal M, Bare C et al. DREAMTools: a Python 
    package for scoring collaborative challenges [version 1; referees: 
    awaiting peer review] F1000Research 2015, 4:1030 
    (doi: 10.12688/f1000research.7118.1)
    `F1000 link <http://f1000research.com/articles/4-1030/v1>`_


.. contents::

Overview
---------

**DREAMTools** aims at sharing code used in the scoring of `DREAM <http://dreamchallenges.org>`_ challenges.

The main goals are to provide:

#. scoring functions for the DREAM challenges for **end-users** via the **dreamtools** standalone application.
#. a place for **developers** involved in the DREAM challenges to share code


Code related to aggregation, leaderboards, or more complex analysis are not
guaranteed to be found in DREAMTools even though it may be in some challenges
(e.g. D8C1). Some functionalities may be restricted with some access to synapse.
Some challenges will require to download public data sets from
`Synapse <www.synapse.org>`_ , **in which case you will need to register and
accept the terms of agreements**.

The **dreamtools** executable
-------------------------------

For users, **DREAMTools** package provides an executable called **dreamtools**, which should be installed automatically during the installation. Knowing the name of the challenge (and possibly sub-challenge), it works as follows::

    dreamtools --challenge d8c1 --sub-challenge sc1a --submission example.zip

It prints some information and the score of the submission for instance for the example above::

     Solution for alphabeta-Network.zip in challenge d8c1 (sub-challenge sc1a) is :
     AUROC: 0.781937275711

Available challenges
-------------------------

The primary goal of **DREAMTools** is to provide scoring functions used in all DREAM challenges. Currently,
**DREAMTools** includes about 80% of DREAM challenges from DREAM2 to DREAM9.5

Most of them are implemented in pure Python. A couple rely on Perl script and
5-6 call R behind the scene. However, the user interface is identical for all of them.

Installation
---------------

**DREAMTools** depends on a few libraries such as Pandas, Numpy, Matplotlib. They should be automatically
installed with **DREAMTools** using pip executable (note the small caps)::

    pip install dreamtools

From source, download the source code and install the package with Python::

    git clone git@github.com:dreamtools/dreamtools.git
    cd dreamtools
    sudo python setup.py install



te for Python3.X
~~~~~~~~~~~~~~~~~~~~~~
**DREAMTools** is compatible with Python2 and Python3. However, 
**DREAMTools** depends on a package that is currently not available for Python3
(synapseclient). As a temporary solution, we forked this package and provide
a version compatible for Python3 and **DREAMTools**.  You will need to install
it manually as follows::

    pip install git+https://git@github.com/cokelaer/synapsePythonClient.git@v1.4.0_py3_dreamtools#egg=synapsePythonClient

Then, as above, type::    

    # if you do not have cython already installed:
    pip install cython

and::

    pip install dreamtools

If you are new to Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are not familiar with Python, or have issues with the previous method
(e.g., compilation failure), or do not have root access, we would recommend to
use the `Anaconda <https://www.continuum.io/downloads>`_ solution.

Anaconda is a free Python distribution. It includes most popular Python packages for science and data analysis. Anaconda will install the software required by
**DREAMTools**. Since it does not require root access, it should not interfere with your system.

Please, visit the `Anaconda <https://www.continuum.io/downloads>`_ website 
and follow the instructions. You may need to
choose between 2 versions of Python (2.X or 3.5). **DREAMTools** is tested under Python 2.7 and 3.5 so the version should not matter.







Issues
-----------

Please fill bug report in https://github.com/dreamtools/dreamtools/issues


Contributions
----------------

Please join https://github.com/dreamtools/dreamtools

User Guide
------------

.. toctree::
    :maxdepth: 1

    userguide.rst

Others
--------

Note that in the Github directory, each challenge directory has its own README.rst file, which
contains basic usage and information about the challenge.

.. toctree::
    :maxdepth: 1

    developers.rst
    credits.rst
    references.rst
    changelog.rst
