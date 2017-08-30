import json
from functools import wraps


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