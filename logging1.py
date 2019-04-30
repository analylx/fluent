import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s filename=%(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='a, %d %b %Y %H:%M:%S',
                    filename='d:/tmp/test.log',
                    filemode='w',
                    )
logging.debug('debug message1')
logging.info('info message2')
logging.warning('warning message3')
logging.error('error message4')
logging.critical('critical message5')