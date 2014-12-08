from .core.sageutils import Login
from .core import settings
import os
configuration = settings.DreamToolsConfig()

try:
    os.mkdir(configuration.user_config_dir + os.sep + "data")
except:
    pass



def create_dreamtools_config_directories(maindir, subdirectories):
    import os
    cfg = configuration.user_config_dir
    path = cfg + os.sep + 'data' + os.sep + maindir
    if os.path.isdir(path) is False:
        os.mkdir(path)
        for directory in subdirectories:
            subdir = path + os.sep +directory
            if os.path.isdir(subdir):
                os.mkdir(path)


