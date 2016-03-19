.. _userguide:

User Guide
===========



Introduction
----------------
**DREAMTools** provides scoring functions that were used in past DREAM
challenges. In order to use those scoring functions, users may use an executable
called **dreamtools** (See :ref:`standalone` section) while developers may use the Python library directly in 
their own pipelines.

The main idea behind **DREAMTools** is to provide to researchers the scoring
functions that were used in past DREAM challenges. Usually, researchers would
already know the topic / purposes of a challenge but information can also be
retrieved with **DREAMTools** as shown here below. Then, one would
need to design a new methodology to solve the challenge. The difficulties then may be
to (i) retrieve a template, (ii) fill the template with a prediction and (iii) 
to score the prediction to evaluate the performance of the prediction.

**DREAMTools** will help researchers in retrieving information and templates
about a challenge, and apply the relevant scoring function to evaluate their
algoritm(s).

What is the data format, what is the challenge about ?
-------------------------------------------------------

Each data format is different and each challenge is complex and specific to a biological problem so we will not explain each challenge or template format in this documentation. However, links and information provided within **DREAMTools** should give enough help to start with.

There were tens of challenges (see http://f1000research.com/articles/4-1030/v1) 
during the last years and we will refer to a given
challenge by a nickname (e.g., D6C3 stands for challenge 3 in DREAM
version 6). Finally, note that some challenges have sub-challenges whose names 
must be provided.

For example, to retrieve information about the D9C1 challenge (Gene essentiality), Python users can type these commands::

    from dreamtools import D9C1
    challenge = D9C1(download=False)
    challenge.onweb()

Or, using the **dreamtools** standalone application, one can type in a shell the
following command::

    dreamtools --challenge D9C1 --info

This should open the Synapse web page of the challenge where description,
template, leaderboards are stored altogether.


Synapse login
-----------------

Before giving more details about **DREAMtools**, we would like to emphasize that the software
is closely linked to |Synapse|_ where challenges are described and where data 
required for the scoring may be stored.

.. note:: **Consequently, users will need to sign up to  Synapse website:**  http://www.synapse.org.


Once you have a Synapse login, you can also create a local authentication by creating
a file called **.synapseConfig** in your home directory and add this content::

    [authentication]
    username: email
    password: password

where the email and password are those you have created/obtained from |Synapse|_ . 
This will avoid you to have to enter the login/password each time **DREAMTools** tries to
connect to |Synapse|_.

Notes about data restrictions
----------------------------------

**DREAMTools** provides functions to obtain the template and gold
standard(s) used in a given challenge. Some challenge have restrictions
of data access and require the user to accept conditions of use. Such data
are stored on |Synapse|_ and the first time you run a challenge within **DREAMTools**, 
files may be downloaded and you may be asked to accept some conditions 
of use.


.. _standalone:

The **dreamtools** executable
--------------------------------

For users, **DREAMTools** package provides an executable called
**dreamtools**, which should be installed automatically. To check that it is
installed properly, type this command in a shell::

    dreamtools --help

this will give you some basic help about the usage. Let us seee how it works. First, let us choose a challenge. Challenge are named DXCY where X starts from number 2 to indicate the DREAM session. Y indicates the challenge itself.

::

    dreamtools --challenge D5C1


This will raise an error because there is no submission provided. A
template/example can be retrieved as follows::


    dreamtools --challenge D5C1 --download-template


This prints the path to a template, which can now be scored (even though the
template contains dummy data in general)::


    dreamtools --challenge D5C1 --filename <path2template>


similarly one can download the gold standard. This is a good way to check the
scoring function since scoring the gold standard with itself should
give a perfect score::

    dreamtools --challenge D5C1 --download-gold-standard
    dreamtools --challenge D5C1 --filename <path2gold>


If there are sub challenges like in D9C1 challenge, a sub-challenge name must be
provided. If one type::

    dreamtools --challenge D9C1 --download-template

an error message will tell you that the sub-challenge name is missing together
their names. Here, the names are shown to be sc1, sc2, sc3::

    dreamtools --challenge D9C1 --download-template --sub-challenge sc1



Scripting
-----------

An alternative to the standalone application is to use **DREAMTools** inside a
Python script. Similarly to what we have seen in the previous section, you 
can download templates, gold standards and scoring functions. All challenges 
are based upon a single :class:`~dreamtools.core.Challenge` class and use a very similar syntax::

    # import a challenge
    from dreamtools import D5C1
    # create the challenge structure
    c = D5C1()

    # figure out the path to a template
    filename = c.download_template()

    # score that template
    results = c.score(filename)

    # print the results
    print(results)

If you have sub challenges, they can be found in the attribute called *sub_challenges*::

    from dreamtools import D9C1
    c = D9C1()
    subname = c.sub_challenges[0]   # get only the first sub challenge name
    filename = c.download_template(subname)
    results = c.score(filename, subname)
    print(results)


Getting information about a challenge
--------------------------------------------

From the Python command line, for a given challenge, you can get a brief summary
and the Synapse page identifier::

    from dreamtools import D9C1
    s = D9C1(download=False)  # Needed if you do not have a Synapse account
    print(s)

You can also open the Synapse web page corresponding to that challenge::

    s.onweb()


Or use the **dreamtools** executable::

    dreamtools --challenge D9C1 --info
    dreamtools --challenge D9C1 --onweb


Where to get more help or examples ?
----------------------------------------

All dream challenges have their own Synapse page and should be used as the
official references. Especially if you want to contact the organisers of a
challenge. 

However, you may also get brief help and information from other sources:

#. From the DREAMTools paper on `F1000 <http://f1000research.com/articles/4-1030/v1>`_.
#. The :ref:`references` of DREAMTools itself
#. Notebooks provided in DREAMTools. There are only a few at the moment but 
   contributions are welcome and will be added.
#. `Notebooks <https://github.com/dreamtools/dreamtools/tree/master/notebooks>`_












.. |Synapse| replace:: Synapse
.. _Synapse: http://www.synapse.org

