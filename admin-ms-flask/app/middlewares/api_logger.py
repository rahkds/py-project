from flask import request, Response
import time
import uuid
from app.config.logger import logger

def set_request_basic_info():
    request.start_time = time.time()
    request.request_id = str(uuid.uuid4())

def log_incoming_request():
    logger.info(f"Request Id. {request.request_id} START - {request.method} -  {request.path}")

def log_end_request(response: Response):
    duration = time.time() - request.start_time
    logger.info(f"Request Id. {request.request_id} END - {request.method} -  {request.path} - {response.status_code} - {duration:.4f} seconds")
    return response


