For developers
===================



How to structure a challenge:
-------------------------------

Please use the module called **layout.py** in ./dreamtools/core/ directory or the **dreamtools-layout** executable provided with **dreamtools**. Use::

    dreamtools-layout --help

Go in dreamtools/dreamtools directory and use the **dreamtools-layout** tool as follows::

    dreamtools-layout --challenge-name D10C4
    
sub directories and files are created including the **scoring.py** with a basic class were to code the
scoring function.


If data file or templates are too large, we strongly recommend to store them in a project on synapse.
I have created a synapse project called `**dreamtools** <https://www.synapse.org/#!Synapse:syn4483180>`_
where for example the D5C2 data files have been stored.



