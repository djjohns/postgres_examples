import pandas as pd
from apply_sql_template import apply_sql_template
from engines.not_conns import Thor, Odin
from sql.test_tbl_sql import select_all_messages


class Db2Db():
    ''' Uses pandas to move a copy a table from on db to another.
    Expects src_db as a sqlalchemy conn, query as a str, target_tbl as a str, target_db as a sqlalchemy conn, and chunkz as a int.'''
    def __init__(self,src_db, query, target_tbl, target_db, chunkz):
        self.src_db = src_db
        self.query = query
        self.target_tbl = target_tbl
        self.target_db = target_db
        self.chunkz = chunkz
        for chunk in pd.read_sql(self.query, self.src_db, chunksize=self.chunkz):
            chunk.to_sql(self.target_tbl, self.target_db, if_exists='append', index=False, chunksize=self.chunkz)


if __name__ == '__main__':
    #TODO: Currently returns 'messages' and not messages.
    # params = {
    
    #     'src_tbl': 'messages',
    #     'view_name': 'top_10_messages'
    # }


    # sql = apply_sql_template(select_all, params)
    # print(sql)
    # Db2Db(Thor, sql, 'test_tbl', Odin, 5000)
    Db2Db(Thor, select_all_messages, 'test_tbl', Odin, 5000)
