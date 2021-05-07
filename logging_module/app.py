import logging
from logging.handlers import SMTPHandler, SysLogHandler, RotatingFileHandler
import os

# mailsending using SMTPHandler

def mailsend():
    logger_obj1 = logging.getLogger(__name__)
    mail_handler = SMTPHandler(
        mailhost='127.0.0.1',
        fromaddr='server-error@example.com',
        toaddrs=['admin@example.com'],
        subject='Application Error'
    )

    mail_handler.setLevel(logging.ERROR)

    mail_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))

    logger_obj1.addHandler(mail_handler)


# locallog using StreamHandler and FileHandler
def localog():

    if not os.path.exists('logs3'):
        os.mkdir('logs3')  # create a directory called logs in the filepath if it doesnot exist

    # Create a custom logger_obj
    logger_obj2 = logging.getLogger(__name__)

    # Create handlers

    w_handler = logging.StreamHandler()
    e_handler = logging.FileHandler('logs3/file.log')   # 'logs2/micro.log'
    w_handler.setLevel(logging.WARNING)
    e_handler.setLevel(logging.ERROR)  # can be set to anything like DEBUG, INFO, WARNING, ERROR, CRITICAL

    # Create formatters and add it to handlers

    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    # f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    f_format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

    w_handler.setFormatter(c_format)

    e_handler.setFormatter(f_format)


    # Add handlers to the logger_obj

    logger_obj2.addHandler(w_handler)
    logger_obj2.addHandler(e_handler)
    logger_obj2.warning('This is a warning message')
    logger_obj2.error('This is an error message on Monday')  # message could be set to anything like DEBUG, INFO, WARNING, ERROR, CRITICAL


# locallog using RotatingFileHandler

def roatatlocallog():
    if not os.path.exists('logs2'):
        os.mkdir('logs2')  # create a directory called logs in the filepath if it doesnot exist
    logger_obj3 = logging.getLogger(__name__)
    file_handler = RotatingFileHandler('logs2/micro.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    #file_handler.setLevel(logging.ERROR)  # can be set to anything like DEBUG, INFO, WARNING, ERROR, CRITICAL
    file_handler.setLevel(logging.WARNING)
    logger_obj3.addHandler(file_handler)
    logger_obj3.warning('This is a warning message')

    #logger_obj.error('This is an error message')  # message could be set to anything


# syslog using SysLogHandler

def sysslog():
    # host and port from json
    logger_obj4 = logging.getLogger(__name__)
    logger_obj4.setLevel(logging.WARNING)
    sys_handler = SysLogHandler()   # address facility, facility
    sys_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    logger_obj4.addHandler(sys_handler)
    logger_obj4.warning('This is a warning message')


if __name__ == "__main__":
    # mailsend()
    localog()
    #roatatlocallog()
    #sysslog()
