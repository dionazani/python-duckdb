import duckdb

def delete_data():

    conn = duckdb.connect("dataset.duckdb")

    #create table
    sql = "DELETE FROM payment_staging"
    conn.execute(sql)

    conn.close()
