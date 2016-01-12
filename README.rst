DREAMTools
==========


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

.. image:: doc/dreamtools_logo.png
    :width: 50%

.. contents::

Overview
----------------

**DREAMTools** aims at sharing code used in the scoring of `DREAM <http://dreamchallenges.org>`_ challenges.

The main goals are to provide:

#. scoring functions for the DREAM challenges for **end-users** via the **dreamtools-scoring** (or just **dreamtools**) standalone application.
#. a place for **developers** involved in the DREAM challenges to share code

**DREAMTools** does not provide code related to aggregation,
leaderboards, or more complex analysis even though such code
can be provided (e.g. D8C1 challenge). Note that some functionalities
may be restricted with some access to synapse platform. Indeed,
some challenges will require to download public data sets from `Synapse
<www.synapse.org>`_ , **in which case you will need to register and accept the
terms of agreements**.

Installation
---------------

If you are new to Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are not familiar with Python, or have issues with the previous method
(e.g., compilation failure), or do not have root access, we would recommend to
use the `Anaconda <https://www.continuum.io/downloads>`_ solution.

Anaconda is a free Python distribution. It includes most popular Python packages
for science and data analysis. Anaconda will install the software required by
**DREAMTools**. Since it does not require root access, it should not interfere with your system. 

Please, visit the `Anaconda <https://www.continuum.io/downloads>`_ website 
and follow the instructions. You may need to
choose between 2 versions of Python (2.X or 3.5). Since **DREAMTools** is 
compatible with Python 2.7 and 3.5, the version should not matter.

Whether you use Anaconda or not, Python should provide an utility called **pip**
that should now be available within a Terminal. 

Before installing **DREAMTools**, please install **cython** as follows::

    pip install cython

You may also use::

    conda install cython

An finally, install **DREAMTools** itself::

    pip install dreamtools

Installation from source
~~~~~~~~~~~~~~~~~~~~~~~~~

The previous method (using **pip**) install the latest release of
**DREAMTools**. If you prefer to use the source code, you can also get the latest version as follows::

   git clone git@github.com:dreamtools/dreamtools.git
   cd dreamtools
   python setup.py install


Note for Python3.X
~~~~~~~~~~~~~~~~~~~~~~
**DREAMTools** is compatible with Python2 and Python3. However, 
**DREAMTools** depends on a package that is currently not available for Python3
(synapseclient). As a temporary solution, we forked this package and provide
a compatible version.  You will need to install it manually as follows::

    pip install git+https://git@github.com/cokelaer/synapsePythonClient.git@v1.4.0_py3_dreamtools#egg=synapsePythonClient

Then, as above, type::    

    pip install dreamtools




The **dreamtools** executable
------------------------------------------

:Note: Challenges available within DREAMTools provide a mechanism to obtain a template and the gold standard used in the scoring. However, some data have restrictions and require the user to accept conditions of use.  
:Note about Synapse: In the current version of DREAMTools, you will need to create a login/password on www.synapse.org , which will be used to download some data files. 
:Restrictions: The first time you run a challenge within DREAMTools, files will be downloaded from Synapse. You may be asked to accept some conditions of use (e.g. D8C1challenge). 

For users, **DREAMTools** package provides an executable called **dreamtools**, which should be installed automatically. 

To obtain some help, type::

    dreamtools --help

You should see a list of challenges: D2C1,D2C3, D2C3,... Those are aliases to 
DREAM challenges. Information about a challenge can be (in general) obtained from the Synapse page of the challenge using the --onweb option::

    dreamtools --challenge D6C3 --onweb

Brief information can also be printed in the terminal as follows::

    dreamtools --challenge D6C3 --info

Next, you may want to score one of your submission. We provide access to
templates for each challenge. For instance::

    dreamtools --challenge D6C3 --download-template

Now that you have a template, you can fill its contents with your own data and
score it (let us assume it is called example.zip)::

    dreamtools --challenge D6C3 --submission D6C3_template.txt

This command should print some information and the score of the submission for instance for the example above, we get the following results::

    {'results': chi2            53.980741
     R-square        34.733565
     Spearman(Sp)     0.646917
     Pearson(Cp)      0.647516
     dtype: float64}

All outputs will contain a json-like output. The synapse page of the challenge
should give information about the scoring methodology.

Note that some challenges (like the D8C1 challenge) have sub-challenges. For instance in D8C1, there are 4 sub-challenges names (e.g., SC1A). So, you would need to be more specific and to provide the name of a sub-challenge. For instance:: 

    dreamtools --challenge D8C1 --download-template --sub-challenge SC1A

.. seealso:: In D8C1, you will also need to accept the conditions of use 
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

