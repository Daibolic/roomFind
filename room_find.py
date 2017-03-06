"""This is the main module"""

from pathlib2 import Path
import data_gather

def main():
    """Entry point of repl"""
    room_info = Path("./room_info")
    if not room_info.is_file():
        print("File room_info is missing, generating...")
        data_gather.get_all_room_time()
    return


if __name__ == "__name__":
    main()
