# logger.py

import logging

logger = logging.getLogger('server')
logger.setLevel(logging.DEBUG) 

fh = logging.FileHandler('server.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh) 
logger.addHandler(ch)