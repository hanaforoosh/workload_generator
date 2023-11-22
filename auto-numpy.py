import importlib
import subprocess
import sys

def import_package(package_name):
    try:
        package = importlib.import_module(package_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        package = importlib.import_module(package_name)

def main():
    import_package('numpy')
    return 'success'