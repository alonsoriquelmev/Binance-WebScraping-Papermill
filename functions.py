import psycopg2

def insert_to_table(df,tablename,schema,conn_raw):
    if len(df)>0:
        df_columns = list(df)
        columns = ",".join(df_columns)
        values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))
        insert_stmt = "INSERT INTO {} ({}) {}".format(schema+'.'+tablename,columns,values)
        cur = conn_raw.cursor()
        psycopg2.extras.execute_batch(cur,insert_stmt,df.values)
        print("Insert done!")
        return cur