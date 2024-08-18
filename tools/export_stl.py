import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))

FREECAD_BINARY = "freecad"
EXPORT_SINGLE_FILENAME = os.path.join(HERE, "./export_stl_internal.py")

in_file_path = sys.argv[1]
out_file_path = sys.argv[2]

command = [
    FREECAD_BINARY, 
    "-c", 
    EXPORT_SINGLE_FILENAME, 
    "--",
    in_file_path, 
    out_file_path 
]
print(' '.join(command))
try:
    subprocess.run(command, check=True)
except:
    exit(1)
    
