For developers
===================

How to structure a new challenge:
-------------------------------------

If you wish to include a scoring function in **DREAMTools**, we provide an
executable called **dreamtools-layout** (from :mod:`dreamtools.core.layout` module). It creates a minimalist layout automatically to help you to start.
You first need to think about a challenge nickname. Let us assume a challenge
for DREAM8 session, which is the fourth one. Its nickname would be D8C4.

First, move in the github tree structure to the **dream8** directory::

    cd dreamtools
    cd dream8

if the directory **dream8** does not exist, create it and add an empty file
called **__init__.py**. Then, all you need to do is to go to *dreamtools/dream8* directory and type::

    dreamtools-layout --challenge-name D8C4

Some sub directories and files are created including the **scoring.py** with a basic class where to code or wrap your scoring function.


If data file or templates are too large, we strongly recommend to store them in a project on Synapse. We have created a synapse project called `dreamtools <https://www.synapse.org/#!Synapse:syn4483180>`_
where for example the D5C2 data files have been stored. Other files can all be
stored there. This may be duplicated with existing projects but would ease the
maintenance of the 30-40 DREAM challenges already available in **DREAMTools**.

Naming conventions
-------------------

There is no strict conventions but to help creating more uniformed code, try to
name the template after the challenge nicknname for instance **D3C1_template**.
Irrespective of the name, place it in the templates/ directory. Similarly for gold standards: start the filename with **D3C1_goldstandard** tag.

Again, if those files are too large, consider placing them in synapse and use
tools inside DREAMTools to retrieve them automatically (see below).


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
        def __init__(self, verbose=True, download=True, **kargs):
            """.. rubric:: constructor"""
            super(D7C4, self).__init__('D7C4', verbose, download, **kargs)
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
            self.getpath_template('filename_in_templates_directory')

        def download_goldstandard(self):
            # should return full path to a template file
            self.getpath_goldstandard('filename_in_goldstandard_directory')


Storing large files
---------------------

Templates and gold standards are either stored within the **DREAMTools**
package or, if there are too large, on the Synapse web site. In the latter
case, the files will be downloaded on request (only once). You should therefore
not change those files, which are located in the **DREAMTools** directory 
(e.g., /home/user/.config/dreamtools). The downloaded files are stored in
specific directories. For instance, files related to the D9C1 challenge are 
stored in /home/user/.config/dreamtools/dream9/D9C1.

So, as developers, you should also figure out if a file should be stored in
Synapse or not. Large files are currently stored in this synapse page
`dreamtools <https://www.synapse.org/#!Synapse:syn4483180>`_

If your class inherits from :class:`dreamtools.core.challenge.Challenge`,
you can then just type this kind of command to (1) download the file and get its
local location::

    filename = self._download_data('DREAM5_GoldStandard_probes.zip',
                'syn2898469')


In this example, the file *DREAM5_GoldStandard_probes.zip* is stored in this
directory: /home/user/.config/dreamtools/dream5/D5C2 for the example above.


License/header
----------------

Please add this :download:`header <header.txt>` at the top of your Python files:


.. include:: header.txt
    :literal:


