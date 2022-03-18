"""
A Python package for the XDSOX instrument on the PADRE H-FORT mission.
"""
# Licensed under a 3-clause BSD style license - see LICENSE.rst

try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"

import os
import datetime

# from dateutil.relativedelta import relativedelta

_package_directory = os.path.dirname(os.path.abspath(__file__))
_data_directory = os.path.abspath(os.path.join(_package_directory, "data"))

launch_date = datetime.datetime(2025, 9, 1)
# phase_e_start = launch_date + relativedelta(months=1)
# phase_e_end = phase_e_start + relativedelta(years=1)
