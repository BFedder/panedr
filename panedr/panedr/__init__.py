# -*- coding: utf-8 -*-

import pbr.version
__version__ = pbr.version.VersionInfo('panedr').release_string()
del pbr

from panedr import edr_to_dict, edr_to_df, read_edr
