import os
import sys
from pathlib import Path

def mode_selection() -> str:
    """
    Prompts the user to select a mode.
    Returns:
    str: The selected mode.
    """
    mode_selection: bool = True
    while mode_selection:
        mode: str = input("Modus auswählen: 0 für Präfix einfügen; 1 für Präfix ändern: ")
        if mode in ["0", "1"]:
            mode_selection = False
        else:
            print("Ungültige Eingabe!")
    return mode



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
