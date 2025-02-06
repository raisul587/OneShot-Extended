"""
Network interface control utilities
"""
import os
import subprocess
import time
import re

def ifaceCtl(iface: str, action: str = 'up') -> bool:
    """Control network interface state.
    
    Args:
        iface: Interface name (e.g., wlan0)
        action: Action to perform ('up' or 'down')
        
    Returns:
        bool: True if operation successful, False otherwise
    """
    if action not in ['up', 'down']:
        return False
        
    try:
        # Check if interface exists
        if not os.path.exists(f'/sys/class/net/{iface}'):
            return False
            
        # Try ip command first (modern systems)
        subprocess.run(['ip', 'link', 'set', iface, action], check=True)
        
        if action == 'up':
            # Wait for interface to be ready
            time.sleep(1)
            # Verify interface is up
            with open(f'/sys/class/net/{iface}/operstate', 'r') as f:
                state = f.read().strip()
                return state in ['up', 'unknown']
        return True
        
    except (subprocess.CalledProcessError, OSError):
        try:
            # Fallback to ifconfig (older systems)
            subprocess.run(['ifconfig', iface, action], check=True)
            time.sleep(1)
            return True
        except (subprocess.CalledProcessError, OSError):
            return False

def getInterface(prompt: bool = True) -> str:
    """Get wireless interface name.
    
    Args:
        prompt: Whether to prompt user to select interface if multiple found
        
    Returns:
        str: Interface name or empty string if none found
    """
    wireless_interfaces = []
    
    try:
        # Try using iwconfig to list wireless interfaces
        output = subprocess.check_output(['iwconfig'], stderr=subprocess.STDOUT, text=True)
        interfaces = re.findall(r'(\w+)\s+IEEE', output)
        wireless_interfaces.extend(interfaces)
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            # Fallback: check /sys/class/net for wireless devices
            for iface in os.listdir('/sys/class/net'):
                if os.path.exists(f'/sys/class/net/{iface}/wireless'):
                    wireless_interfaces.append(iface)
        except OSError:
            return ''
    
    if not wireless_interfaces:
        return ''
        
    if len(wireless_interfaces) == 1:
        return wireless_interfaces[0]
        
    if prompt:
        print("\nAvailable wireless interfaces:")
        for i, iface in enumerate(wireless_interfaces, 1):
            print(f"{i}. {iface}")
        try:
            choice = int(input("\nSelect interface number: "))
            if 1 <= choice <= len(wireless_interfaces):
                return wireless_interfaces[choice - 1]
        except ValueError:
            pass
    
    return wireless_interfaces[0]  # Return first interface if no selection made

def checkInterface(iface: str) -> bool:
    """Check if wireless interface exists and is up.
    
    Args:
        iface: Interface name to check
        
    Returns:
        bool: True if interface exists and is up
    """
    try:
        # Check if interface exists
        if not os.path.exists(f'/sys/class/net/{iface}'):
            return False
            
        # Check if it's a wireless interface
        if not os.path.exists(f'/sys/class/net/{iface}/wireless'):
            return False
            
        # Check interface state
        with open(f'/sys/class/net/{iface}/operstate', 'r') as f:
            state = f.read().strip()
            return state in ['up', 'unknown']
            
    except OSError:
        return False
