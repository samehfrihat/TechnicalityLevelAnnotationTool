from flask import json
from src import app


def response(data, status, mime_type='application/json'):
    return app.response_class(
        response=json.dumps(data),
        status=status,
        mimetype=mime_type
    )


def return_fail(error: str):
    return {"status": False, "error": error}


def return_pass(value=None):
    return {"status": True, "value": value}
