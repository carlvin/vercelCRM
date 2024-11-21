
from pathlib import Path

def setup_logging(base_dir:Path) -> dict:
    """
    Sets up the logging configuration for the application.
    """

    # Ensure logs directory exists
    LOGS_DIR = base_dir / 'logs'
    LOGS_DIR.mkdir(exist_ok=True)
    """
    Defines the logging formatters used in the application.

    The `FORMATTERS` dictionary defines two logging formatters:

    1. `verbose`: A verbose formatter that includes detailed information about the log message, such as the log level, timestamp, module, filename, line number, function name, and process ID.
    2. `simple`: A simpler formatter that includes the log level, timestamp, module, filename, line number, function name, and the log message.

    These formatters can be used to configure the logging handlers in the application.
    """
    FORMATTERS = (
        {
            "verbose": {
                "format": "{levelname} {asctime:s} {name} {threadName} {thread:d} {module} {filename} {lineno:d} {name} {funcName} {process:d} {message}",
                "style": "{",
            },
            "simple": {
                "format": "{levelname} {asctime:s} {name} {module} {filename} {lineno:d} {funcName} {message}",
                "style": "{",
            },
        },
    )


    """
    Defines the logging handlers used in the application.

    The `HANDLERS` dictionary defines three logging handlers:

    1. `console_handler`: A console handler that logs messages to the console with a simple formatter.
    2. `info_handler`: A rotating file handler that logs messages with a verbose formatter to the `data_info.log` file. The file is rotated when it reaches 5 MB, and up to 5 backup files are kept.
    3. `error_handler`: A rotating file handler that logs messages with a verbose formatter to the `data_error.log` file. The file is rotated when it reaches 5 MB, and up to 5 backup files are kept.

    These handlers can be used to configure the logging loggers in the application.
    """
    HANDLERS = {
        "console_handler": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG"
        },
        "info_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{base_dir}/logs/data_info.log",
            "mode": "a",
            "encoding": "utf-8",
            "formatter": "verbose",
            "level": "INFO",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
        "error_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{base_dir}/logs/data_error.log",
            "mode": "a",
            "formatter": "verbose",
            "level": "WARNING",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
    }

    """
    Defines the logging loggers used in the application.

    The `LOGGERS` dictionary defines four logging loggers:

    1. `django`: Logs messages from the Django framework to the console and the `data_info.log` file at the `INFO` level.
    2. `django.request`: Logs messages related to requests at the `INFO` level, and propagates the messages to higher-level loggers.
    3. `django.template`: Logs messages related to templates at the `DEBUG` level, but does not propagate the messages to higher-level loggers.
    4. `django.server`: Logs messages related to the server at the `INFO` level, and propagates the messages to higher-level loggers.

    These loggers can be used to configure the logging in the application.
    """
    LOGGERS = (
        {
            "django": {
                "handlers": ["console_handler", "info_handler"],
                "level": "INFO",
            },
            "django.request": {
                "handlers": ["error_handler"],
                "level": "INFO",
                "propagate": True,
            },
            "django.template": {
                "handlers": ["error_handler"],
                "level": "DEBUG",
                "propagate": False,
            },
            "django.server": {
                "handlers": ["error_handler"],
                "level": "INFO",
                "propagate": True,
            },
        },
    )


    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": FORMATTERS[0],
        "handlers": HANDLERS,
        "loggers": LOGGERS[0],
    }