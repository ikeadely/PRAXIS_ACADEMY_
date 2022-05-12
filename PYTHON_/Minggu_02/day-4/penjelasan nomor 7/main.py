from containers import Readers, Clients, Configs
if __name__ == "__main__":
    Configs.config.override({
        "domain_name": "impa.gmail.com"
        "email_address": "YOUR_EMAIL_ADDRESS",
        "password": "YOUR_PASSWORD",
        "mailbox": "INBOX"
    })
    email_reader = Readers.email_readers()
    print (email_reader.read())