import logging
def a(logger):
   logger.info('WORKING WORKINGGGG')

logging.basicConfig(filename='example2.log',level=logging.DEBUG,)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
a(logging.getLogger())