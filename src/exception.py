import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    This function returns a detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logging.error(self.error_message)
    
    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     logging.info("Logger is configured and ready to use.")
#     try:
#         x = 1 / 0
#     except ZeroDivisionError as e:
#         logging.error("An error occurred: %s", e)
