import logging
import sys

def logger_setup(file_logger: str = None,log_to_stdout: bool =False) -> logging.Logger:
    logger = logging.getLogger("client")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if file_logger:
        file_handler = logging.FileHandler(file_logger)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    if log_to_stdout:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)

    return logger

    