import psycopg2
from utilities.GetSecrets import GetSecrets


class PgConn():
    ''' Expects a filename as a str and a db_name as a str. 
    Returns a conn to a postgres db listed in the secrets.json.
    Implement by:
        filename = './secrets/secrets.json'
        db_name = "thor"
        conn = PgConn(filename, db_name)
    '''
    def __new__(cls, filename, db_name):
        # Grab all of our super secret stuff.

        thor_secrets = GetSecrets(filename, db_name)
        
        conn = psycopg2.connect(
        host=thor_secrets["host"],
        port=thor_secrets['port'],
        connect_timeout=5,
        database=thor_secrets['database'],
        user=thor_secrets['user'],
        password=thor_secrets['pass']
        )
        return conn


if __name__ == '__main__':
    filename = '../secrets/secrets.json'
    setting = "thor"
    PgConn(filename, setting)
