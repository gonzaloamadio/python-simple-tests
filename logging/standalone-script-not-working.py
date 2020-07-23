import os
import logging
import sys

logger = logging.getLogger(os.path.splitext(os.path.basename(sys.argv[0]))[0])


def set_logger(verbosity):
    """
    Set logger level based on verbosity option
    """
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(module)s| %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if verbosity == 0:
        logger.setLevel(logging.WARN)
    elif verbosity == 1:  # default
        logger.setLevel(logging.INFO)
    elif verbosity > 1:
        logger.setLevel(logging.DEBUG)

    # verbosity 3: also enable all logging statements that reach the root logger
    if verbosity > 2:
        logging.getLogger().setLevel(logging.DEBUG)

def set_logger2():
#    logging.basicConfig(filename="/standalone-script.log",
#                        format='%(asctime)-15s|%(levelname)s|%(module)s|%(message)s',
#                        level=logging.INFO)

    logger.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setFormatter(formatter)

def foo_donde_uso_logging_seteado_en_main():
    print("UN print antes del log")
    print(os.path.splitext(os.path.basename(sys.argv[0]))[0])
    print(__name__)
#    logger.info("-- gon log --")

def main():

#    parser = argparse.ArgumentParser(
#        description='Receive messages from an UDP socket'
#    )
#    parser.add_argument('host', type=str)
#    parser.add_argument('port', type=int)
#    parser.add_argument('--verbosity', '-v', type=int, default=1,
#        help="Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output")
#    args = parser.parse_args()
#    set_logger(args.verbosity)

    #set_logger2()

    logger.info('Adentro del main')

    foo_donde_uso_logging_seteado_en_main()

if __name__ == "__main__":
    sys.exit(main())
