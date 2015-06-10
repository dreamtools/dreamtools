For developers
===================



How to structure a challenge:
-------------------------------

Let us assume DREAM9 challenge refered as the first challenge. Its nickname is
D9C1.


That challenge may have sub challenges. For instance in D7C1, we had 3
sub-challenges. Nicknames should be given as well. Those nicknames will be used
in the dreamtools-scoring standalone application.

#. In the tree directory of **drematools**, we host a challenge in
   ./dreamtools/dream9/D9C1. 
#. there, create a file called __init__.,py , which can be empty.
#. Create a scoring.py module where code will be implemented.
#. Store the templats in ./templates directory
#. Store the templats in ./templates directory
#. add a README.rst (see for isntance D7C1/README.rst)
#. data required to score submissions could be store in ./data
#. tools and resources to generate the test data in ./generator
#. any other resources in ./misc   

