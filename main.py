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

def prefix_input() -> str:
    """
    Prompts the user to enter a prefix.
    Returns:
    str: The entered prefix.
    """
    prefix: str = input("Präfix eingeben: ")
    return prefix

def prefix_add(prefix: str) -> None:
    """
    Adds a prefix to all files except python skripts in the current directory.
    Args:
    prefix (str): The prefix to add.
    """
    for os_file in os.listdir():
        file = Path(os_file)
        if os.path.isfile(file) and file.suffix != ".py":
            file_name, file_extension = file.stem, file.suffix
            new_file_name = f"{prefix}-{file_name}{file_extension}"
            file.rename(new_file_name)
            print(f"Umbenennen von {file} zu {new_file_name}")

def prefix_edit(prefix: str) -> None:
    """
    Edits the prefix of all files except python skripts in the current directory.
    Args:
    prefix (str): The new prefix.
    """
    for os_file in os.listdir():
        file = Path(os_file)
        if os.path.isfile(file) and file.suffix != ".py":
            file_name, file_extension = file.stem, file.suffix
            nameblocks:list[str] = file_name.split("-")
            nameblocks[0] = prefix
            new_file_name:str = "-".join(nameblocks)+file_extension
            file.rename(new_file_name)
            print(f"Umbenennen von {file} zu {new_file_name}")
            
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
    
    input("Drücken Sie Enter zum Beenden...")
