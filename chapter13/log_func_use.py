from chapter13 import log_func

log_func.func()


import logging

logging.basicConfig()
log_func.func()


logging.basicConfig(level=logging.ERROR)
log_func.func()

logging.getLogger('log_func').level=logging.DEBUG
log_func.func()