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

Naming conventions
-------------------

Put a template that filename starts with  **D3C1_template** in the templates/ directory
Similarly for goldstandard, start the filename with D3C1_goldstandard tag.




Basic Structure of the Challenge class
--------------------------------------------
::

    import os
    from dreamtools.core.challenge import Challenge

    class D7C4(Challenge):
        """A class dedicated to D7C4 challenge

        ::

            from dreamtools import D7C4
            s = D7C4()
            filename = s.download_template() 
            s.score(filename) 

        Data and templates are downloaded from Synapse. You must have a login.

        """
        def __init__(self):
            """.. rubric:: constructor"""
            super(D7C4, self).__init__('D7C4')
            self._path2data = os.path.split(os.path.abspath(__file__))[0]
            self._init()
            # if several sub-challenges, name them here
            self.sub_challenges = []

        def _init(self):
            # should download files from synapse if required.
            pass

        def score(self, prediction_file):
            raise NotImplementedError

        def download_template(self):
            # should return full path to a template file
            pass
            
        def download_goldstandard(self):
            # should return full path to a template file
            pass






