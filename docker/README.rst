Docker example
===================

In principle, you should be able to install **DREAMTools** without problems
using **pip** tool. However, we provide here a docker image http://www.docker.io
that may be use to try **DREAMTools**

To build an image with docker, go into the docker directory and build the
image::


    cd docker
    sudo docker  build  -t="dreamtools_test" .

This will take about 10-15 minutes to finish depending on your connection.

In brief, the  command above download a fedora distribution and installs
all dependencies (e.g., numpy) and dreamtools 0.10.5.

Then, start the docker::    

    sudo docker run -i -t -entrypoint='/bin/bash' dreamtools_test -i

This will start a docker and provides a Linux shell. There, type::

    ipython

Inside the IPython shell, you can try **DREAMTools** directly::

    import dreamtools
    from dreamtools import *
    s = D5C2()
    s.Ntf = 2 # to speed up the test
    s.score(s.download_template))


We also provide a Docker for ubuntu (See Dockerfile_ubuntu and dreamtools_install_ubuntu.sh).

