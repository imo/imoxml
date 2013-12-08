"""Interface to the Expat non-validating XML parser."""
__version__ = '$Revision: 17640 $'

import sys

from _imoexpat import *

# provide pyexpat submodules as xml.parsers.expat submodules
sys.modules['xml.parsers.expat.model'] = model
sys.modules['xml.parsers.expat.errors'] = errors
