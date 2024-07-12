from enum import Enum


from . import v4
from . import blur
from . import meku



class THEME(Enum):
    BLUR = blur
    V4 = v4
    MEKU = meku
