"""This is the main module"""

import os.path
import data_gather

def main():
    """Entry point of repl"""
    has_file = os.path.isfile("./room_info")
    if not has_file:
        print("File room_info is missing, generating...")
        data_gather.get_all_room_time()
    print("room_info file found")
    return

if __name__ == "__main__":
    main()
