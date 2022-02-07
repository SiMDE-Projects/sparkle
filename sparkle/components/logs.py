import logging.config
import os

from django.utils.log import DEFAULT_LOGGING

LOGLEVEL = os.environ.get("LOGLEVEL", "ERROR").upper()

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                # exact format is not important, this is the minimum information
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            },
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            # console logs to stderr
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            # default for all undefined Python modules
            "": {
                "level": LOGLEVEL,
                "handlers": ["console"],
            },
            # Our application code
            "sparkle": {
                "level": LOGLEVEL,
                "handlers": ["console"],
                # Avoid double logging because of root logger
                "propagate": False,
            },
            # Default runserver request logging
            "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)
