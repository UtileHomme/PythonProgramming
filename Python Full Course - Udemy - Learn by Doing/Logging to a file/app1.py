import logging

logging.basicConfig(format ='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('books')

logger.info('This will not show up.')
logger.warning('This will.')
logger.debug('This is a debug message')
logger.critical('A  critical error occurred')

"""
DEBUG - they don't show up
INFO - they don't show up
WARNING - this shows up
ERROR - this shows up
CRITICAL - this shows up
"""

logger = logging.getLogger('books.database')
