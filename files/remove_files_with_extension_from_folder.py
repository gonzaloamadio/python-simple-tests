import os
import sys
import argparse
import fnmatch

# FOLDER="/tmp/testdir"
# EXTENSION=".json"

def remove_files(FOLDER,EXTENSION):

    # create folder if it does not exists
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    # create files
    for x in range(3):
        filename = f"{x}{EXTENSION}"
        with open(os.path.join(FOLDER, filename), 'wb') as temp_file:
            pass

    # print files
    print("There should be 3 files")
    for file_name in os.listdir(FOLDER):
        print(file_name)

    if os.path.isdir(FOLDER):
        with os.scandir(FOLDER) as entries:
            for entry in entries:
                if entry.name.endswith(EXTENSION):
                    print("si")
                if fnmatch.fnmatch(entry.name, '*.json'):
                    print(f"File name to be removed {FOLDER}/{entry.name}")
                    os.remove(os.path.join(FOLDER,entry.name))
    else:
        print("ERR")
        return 1

    print("There should be 0 files")
    for file_name in os.listdir(FOLDER):
        print(file_name)

    return 0

def main():
    parser = argparse.ArgumentParser(description='Remove files from folder')
    parser.add_argument("--folder", required=True, help="path/to/folder")
    parser.add_argument("--extension", required=True, help="Extension of files that will be deleted")
    args = parser.parse_args()

    print("FILENAME")
    print(os.path.basename(__file__))
    print(__file__)

    f = args.folder
    e = args.extension
    remove_files(f,e)

if __name__ == '__main__':
    sys.exit(main())


