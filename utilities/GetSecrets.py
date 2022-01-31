import json


class GetSecrets():
    '''
    This a simple wrapper to load db conn settings stored in a json file.
    Expects filename as str and db_name as str.
        This class can be implemented as follows:
            filename = './secrets/secrets.json'
            db_name = "thor"
            thor_secrets = GetSecrets(filename, db_name)
            print(thor_secrets["host"])
    '''
    def __new__(cls, filename, setting):
        with open(filename) as secrets_file:
            secrets = json.load(secrets_file)
        try:
            return secrets[setting]
        except Exception as e:
            print(e)

            
            
if __name__ == '__main__':
    filename = './secrets/secrets.json'
    setting = "thor"
    thor_secrets = GetSecrets(filename, setting)
    print(thor_secrets["host"])
