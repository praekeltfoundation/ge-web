from .base import *  # noqa
import dj_database_url
from os.path import abspath, dirname, join

DEBUG = False

PROJECT_ROOT = env.str("PROJECT_ROOT") or dirname(dirname(abspath(__file__)))
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///%s" % (join(PROJECT_ROOT, "geweb.db"),)
    )
}

SECRET_KEY = env.str("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

try:
    from .local import *
except ImportError:
    pass
