from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class ProductionConfig:
    DEBUG = False

    # Initialize the SecretClient with RBAC
    #KEY_VAULT_URL = "https://your-key-vault-name.vault.azure.net"
    #credential = DefaultAzureCredential()
    #client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)

    #SECRET_KEY = client.get_secret("app-service-production-secret-key").value

    # Redis Configuration
    #REDIS_HOST = client.get_secret("redis-cache-host-uri").value
    #REDIS_PORT = client.get_secret("redis-cache-host-port").value
    #REDIS_USERNAME = client.get_secret("redis-cache-username").value
    #REDIS_PASSWORD = client.get_secret("redis-cache-password").value
    #REDIS_DB = 0  # Optional, defaults to 0 if not specified
    
    # Optional: Define Redis parameters if needed
    #REDIS_MAX_MEMORY = '30mb'
    #REDIS_EVICTION_POLICY = 'allkeys-lru'

    # Rate Limiting Defaults for Production
    #DEFAULT_LIMITS = ["1000 per day", "200 per hour"]

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