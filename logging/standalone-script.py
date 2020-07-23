import os
import logging
import sys
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(os.path.splitext(os.path.basename(sys.argv[0]))[0])

"""
Level	Numeric value
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
"""

def set_logger2():

    logger.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter(fmt="%(asctime)s - %(name)s %(levelname)s: %(message)s",
                          datefmt="%Y-%m-%d - %H:%M:%S")
#    fh = logging.FileHandler("mylog.log")
    fh = RotatingFileHandler("mylog.log", backupCount=2)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
#    logger.propagate = False

def foo_donde_uso_logging_seteado_en_main():
    logger.info("-- gon log info --")
    logger.debug("-- gon log debug --")

def main():

    set_logger2()

    logger.info('Adentro del main')

    foo_donde_uso_logging_seteado_en_main()

if __name__ == "__main__":
    sys.exit(main())
