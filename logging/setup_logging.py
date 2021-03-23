import logging
import datetime
import os
import sys


LOGS_DIRECTORY = "logs"
logger = logging.getLogger(__name__)

def setup_logging():
    """LOGS_DIRECTORY should exists, or add a check and create it if not"""
    formatter = logging.Formatter('%(name)s:%(levelname)s:%(asctime)s:%(message)s', '%Y-%m-%d %H:%M:%S')

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    now_date = datetime.datetime.now()
    timestamp = format(now_date, '%Y%m%d%H%M%S')
    log_filepath = os.path.join(LOGS_DIRECTORY, timestamp + '.log')
    fh = logging.FileHandler(log_filepath, 'w')
    fh.setFormatter(formatter)
    root_logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    root_logger.addHandler(sh)


def foo():
    logger.info(f"Info: test2")


def main():
    setup_logging()
    logger.debug(f"Exception: test")
    logger.info(f"Info: test")
    foo()


if __name__ == '__main__':
    main()
