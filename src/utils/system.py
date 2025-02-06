"""
System utilities for OneShot-Extended
"""
import os
import platform

def isAndroid() -> bool:
    """Check if running on Android system.
    
    Returns:
        bool: True if running on Android, False otherwise
    """
    # Check common Android indicators
    android_indicators = [
        os.path.exists('/system/app'),  # Android system directory
        os.path.exists('/data/data/com.termux'),  # Termux
        'ANDROID_ROOT' in os.environ,  # Android environment variable
        'ANDROID_DATA' in os.environ,  # Android environment variable
        platform.system().lower() == 'android'  # Direct platform check
    ]
    
    return any(android_indicators)

def getAndroidArch() -> str:
    """Get Android device architecture.
    
    Returns:
        str: Architecture string ('arm64', 'arm', 'x86_64', 'x86' or '')
    """
    if not isAndroid():
        return ''
        
    arch = platform.machine().lower()
    
    if arch in ['aarch64', 'arm64']:
        return 'arm64'
    elif arch.startswith('arm'):
        return 'arm'
    elif arch in ['x86_64', 'amd64']:
        return 'x86_64'
    elif arch in ['i686', 'x86']:
        return 'x86'
    
    return ''

def checkRoot() -> bool:
    """Check if running with root privileges.
    
    Returns:
        bool: True if root, False otherwise
    """
    if isAndroid():
        # On Android, check if running in su context
        try:
            return os.getuid() == 0 or os.access('/system', os.W_OK)
        except:
            return False
    else:
        # On other systems, just check uid
        return os.getuid() == 0

def checkDependencies() -> bool:
    """Check if required system tools are available.
    
    Returns:
        bool: True if all dependencies are met, False otherwise
    """
    required_tools = [
        'iwconfig',
        'ifconfig',
        'ip',
        'wpa_supplicant',
        'wpa_cli'
    ]
    
    # On Android, check Termux packages
    if isAndroid():
        required_tools.extend([
            'su',
            'tsu'
        ])
    
    for tool in required_tools:
        if not any(os.path.exists(os.path.join(path, tool))
                  for path in os.environ.get('PATH', '').split(os.pathsep)):
            return False
    
    return True
