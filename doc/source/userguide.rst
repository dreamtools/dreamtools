User Guide
===========


For a user, there are 2 ways to use **DREAMTools**. Either using the executable
**dreamtools** or by scripting the library. 

Before explaining the two approches, let us simply explain the idea of the
scoring functions. It may sound obvious but to score a submission one need to have a submission ! Given the complexity and diversity of challenges, the templates are also complex and diverse. The format must be correct and the scoring functions in **DREAMTools** do not have thorough format validators so it would be handy to retrieve a template submission, which is possible as shown hereafter.

The scoring will internally download a gold standard file, which can also be
retrieved independently. 

Finally, note that some challenges have sub-challenges, which name must be provided. 


The **dreamtools** executable
--------------------------------

In a shell, type ::

    dreamtools --help

to obtain some basic help about the usage. 

First, let us choose a challenge. Challenge are named DXCY where X starts from
number 2 to indicate the DREAM session. Y indicates the challenge itself. 

::

    dreamtools --challenge D5C1


This will raise an error becaseu there is no submission provided. A
template/example can be easily retrieved::


    dreamtools --challenge D5C1 --download-template


This prints the path to a template, which can now be scored::


    dreamtools --challenge D5C1 --filename <path2template>


similarly one can download the gold standard. This is a good way to check the
scoring function by the way::
    
    dreamtools --challenge D5C1 --download-gold-standard
    dreamtools --challenge D5C1 --filename <path2gold>


If there are sub challenges like in D9C1 challenge, a sub-challenge name must be
provided. If one type::

    dreamtools --challenge D9C1 --download-template

an error message will tell you that the sub-challenge name is missing together
the their names. Here, the names are shown to be sc1, sc2, sc3.::

    dreamtools --challenge D9C1 --download-template -sub-challenge sc1



Scripting
-----------

All challenges have a single class inside the library. For instance the
challenge 3 in DREAM 5 class is named D5C3. 

The layout of those classes are identical throughout the challenges::

    from dreamtools import D5C1
    c = D5C1()
    filename = c.download_template()
    results = c.score(filename)
    print(results)

If you have sub challenges, they can be found in the attribute sub_challenges::

    from dreamtools import D9C1
    c = D9C1()
    subname = c.sub_challenges[0]
    filename = c.download_template(subname)
    results = c.score(filename, subname)
    print(results)


Getting information about the challenge
--------------------------------------------


From the Python command line, for a given challenge, you can get a brief summary
and more importantly the Synpase page::

    from dreamtools import D9C1
    s = D9C1()
    print(s)


You can also use the **dreamtools** executable::

    dreamtools --challenge D9C1 --info
