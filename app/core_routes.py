from flask import Blueprint, render_template, jsonify
from . import limiter
from logging import getLogger

core = Blueprint('core', __name__)

# Import the configured logger
logger = getLogger("app_logger")

@core.route('/')
def home():
    logger.info("Home page accessed")
    return render_template('core/index.html')

@core.route('/healthcheck')
def health():
    logger.info("Healthcheck endpoint accessed")
    return jsonify({"status": "healthy"}), 200