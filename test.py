from utilities.Connections import PgConn
from sql.test_tbl_sql import grab_test_tbl_schema, drop_test_tbl


# Specify json filename and db_name to look at.
filename = './secrets/secrets.json'
db_name = "thor"
# PgConn returns the conn of the db we wish to connect to.
conn = PgConn(filename, db_name)
cur = conn.cursor() # Create our cursor.

def drop_tbl():
    ''' Uses an sql import to execute a DROP TABLE statement. '''
    cur.execute(drop_test_tbl)  # Drop out table.
    print(drop_test_tbl)  # Print the sql ran.
    conn.commit()  # Commit our execute statements.

def grab_schema():
    ''' Uses an sql import to execute a SELECT statement. This statement inserts just the source table schema into the target table. '''
    cur.execute(grab_test_tbl_schema)
    print(grab_test_tbl_schema)  # Print the sql ran.
    conn.commit()  # Commit our execute statements.
   


if __name__ == '__main__':
    drop_tbl()
    grab_schema()
    cur.close()  # Close our cursor.
