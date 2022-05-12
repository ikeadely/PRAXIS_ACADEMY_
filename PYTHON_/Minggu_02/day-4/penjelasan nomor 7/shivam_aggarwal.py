# dependency injection python

# example

# class EmailClient(object):
#     def __init__(self, config):
#         self._config = config
#     def connect(self, config):
#         pass

# class EmailReader(object):
#     def __init__(self, client):
#         try:
#             self._client = client
#         except Exception as e:
#             raise e    
#     def read(self):
            # pass 

from dependency_injector import providers, containers
from email_client import EmailClient
from email_reader import EmailReader

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
class Clients(containers.DeclarativeContainer):
    email_client = providers.Singleton(EmailClient, Configs.config)
class Readers(containers.DeclarativeContainer):
    email_reader = providers.Factory(EmailReader, client=Clients.email_client)

from containers import Readers, Clients, Configs
if __name__ == "__main__":
    Configs.config.override({
        "domain_name": "imap.gmail.com",
        "email_address": "YOUR_EMAIL_ADDRESS",
        "password": "YOUR_PASSWORD",
        "mailbox": "INBOX"
    })
    email_reader = Readers.email_reader()
    print (email_reader.read())

# ^^ gtw