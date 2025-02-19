import sys
from src.logger import logging

def get_error_message(error,error_detail:sys):
    _,_,tb = error_detail.exc_info()
    filename = tb.tb_frame.f_code.co_filename
    error_message = f"{str(error)} is the error occured in {filename} file at line {tb.tb_lineno}"
    return error_message

class CustomException(Exception):
    logging.info("Custom Exception Class is being called")
    def __init__(self,code_error,error_detail:sys):
        super().__init__(code_error)
        self.code_error = get_error_message(code_error,error_detail)

    def __str__(self):
        return self.code_error

