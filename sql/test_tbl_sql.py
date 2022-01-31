
# Selects the top ten rows from a table.
top_10 = f'''
SELECT * FROM {{ src_tbl }} ORDER BY id desc LIMIT 10;
'''

# Creates a view of the top 10 rows from a table name.
create_top_10_view = f'''
CREATE VIEW {{ view_name }} AS
SELECT * 
FROM {{ src_tbl }}
ORDER BY id DESC
LIMIT 10;
'''

# Select all from a table.
select_all = 'SELECT * FROM {{ src_tbl }}'


# Copies schema from one table to another.
grab_tbl_schema = f'''
SELECT * FROM {{ src_tbl }} WHERE 1 = 2;
'''

# Drops a table from the current db.
drop_tbl = f'''
DROP TABLE IF EXISTS {{ src_tbl }} CASCADE;
'''

# drops a view in the current db.
drop_view = f'''
DROP VIEW IF EXISTS {{ view_name }};
'''

## NON TEMPLMENTED SQL!
# Select all from a table.
select_all_messages = '''SELECT * FROM messages'''