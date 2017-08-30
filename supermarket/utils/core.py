from functools import wraps
from flask import Response, json


def catch_exception():
    def decorator(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return json.dumps('Unexpected error!')

        return decorated_func
    return decorator


def return_json(data):
    return Response(json.dumps(data), status=200, mimetype='application/json')