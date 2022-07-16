import glob

python_files = glob.glob('*.py')

print("List of Python files from running glob.glob('*.py')")
print(python_files)

import sys
# Try running => python demo.py one two three
print(sys.argv)

# more sophisticated mechanism to handle command line arguments
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file'
)

parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
