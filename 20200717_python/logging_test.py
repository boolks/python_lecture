import logging


def say_hello(msg):
    return 'Hello ' + msg


# logger 생성
root_logger = logging.getLogger()
# log_level 설정
root_logger.setLevel(logging.DEBUG)
# logger file Handler 생성
fileHandler = logging.FileHandler('test.log', 'w', 'utf-8')
# logger console Handler 생성
streamHandler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(filename)s: %(lineno)s - %(message)s')

# File Handler 에 file_formatter 설정
fileHandler.setFormatter(file_formatter)
streamHandler.setFormatter(formatter)

# logger 객체에 file handler 와 stream handler 를 등록
root_logger.addHandler(fileHandler)
root_logger.addHandler(streamHandler)

root_logger.debug('Start of Program')
root_logger.debug(say_hello('debug 모드'))
root_logger.info(say_hello('info 모드'))
# root_logger.warn(say_hello('warn 모드'))
root_logger.error(say_hello('error 모드'))
root_logger.fatal(say_hello('fatal 모드'))
root_logger.debug('End of Program')
