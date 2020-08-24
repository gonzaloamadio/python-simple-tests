
import sys


print(sys.version_info)

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")
