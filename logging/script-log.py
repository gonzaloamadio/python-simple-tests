import logging
import logging.config
import sys

# REF: https://stackoverflow.com/questions/8269294/python-logging-only-log-from-script/48891485

# ----------------- FORMA 2 : Dict confic, mismo resultado

DEFAULT_LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
            'datefmt': '%Y-%m-%d - %H:%M:%S' },
    },
    'handlers': {
        'console':  {'class': 'logging.StreamHandler',
                     'formatter': "standard",
                     'level': 'DEBUG',
                     'stream': sys.stdout
                     },
        'file':     {'class': 'logging.FileHandler',
                     'formatter': "standard",
                     'level': 'DEBUG',
                     'filename': 'mylog.log'}
                     #'filename': 'mylog.log','mode': 'w'}
    },
    'loggers': {
        'db_listener':   {'level': 'INFO',
                     'handlers': ['console', 'file'],
                     'propagate': False },
    }
}

logging.config.dictConfig(DEFAULT_LOGGING)
log = logging.getLogger('db_listener')

# ------------------- FORMA 1: Todas funciones

log2 = logging.getLogger('db-listener2')
log2.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s: %(message)s",
                          datefmt="%Y-%m-%d - %H:%M:%S")
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
# fh = logging.FileHandler("mylog.log", "w")
fh = logging.FileHandler("mylog.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log2.addHandler(ch)
log2.addHandler(fh)


def foo():
    print("myprint")
    log2.info("log 2")
    log.info("log 1")


def main():
    foo()

if __name__ == "__main__":
    sys.exit(main())
