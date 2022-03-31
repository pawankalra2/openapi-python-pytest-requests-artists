import requests
import logging
import re
import os

SESSION = requests.Session()

#APP_URL = os.getenv("APP_URL", "")
#ADMIN_USER = os.getenv("ADMIN_USER", "")
#ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
APP_URL_ARTISTS = "https://example.io/v1/"
APP_URL_PETSSTORE = "https://petstore.swagger.io/v2/"
ADMIN_USER = "admin"
ADMIN_PASSWORD = "admin"

LOG = logging.getLogger()


class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, "*******")

        return True


LOG.addFilter(HideSensitiveData())
