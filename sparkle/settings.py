import getconf
from split_settings.tools import include

config = getconf.ConfigGetter("sparkle", ["./local_settings.ini"])

include(
    "components/*.py",
)
