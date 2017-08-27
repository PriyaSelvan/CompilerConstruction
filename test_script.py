import subprocess
import sys
proc = subprocess.Popen(["python","interpreter.py","input_file", "-c", "import writer; writer.write()"], stdout=subprocess.PIPE)
out = proc.communicate()[0]
a=out.upper().split()
if ( not (a[0]==5 and a[1]==1)):
    sys.exit()
