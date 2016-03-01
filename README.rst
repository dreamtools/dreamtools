############################################################################
DREAMTools
############################################################################

.. image:: https://badge.fury.io/py/dreamtools.svg
    :target: https://pypi.python.org/pypi/dreamtools

.. image:: https://secure.travis-ci.org/dreamtools/dreamtools.png
    :target: http://travis-ci.org/dreamtools/dreamtools

.. image:: https://coveralls.io/repos/dreamtools/dreamtools/badge.png?branch=master
   :target: https://coveralls.io/r/dreamtools/dreamtools?branch=master

.. image:: https://badge.waffle.io/dreamtools/dreamtools.png?label=ready&title=ready
   :target: https://waffle.io/dreamtools/dreamtools
   
.. image:: https://zenodo.org/badge/18543/dreamtools/dreamtools.svg
   :target: https://zenodo.org/badge/latestdoi/18543/dreamtools/dreamtools

:Note: DREAMTools is compatible for Python 2.7, 3.3, 3.4, 3.5
:Note about coverage: We do not run the entire test suite on Travis, which
                      reports a 40% test coverage. Note however, that the actual
                      test coverage is about 80%.
:Contributions: Please join https://github.com/dreamtools/dreamtools and share your notebooks https://github.com/dreamtools/dreamtools/notebooks

:Online documentation: `On pypi website <http://pythonhosted.org/dreamtools/>`_
:Issues and bug reports: `On github <https://github.com/dreamtools/dreamtools/issues>`_
:How to cite: Cokelaer T, Bansal M, Bare C et al. DREAMTools: a Python 
    package for scoring collaborative challenges [version 1; referees: 
    awaiting peer review] F1000Research 2015, 4:1030 
    (doi: 10.12688/f1000research.7118.1)
    `F1000 link <http://f1000research.com/articles/4-1030/v1>`_

.. won't appear on github but within the sphinx doc
.. image:: ../dreamtools_logo.png
    :width: 50%

.. contents::

Overview
----------------

Motivation
~~~~~~~~~~~~

**DREAMTools** aims at sharing code used in the scoring of `DREAM <http://dreamchallenges.org>`_ challenges that pose fundamental questions about system biology and translational medicine.

The main goals of **DREAMTools** are to provide:

#. scoring functions equivalent to those used during past DREAM challenges for **end-users** via a standalone application (called **dreamtools**).
#. a common place for **developers** involved in the DREAM challenges to share code

**DREAMTools** does not provide code related to aggregation,
leaderboards, or more complex analysis even though such code
may be provided (e.g., in D8C1 challenge). 

Note that many scoring functions requires data hosted on `Synapse <www.synapse.org>`_ . We therefore strongly encourage you to **register to Synapse**. Depending on the challenge, you may be requested to accept terms of agreements to use the data. 

Usage
~~~~~~~~~
**DREAMTools** can be used by developers as a Python package::

    >>> from dreamtools import D6C3
    >>> s = D6C3()
    >>> s.score(s.download_template())
    {'results': chi2            53.980741
    R-square        34.733565
    Spearman(Sp)     0.646917
    Pearson(Cp)      0.647516
    dtype: float64}

A standalone application can be used from a terminal. The executable is called **dreamtools**. Here is an example::

    dreamtools --challenge D6C3 --submission path_to_a_file

See below for more details about the usage of the standalone application.




Installation
---------------

Although there is a dedicated documentation related to the :ref:`installation`  of **DREAMTools** (in doc/source/installation.rst), we provide here below a brief summary.


Familiar with Python ecosystem ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are familiar with Python and the **pip** application and your system 
is already configured (compilers, development libraries available)), these 
two commands should install **DREAMTools** and its dependencies (in unix or
windows terminal)::

    pip install cython
    pip install dreamtools


If you are new to Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are not familiar with Python, or have issues with the previous method
(e.g., compilation failure), or do not have root access, we would recommend to
use the `Anaconda <https://www.continuum.io/downloads>`_ solution.

Anaconda is a free Python distribution. It includes most popular Python packages
for science and data analysis. Anaconda will install most of the software 
required by **DREAMTools**. Besides, since it does not require root access, it 
should not interfere with your system.

You will need to choose between 2 versions of Python (2.X or 3.5). Since **DREAMTools** is 
compatible with Python 2.7 and 3.5, the version should not matter. **Note, however, that 
for Windows' users, we would recommend to use Python 2.7** (see :ref:`installation` for explanations).


Here below are 4 steps checked on Unix and Windows platforms. 

**For Mac and Linux users:**

#. Download Anaconda
#. Open an Anaconda shell (or a unix shell)
#. Download `conda_install.sh <https://raw.githubusercontent.com/dreamtools/dreamtools/master/conda_install.sh>`_ 
#. Execute the script (e.g. for Python2)::

    sh conda_install.sh python=2


Similarly for **For Windows**:

#. Download Anaconda2 (Python2) for windows
#. Open an Anaconda prompt (from the Start->All program->Anaconda2->Anaconda
   Prompt
#. Download `conda_install.bat <https://raw.githubusercontent.com/dreamtools/dreamtools/master/conda_install.bat>`_ 
#. Execute the script::

    conda_install.bat

If there is an issue, please visit the :ref:`installation` page (doc/source/installation.rst) where details about the installation scripts can be found.


Installation from source
~~~~~~~~~~~~~~~~~~~~~~~~~

The command::

    pip install dreamtools
    
install the latest release of **DREAMTools**. If you prefer to use the source code, you can also get the github repository and install **DREAMTools** as 
follows (dependencies such as numpy or scipy will need to be compiled if 
not found)::


   git clone git@github.com:dreamtools/dreamtools.git
   cd dreamtools
   python setup.py install



The **dreamtools** executable
------------------------------------------

**DREAMTools** provides functions to obtain the template and gold 
standard(s) used in a given challenge. Some challenge have restrictions 
of data access and require the user to accept conditions of use. Such data 
are stored on http://www.synapse.org. You will need to create a 
login/password on www.synapse.org website. The first time you run a 
challenge within DREAMTools, files will be downloaded from Synapse. You 
may be asked to accept some conditions of use (e.g. D8C1 challenge) 
directly on the website. 

For users, **DREAMTools** package provides an executable called 
**dreamtools**, which should be installed automatically. 

To obtain some help, type::

    dreamtools --help

You should see a list of challenges: D2C1,D2C3, D2C3,... Those are aliases to 
DREAM challenges. Information about a challenge can be (in general) obtained
from the Synapse page of the challenge using the --onweb option::

    dreamtools --challenge D6C3 --onweb

Brief information can also be printed in the terminal as follows::

    dreamtools --challenge D6C3 --info

Next, you may want to score one of your submission. We provide access to
templates for each challenge. For instance::

    dreamtools --challenge D6C3 --download-template

This command prints the location of the template on your system. Copy that file
in local/temporary place. Now that you have a copy of the template, you can fill 
its contents with your own data and score it (let us assume it is called D6C3_template.txt)::

    dreamtools --challenge D6C3 --submission D6C3_template.txt

This command should print some information and the score of the submission 
for instance for the example above, we get the following results::

    {'results': chi2            53.980741
     R-square        34.733565
     Spearman(Sp)     0.646917
     Pearson(Cp)      0.647516
     dtype: float64}

All outputs will contain a json-like output. The synapse page of the challenge
should give information about the scoring methodology.

Note that some challenges (like the D8C1 challenge) have sub-challenges. For instance in D8C1, there are 4 sub-challenges names (e.g., SC1A). So, you would need to be more specific and to provide the name of a sub-challenge. For instance:: 

    dreamtools --challenge D8C1 --download-template --sub-challenge SC1A

.. note:: In D8C1, you will also need to accept the conditions of use 
    of the data on a Synapse page, which should pop up.

The sub-challenge names can be obtained using --info option (see here above). Similarly to the simpler case shown above, you can now score that submission as follows::  

    dreamtools --challenge D8C1 --sub-challenge SC1A \
        --submission D8C1_example.zip

Again, you should get an output with the results::

     Solution for alphabeta-Network.zip in challenge d8c1 (sub-challenge sc1a) is :
     meanAUROC: 0.803628919403


Available challenges
-------------------------

**DREAMTools** includes about 80% of DREAM challenges from DREAM2 to DREAM9.5
Please visit `F1000 link <http://f1000research.com/articles/4-1030/v1>`_  (Table 1).


Gold standards
-----------------

All gold standards are retrieved automatically. You can obtain the location of a gold standard file as
follows::

    dreamtools --challenge D6C3 --download-goldstandard

Issues
-----------

Please fill bug report in https://github.com/dreamtools/dreamtools/issues


Contributions
---------------

Please join https://github.com/dreamtools/dreamtools


For developers
----------------

Please see doc/source/developers.rst

Credits
-----------

Please see doc/source/credits.rst


More documentation ?
------------------------

Please see the doc directory, which is processed and posted on 
`pypi website <http://pythonhosted.org/dreamtools/>`_ with each release.

