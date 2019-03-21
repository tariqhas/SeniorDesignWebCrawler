import pymysql as mariadb
import pandas as pd

class DatabaseInterface:

    def __init__(self, db_config):
        # config validation
        try:
            self.user = db_config['user']
            self.password = db_config['password']
            self.database = db_config['database']
            self.host = db_config['host']
            self.port = db_config['port']
        except AttributeError:
            raise Exception(message='Database config format is not correct')

        self.conn = mariadb.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    db=self.database,
                                    port=self.port
                                    )

    #for select statements, will return all results
    def selectSql(self, query):
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    #for anything that modifies a table
    def modifySql(self, query):
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            cursor.commit()
        return

    def runStoredProcedure(self, procedureName, args): # args is a tuple of inputs to the procedure
        with self.conn.cursor() as cursor:
            cursor.callproc(procedureName, args)
            cursor.commit()
            res = cursor.fetchall()
            if res is not None:
                return res
            else:
                return

    def createNewDataTable(self, df, docid, attid):
        tablename = "table_" + str(docid) + '_' + str(attid)
        df.to_sql(name=tablename, con=self.conn, if_exists='overwrite')
        return tablename
