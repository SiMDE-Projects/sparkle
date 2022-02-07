import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = "/static/"
STATIC_ROOT = "/static"
STATICFILES_DIRS = (
    os.path.join(
        BASE_DIR, "sparkle", "frontend", "dist"
    ),  # update the STATICFILES_DIRS
)
