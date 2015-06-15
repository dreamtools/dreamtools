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

from dream7.D7C1.scoring import D7C1
from dream5.D5C2.scoring import D5C2
from dream8.D8C2.sc1 import D8C2_sc1
from dream8.D8C2.sc2 import D8C2_sc2