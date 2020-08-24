import argparse
import glob
import logging
import os
import sys

from structlog import get_logger

logging.basicConfig(
    format="%(message)s",
    stream=sys.stdout,
    level=logging.INFO,
)

logger = get_logger()


def remove_files(folder, extension):

    logger.info(f'About to delete files with extension {extension} from folder {folder}')

    # Get a list of all the file paths that ends with .txt from in specified directory
    file_list = glob.glob(f'{folder}/*{extension}')
    for file_path in file_list:
        try:
            os.remove(file_path)
        except Exception as e:
            logger.exception(f'There was an error triggering {os.path.basename(__file__)}. Reason: {e}')
            return 1

    logger.info(f'Finish deleting files with extension {extension} from folder {folder}')
    return 0


def main():
    parser = argparse.ArgumentParser(description='Remove files from folder')
    parser.add_argument("--folder", required=True, help="path/to/folder containing files to be deleted")
    parser.add_argument("--extension", required=True, help="Extension of files that will be deleted")
    args = parser.parse_args()

    remove_files(args.folder, args.extension)


if __name__ == '__main__':
    sys.exit(main())
