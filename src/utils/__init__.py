"""
Utility modules for OneShot-Extended
"""
import os
import sys
import tempfile

# Import interface control functions
from .interface import ifaceCtl, getInterface, checkInterface

# Import system utilities
from .system import isAndroid, getAndroidArch, checkRoot, checkDependencies

def die(msg: str):
    """Print error message and exit program.
    
    Args:
        msg: Error message to display
    """
    print(f'\n[!] {msg}')
    sys.exit(1)

# Base directories
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC_DIR = os.path.join(ROOT_DIR, 'src')

# Data directories
DATA_DIR = os.path.join(ROOT_DIR, 'data')
REPORTS_DIR = os.path.join(DATA_DIR, 'reports')
SESSIONS_DIR = os.path.join(DATA_DIR, 'sessions')
PIXIEWPS_DIR = os.path.join(DATA_DIR, 'pixiewps')
HANDSHAKES_DIR = os.path.join(DATA_DIR, 'handshakes')

# Ensure directories exist
for directory in [DATA_DIR, REPORTS_DIR, SESSIONS_DIR, PIXIEWPS_DIR, HANDSHAKES_DIR]:
    os.makedirs(directory, exist_ok=True)

# Temporary directory
TEMP_DIR = tempfile.gettempdir()

# Debug mode
DEBUG = False  # Can be set via command line arguments

# Export all utility functions
__all__ = [
    # Interface functions
    'ifaceCtl', 'getInterface', 'checkInterface',
    # System functions
    'isAndroid', 'getAndroidArch', 'checkRoot', 'checkDependencies',
    # Error handling
    'die',
    # Directory constants
    'REPORTS_DIR', 'SESSIONS_DIR', 'PIXIEWPS_DIR', 'HANDSHAKES_DIR',
    'DATA_DIR', 'TEMP_DIR',
    # Debug flag
    'DEBUG'
]
