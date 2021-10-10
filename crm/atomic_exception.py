import logging
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import exception_handler, set_rollback


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
            response = Response({"error": True, "content": msg}, status=400)

    if response is None:
        set_rollback()
        logger.exception(exc)
        response = Response({"error": True, "content": str(exc)}, status=500)

    return response