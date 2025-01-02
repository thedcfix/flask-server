from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class DevelopmentConfig:
    # Application Configuration
    DEBUG = True
    SECRET_KEY = "\x16\xf9\xc2\xf5\xff\xc0s6\x10a\xcdD^\x9b\x97\x17\x01\x1665\xacWmp"

    # Redis Configuration
    REDIS_HOST = 'redis-19192.crce175.eu-north-1-1.ec2.redns.redis-cloud.com'
    REDIS_PORT = 19192
    REDIS_USERNAME = "default"
    REDIS_PASSWORD = "y5V0j0f9V82oWjiORLnsHYAvoHDOXAi6"
    REDIS_DB = 0  # Optional, defaults to 0 if not specified
    
    # Optional: Define Redis parameters if needed
    REDIS_MAX_MEMORY = '30mb'
    REDIS_EVICTION_POLICY = 'allkeys-lru'

    # Rate Limiting Defaults for Development
    DEFAULT_LIMITS = ["1000 per day", "200 per hour"]

    # Application Insights Configuration
    APPLICATIONINSIGHTS_CONNECTION_STRING = "InstrumentationKey=984ae61a-1299-4743-9798-e1fee4125bd6;IngestionEndpoint=https://swedencentral-0.in.applicationinsights.azure.com/;ApplicationId=202a4da3-2c39-415d-8d06-7c69aa532bfb"
    