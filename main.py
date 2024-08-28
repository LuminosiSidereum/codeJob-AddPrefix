import os
import sys
from pathlib import Path




if __name__=="__main__":
    modus:str = mode_selection()
    prefix:str = prefix_input()

    # Set storage directory of the python skript as current diretory
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)
    
    if modus == "0":
        prefix_add(prefix)
    if modus == "1":
        prefix_edit(prefix)
