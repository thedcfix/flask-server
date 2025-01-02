from flask import Blueprint, render_template
from . import limiter
from logging import getLogger

auth = Blueprint('auth', __name__, url_prefix='/auth')

# Import the configured logger
logger = getLogger("app_logger")

@auth.route('/login')
@limiter.limit("10 per minute")
def login():
    logger.info("Login attempt")
    return render_template('auth/login.html')