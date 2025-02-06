"""
Utility modules for OneShot-Extended
"""
import os
import tempfile

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
