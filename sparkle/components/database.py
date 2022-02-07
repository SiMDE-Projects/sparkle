import dj_database_url
import getconf

config = getconf.ConfigGetter("sparkle", ["./local_settings.ini"])
if config.getstr("DJANGO_SECRET") != "whatever":
    database = None
    if config.getstr("db.secret") != "":
        database = dj_database_url.parse(config.getstr("db.default"))
    DATABASES = {
        "default": database
        if database
        else dj_database_url.parse(config.getstr("db.default"))
    }
    DATABASES["default"]["ENGINE"] = "django.db.backends.mysql"
