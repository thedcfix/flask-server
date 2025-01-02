from flask import Flask, jsonify
from flask_wtf import CSRFProtect
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from configuration import config
from configuration.development import DevelopmentConfig

import logging
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace

import os

csrf = CSRFProtect()

# Just a global reference, not a Limiter instance yet
limiter = None

cors = CORS()

def create_app(config_env):
    global limiter

    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config[config_env])

    # Enable CORS
    cors.init_app(app)

    # CSRF Protection
    csrf.init_app(app)

    # Configure limiter with a Redis Cache storage based on configuration
    redis_uri = (f"redis://{app.config.get('REDIS_USERNAME')}:{app.config.get('REDIS_PASSWORD')}@{app.config.get('REDIS_HOST')}:{app.config.get('REDIS_PORT')}")

    # If limiter is not yet created, instantiate it now with the correct parameters
    if limiter is None:
        local_limiter = Limiter(
            key_func=get_remote_address,
            default_limits=app.config.get('DEFAULT_LIMITS', []),
            storage_uri=redis_uri,
        )
        # Assign it to the global limiter reference
        globals()['limiter'] = local_limiter
    else:
        # If already created (e.g., re-calling create_app), just update its config
        limiter.default_limits = app.config.get('DEFAULT_LIMITS', [])
        limiter.storage_uri = redis_uri

    # Limiter for calls coming from the same IP address. Used in routes 
    limiter.init_app(app)

    # Retrieve Application Insights Connection String
    APPLICATIONINSIGHTS_CONNECTION_STRING = os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING') or DevelopmentConfig.APPLICATIONINSIGHTS_CONNECTION_STRING

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s -- %(message)s', handlers=[logging.StreamHandler()])
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    # Configure Azure Monitor
    configure_azure_monitor(logger_name="app_logger", connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING)

    from .core_routes import core
    from .auth_routes import auth
    # Register Blueprint routes
    app.register_blueprint(core)
    app.register_blueprint(auth)
    
    return app
