import logging
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import exception_handler, set_rollback




class MyCustomError(Exception):
    def __init__(self, message:str, status_code:int):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return self.message



def crm_exception_handler(exc, context):
    """
    DRF custom exception handler.  This will allow us to add useful information
    to any exceptions to help out our frontend devs
    """

    # Call REST framework's default exception handler first, to get the standard error response.
    response = exception_handler(exc, context)

    if not response and isinstance(exc, IntegrityError):
        # https://github.com/encode/django-rest-framework/issues/5760
        if 'duplicate key value violates unique constraint' in str(exc):
            set_rollback()
            msg = "Unique constraint violated: {exc}".format(exc=exc)
            response = Response({"detail": msg}, status=400)

    elif type(exc).__name__ == MyCustomError.__name__:
        logger = logging.getLogger(__name__)
        set_rollback()
        logger.exception(exc)
        response = Response({"detail": str(exc)}, status=int(exc.status_code))

    return response