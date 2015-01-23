from biokit.rtools import RSession


__all__ = ['RTools']


class RTools(object):
    """A base class to handle the R session and its verbosity"""
    def __init__(self, verboseR):
        assert verboseR in [True, False]
        self._verboseR = verboseR
        self.session = RSession(verbose=self.verboseR)
       

    def _get_verboseR(self):
        return self._verboseR
    def _set_verboseR(self, value):
        assert value in [True, False]
        self._verboseR = value
        self.session.dump_stdout = value
    verboseR = property(_get_verboseR, _set_verboseR)

