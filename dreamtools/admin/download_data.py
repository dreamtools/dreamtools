from dreamtools import Challenge
import dreamtools


def get_challenge_list():
    """Returns list of challenge names"""
    registered = sorted([x for x in dir(dreamtools) if x.startswith('D')
        and 'C' in x])
    return registered


def _generic_download(name, mode):
    c = Challenge(name)
    class_inst = c.import_scoring_class()
    if mode == 'template':
        if len(class_inst.sub_challenges) == 0:
            class_inst.download_template()
        else:
            for subname in class_inst.sub_challenges:
                class_inst.download_template(subname)
    elif mode == 'gs':
        if len(class_inst.sub_challenges) == 0:
            class_inst.download_goldstandard()
        else:
            for subname in class_inst.sub_challenges:
                class_inst.download_goldstandard(subname)


def download_gs(name):
    _generic_download(name, 'gs')


def download_template(name):
    _generic_download(name, 'template')


def download_all():
    names = get_challenge_list()
    for name in names:
        print("Downloading template for %s" % name)
        try:
            download_gs(name)
        except NotImplementedError:
            pass
        except Exception as err:
            raise(err)

        print("Downloading GS for %s" % name)
        try:
            download_template(name)
        except NotImplementedError:
            pass
        except Exception as err:
            raise(err)


