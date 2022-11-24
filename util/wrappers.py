from logging import exception


def try_except(func):
    def handler(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            exception(e)

    return handler
