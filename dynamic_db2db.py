from apply_sql_template import apply_sql_template
from sql.test_tbl_sql import select_all


params = {
    
    'src_tbl': 'messages',
    'view_name': 'top_10_messages'
}


sql = apply_sql_template(select_all, params)
print(sql)

