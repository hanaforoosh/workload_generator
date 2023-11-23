from utils import get_powerset

function_file_content = """
import importlib
import subprocess
import sys
import time

def import_package(package_name):
    try:
        package = importlib.import_module(package_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        package = importlib.import_module(package_name)

def fixed_part():
    time.sleep(5)

def main():
    start_time = time.time()
    packages = {packages}
    for package in packages:
        import_package(package)
    fixed_part()
    end_time = time.time()
    execution_time = end_time - start_time
    return str(execution_time)
"""
function_file_prefix = "Functions/python-"
function_file_postifx = ".py"


def generate_functions(packages: list):
    formatted = function_file_content.format(packages=packages)
    with open(
        function_file_prefix + "-".join(packages) + function_file_postifx, "w"
    ) as f:
        print(formatted, file=f)


if __name__ == "__main__":
#   packages = [
#       "requests",
#       "numpy",
#       "pandas",
#       "matplotlib",
#       "flask",
#       "scikit-learn",
#       "tensorflow",
#       "keras",
#       "pytest",
#       "django",
#   ]
    packages = [
            "numpy",
            "flask",
            "pytest",
            "fastapi",
    ]
    pset = get_powerset(packages)
    for p in pset:
        generate_functions(list(p))
