from sql.test_tbl_sql import drop_test_table
from utilities.Connections import PgConn


class CleanTestTables():
    '''
    ### Cleans out our test table.
    #### Args:
    query (str): The query to be executed. This can be imported from another module.
    
    filename (str): The filename ans path to our secrets.json.
    
    db_name (str): The database name we wish to connect to in the secrets.json.
    ### Implement thusly
    ```
    from sql.test_tbl_sql import drop_test_table
    
    filename = './secrets/secrets.json'
    db_name = "odin"
    CleanTestTables(drop_test_table, filename, db_name)
    ```
    '''
    def __init__(self, query, filename, db_name):
        self.query = query
        self.filename = filename
        self.db_name = db_name

        with PgConn(self.filename, self.db_name) as conn:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            cur.close()
            print(query)



if __name__ == '__main__':
    filename = './secrets/secrets.json'
    db_name = "odin"
    CleanTestTables(drop_test_table, filename, db_name)
