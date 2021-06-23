"""
watchtower-py

Library for building Python applications that integrate with Watchtower.cash
"""

__version__ = '0.1.3'
__author__ = 'Joemar Taganna'
__credits__ = 'Paytaca, Inc.'

from .subscription import subscribe
from .bch import BCH
from .slp import SLP
