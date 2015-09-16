FAQS
=====



I cannot find the gold standard or template in the source code ?
--------------------------------------------------------------------

To keep the DREAMTools package light-weight, we have moved most of the data files 
on Synapse website. However, data (templates and gold standard) are downloaded 
on request and stored locally in a common directory. For instance under Linux, 
the files are stored in /home/user/.config/dreamtools/

Once the DREAMTools package is installed, you can retrieve the location of 
a template of gold standard using the following methods (e.g., for D5C1 challenge)::

  from dreamtools import D5C1
  s = D5C1()
  s.download_template()
  s.download_goldstandard()
  
  
