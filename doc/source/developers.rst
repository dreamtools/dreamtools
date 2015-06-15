For developers
===================



How to structure a challenge:
-------------------------------

Let us assume you want to add a DREAM9 challenge referred as the first challenge.
Its nickname is **D9C1**.


That challenge may have sub challenges. For instance in D7C1, we had 3
sub-challenges. Nicknames should be given as well. Those nicknames will be used
in the dreamtools-scoring standalone application. If there is only one sub-challenge, there is
no need to name it.

#. In the tree directory of **dreamtools**, we will host the D9C1 challenge in
   ./dreamtools/dream9/D9C1. 
#. there, create a file called __init__.,py , which can be empty.
#. Create a scoring.py module where code will be implemented.
#. You may store a template in ./templates directory if not too large
#. add a README.rst (see for instance D7C1/README.rst)
#. data required to score submissions could be store in ./data
#. any other resources in ./misc


If data file or templates are too large, we strongly recommend to store them in a project on synapse.
I have created a synapse project called `**dreamtools** <https://www.synapse.org/#!Synapse:syn4483180>`_
where for example the D5C2 data files have been stored.



