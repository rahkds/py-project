from app.config.logger import logger
from app.utils.api_response import APIResponse

def error_handler(error):
    logger.error(f"Unhandled error {error}")
    return APIResponse.server_error(error)