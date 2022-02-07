import os
from pathlib import Path

import getconf

config = getconf.ConfigGetter("sparkle", ["./local_settings.ini"])
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = config.getbool("django.debug", False)
WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "./frontend/",
        "STATS_FILE": os.path.join(BASE_DIR, "./sparkle/frontend/webpack-stats.json"),
        "CACHE": not DEBUG,
    }
}
