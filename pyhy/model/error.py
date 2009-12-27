from pyhy.error import HyvesError

class HyvesNotLoadedError(StopIteration, HyvesError):
    pass
