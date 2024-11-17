from flask import Flask
from flask_cors import CORS
import requests

from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace
from logging import INFO, WARNING, DEBUG, ERROR, getLogger

import os
import configparser

# classes
###############################################################################

# Config class to read the config.ini file

class Config:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    @property
    def SECRET_KEY(self):
        return self.config['DEFAULT']['SECRET_KEY']

    @property
    def APPLICATIONINSIGHTS_CONNECTION_STRING(self):
        return str(self.config['DEFAULT']['APPLICATIONINSIGHTS_CONNECTION_STRING'])

config = Config()

# initialization
###############################################################################

# Set the environment variable at runtime
# Remove this in production and set the environment variable in the app service configuration
# ----

APPLICATIONINSIGHTS_CONNECTION_STRING = config.APPLICATIONINSIGHTS_CONNECTION_STRING

# Check if the connection string is None or empty
if not APPLICATIONINSIGHTS_CONNECTION_STRING:
    raise ValueError("APPLICATIONINSIGHTS_CONNECTION_STRING cannot be None or empty")

os.environ['APPLICATIONINSIGHTS_CONNECTION_STRING'] = APPLICATIONINSIGHTS_CONNECTION_STRING

# ----

# Definint log configuration. Fetches Connection String from APPLICATIONINSIGHTS_CONNECTION_STRING environment variable
configure_azure_monitor(logger_name="app_logger")
logger = getLogger("app_logger")
logger.setLevel(INFO)

# Example usage of the logger
# logger.info("info log")
# logger.warning("warning log")
# logger.error("error log")

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = 'APP_SECRET_KEY'

CORS(app)

# functions
###############################################################################


# routes
###############################################################################

@app.route('/')
def home():
    return config.secret_key

if __name__ == '__main__':
    app.run(debug=True)