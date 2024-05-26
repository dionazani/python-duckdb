import duckdb

def drop_table():

    conn = duckdb.connect("dataset.duckdb")

    #create table
    sql = "DROP TABLE payment"
    conn.execute(sql)

    conn.close()