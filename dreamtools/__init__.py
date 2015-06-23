from .core.sageutils import Login
from .core import settings
import os
configuration = settings.DreamToolsConfig()
dreampath = configuration.user_config_dir


def create_dreamtools_config_directories(maindir, subdirectories):
    import os
    cfg = configuration.user_config_dir
    path = cfg + os.sep + maindir
    if os.path.isdir(path) is False:
        print("Creating directories in %s for %s" % (cfg, maindir) )
        os.mkdir(path)
    for directory in subdirectories:
        subdir = path + os.sep +directory
        if os.path.isdir(subdir) is False:
            print(" - creating %s" % subdir)
            os.mkdir(subdir)

from dreamtools.core.challenge import Challenge




from dream3.D3C1.scoring import D3C1

from dream4.D4C1.scoring import D4C1
from dream4.D4C3.scoring import D4C3

from dream5.D5C2.scoring import D5C2

from dream7.D7C1.scoring import D7C1

from dream8.D8C2.scoring import D8C2

from dream9dot5.D9dot5C1.scoring import D9dot5C1
