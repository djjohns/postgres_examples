import psycopg2
from utilities.GetSecrets import GetSecrets


class PgConn():
    ''' 
    #### Supply filename to secrets.json and db_name. This Returns a conn while hidding all of our precious secrets.
    ### Args:
    filename (str): Path and filename of secrest.json.
    
    db_name (str): Name of the db we wish to connect to.
    
    ### Implement thusly.
    
    ```
    filename = './secrets/secrets.json'
    db_name = "thor"
    
    with PgConn(filename, db_name) as conn:
        cur = conn.cursor()
        cur.execute(some_sql_import)
        conn.commit()
        cur.close()
    ```
    '''
    def __new__(cls, filename, db_name):
        # Grab all of our super secret stuff.

        secrets = GetSecrets(filename, db_name)
        
        conn = psycopg2.connect(
        host = secrets["host"],
        port = secrets['port'],
        connect_timeout=5,
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass']
        )
        return conn


if __name__ == '__main__':
    filename = '../secrets/secrets.json'
    setting = "thor"
    PgConn(filename, setting)
