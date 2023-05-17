from rest_framework.views import exception_handler


def custom_exception_handler(exception, exception_context):
    response = exception_handler(exception, exception_context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['name'] = response.data.get("name")

    return response
