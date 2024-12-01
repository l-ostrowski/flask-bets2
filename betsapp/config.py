from flask import current_app

class Config(object):
    SECRET_KEY = "c874b801a7caf1be80c5ff8900a3dad08c7de89c"
    #DB_FILE = "./data/bets_euro24.db"
    DB_FILE = "./betsapp/data/bets_euro24.db"
    BONUS_DEADLINE = '14-06-2024 20:55'
    TIME_ZONE_OFFSET = +2 #differences in hours between server datetime and match datetime 
                            #(tells how much hours do we need to add to the server time)

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass


def AzureKV(app):
    from azure.keyvault.secrets import SecretClient
    from azure.identity import DefaultAzureCredential, CredentialUnavailableError
    import logging
    #logging.basicConfig(level=logging.INFO)
    #logging.info('Hello! App was started')

    credentials = DefaultAzureCredential()
    vault_url = "https://kv-azure-vault.vault.azure.net/"
    secret_name = "flask-bets-dbfile"

    secret_client = SecretClient(vault_url= vault_url, credential= credentials)

    secret = '0'
    try:
        secret = secret_client.get_secret(secret_name)
        db_file = secret.value
        #logging.info("db_file retrieved from Azure Vault:"  + db_file) 
        print("db_file retrieved from Azure Vault: " + db_file)
    except:
        #db_file = './data/bets_euro24.db'
        #logging.info("Secret was not retrieved. Hardcoded db_file will be used: " + db_file)
        print("Secret was not retrieved. Value from config file will be used: " + app.config["DB_FILE"])   





