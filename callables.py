from utilities.Connections import PgConn
from sql.test_tbl_sql import top_10, grab_messages_schema, create_top_10_view, drop_view


# Specify json filename and db_name to look at.
filename = './secrets/secrets.json'
source_db_name = "thor"
target_db_name = "odin"
# PgConn returns the conn of the db we wish to connect to.
source_conn = PgConn(filename, source_db_name)
source_cur = source_conn.cursor() # Create our cursor.
target_conn = PgConn(filename, source_db_name)
target_cur = source_conn.cursor() # Create our cursor.

def grab_schema():
    ''' Uses an sql import to execute a SELECT statement. This statement inserts just the source table schema into the target table. '''
    tst = source_cur.execute(grab_messages_schema)
    print(grab_messages_schema)  # Print the sql ran.
    source_conn.commit()  # Commit our execute statements.
    print(source_cur.fetchone()) #
    print(tst)
    
def grab_top_10():
    ''' Uses an sql import to execute a SELECT statement.'''
    source_cur.execute(top_10)
    source_conn.commit()  # Commit our execute statements.
    print(top_10)  # Print the sql ran.
    print(source_cur.fetchall()) #
    # source_conn.commit()  # Commit our execute statements.
    
def create_view():
    ''' Uses an sql import to execute a SELECT statement.'''
    source_cur.execute(create_top_10_view)
    source_conn.commit()  # Commit our execute statements.
    print(create_top_10_view)
    
def drop_this_view():
    ''' Uses an sql import to execute a SELECT statement.'''
    source_cur.execute(drop_view)
    source_conn.commit()  # Commit our execute statements.
    print(drop_view) 
   


if __name__ == '__main__':
    # grab_top_10()
    # grab_schema()
    drop_this_view()
    create_view()
    source_cur.close()  # Close our cursor.
