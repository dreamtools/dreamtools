FAQS
=====


Installation:: compilation issues
------------------------------------------------------------

DREAMTools depends on packages (e.g., numpy, cython) that requires a C compilator. When using the **pip** commands dependencies will be compiled. This takes time but more importantly may fail (e.g., missing library). In this situation, we would recommend you to use Anaconda solution. This will also speed up the installation. Visit Anaconda.org and install the software. Once done, open a terminal and type::

  pip install cython
  pip install dreamtools

What are the challenges available in DREAMTools ?
----------------------------------------------------

You can either check this reference http://f1000research.com/articles/4-1030/v1 (Table1), or type::

  dreamtools --help

I cannot find the gold standard or template in the source code, why  ?
------------------------------------------------------------------------

To keep DREAMTools package light-weight, we have moved some of the data files 
on Synapse website. However, data (templates and gold standard) are downloaded 
on request and stored locally in a common directory. For instance under Linux, 
the files are stored in /home/user/.config/dreamtools/

Once the DREAMTools package is installed, you can retrieve the location of 
a template of gold standard using the following methods (e.g., for D5C1 challenge)::

  from dreamtools import D5C1
  s = D5C1()
  s.download_template()
  s.download_goldstandard()
  
  
Is DREAMTools available for Python 3 ?
---------------------------------------------
Yes, it is Python3 compatible. Note, however, that some dependencies (e.g., gevent, synapseclient) were not Python3 compatible when we started the DREAMTools project. The gevent version available on the Python repository (pip command) should now be compatible. The synapseclient will be soon. Meanwhile, you should install this version::

    pip install git+https://git@github.com/cokelaer/synapsePythonClient.git@v1.4.0_py3_dreamtools#egg=synapsePythonClient


Do I need a Synapse account ?
--------------------------------
It depends on the challenge you are interested in. In general, files will be downloaded from synapse so you may need to have an account. Besides, you may be requested to accept conditions of use of some data sets. 






