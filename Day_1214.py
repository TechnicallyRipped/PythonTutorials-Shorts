

import sys

debug = '--debug' in sys.argv

print('Start')

if debug:
    print('~ Debug mode ~')

print('End')