import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

dependencies = []
with open ("requirements.txt", "r") as modules_depedencies:
    for modules in modules_depedencies:
        dependencies.append(modules.rstrip())
try:
    pkg_resources.require(dependencies)
except DistributionNotFound:
    print("Missing libreries, if you use pip, try running in this location:\n\n\tpython -m pip install -r requirements.txt")
    exit()