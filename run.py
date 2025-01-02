import os
from app import create_app

# Determine configuration based on environment variable
config_name = os.getenv('FLASK_CONFIG_ENV') or 'development'

app = create_app(config_name)

if __name__ == '__main__':
    app.run()