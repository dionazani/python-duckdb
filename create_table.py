import duckdb

def create_table():

    conn = duckdb.connect("dataset.duckdb")

    #create table
    sql = """
    CREATE TABLE IF NOT EXISTS payment_staging(
        invoice_id varchar,
        branch varchar,
        city varchar,
        customer_type varchar,
        gender varchar, 
        product_line varchar,
        unit_price double,
        quantity integer,
        invoice_date date,
        invoice_time varchar,
        payment varchar)
    """
    conn.execute(sql)
    
    conn.close()