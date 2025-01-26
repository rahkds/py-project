from flask import Flask
from . import api_logger,error_handler

def register_middleware(app: Flask):
    app.before_request(api_logger.set_request_basic_info)
    app.before_request(api_logger.log_incoming_request)
    app.after_request(api_logger.log_end_request)
    app.register_error_handler(Exception, error_handler.error_handler)