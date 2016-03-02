############################################################################
DREAMTools
############################################################################

.. image:: https://badge.fury.io/py/dreamtools.svg
    :target: https://pypi.python.org/pypi/dreamtools

.. image:: https://secure.travis-ci.org/dreamtools/dreamtools.png
    :target: http://travis-ci.org/dreamtools/dreamtools

.. image:: https://coveralls.io/repos/dreamtools/dreamtools/badge.png?branch=master
   :target: https://coveralls.io/r/dreamtools/dreamtools?branch=master

.. image:: https://zenodo.org/badge/18543/dreamtools/dreamtools.svg
   :target: https://zenodo.org/badge/latestdoi/18543/dreamtools/dreamtools

.. image:: http://readthedocs.org/projects/dreamtools/badge/?version=latest
   :target: http://dreamtools.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status

:Python version: DREAMTools is supported for Python 2.7, 3.4 and 3.5
:Note about coverage: We do not run the entire test suite on Travis, which
                      reports a 40% test coverage. Note however, that the actual
                      test coverage is about 80%.
:Contributions: Please join https://github.com/dreamtools/dreamtools and share your notebooks https://github.com/dreamtools/dreamtools/notebooks

:Online documentation: `On readthedocs <http://dreamtools.readthedocs.org/>`_
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

See `online documentation on <dreamtools.rtd.org for details>`_ for more details
and examples. The source code also provides a set of IPython/Jupyter notebooks.


Installation
---------------

There is a dedicated page on  `online documentation on RTD <http://dreamtools.readthedocs.org/en/latest/#installation>`_ but here is a quick installation guide.


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

This command should install **DREAMTools** in your default conda environment. If you wish
to try **DREAMTools** in another environment (e.g different python version), you
would need to create a new one and then install **DREAMTools** in that
environment::

    conda create --name test_dreamtools --python 3.5
    source activate test_dreamtools
    conda install dreamtools


If there is an issue or wish to install from source, please visit the `online documentation on RTD <http://dreamtools.readthedocs.org/en/latest/#installation>`_ for details.



Available challenges, templates and gold standards
--------------------------------------------------------

**DREAMTools** includes about 80% of DREAM challenges from DREAM2 to DREAM9.5
Please visit `F1000 link <http://f1000research.com/articles/4-1030/v1>`_  (Table 1).

All gold standards and templates are retrieved automatically. Once downloaded, you will get
the location of the file. For instance::

    dreamtools --challenge D6C3 --download-goldstandard
    dreamtools --challenge D6C3 --download-template


See `online documentation on RTD <http://dreamtools.readthedocs.org/>`_ for details.

