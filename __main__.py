#! usr/bin/env python3
"""This is the main module"""

import os.path
import data_gather

def main():
    """Entry point of repl"""
    has_file = os.path.isfile("./room_info")
    if not has_file:
        print("File room_info is missing, generating...")
        data_gather.get_all_room_time()
        print("Info gathered. Stored in file room_info.")
    else:
        print("room_info file found")

    has_code = os.path.isfile("./bld_code")
    if not has_code:
        print("File bld_info is missing, generating...")
        data_gather.generate_building_codes()
        print("Building codes gathered. Stored in file bld_code.")
    else:
        print("Building codes file found")
    return

if __name__ == "__main__":
    main()
