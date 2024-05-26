import duckdb

def import_csv():
    conn = duckdb.connect("dataset.duckdb")

    #import csv
    sql = """
    INSERT INTO payment_staging (invoice_id,branch,city,customer_type,gender,product_line,unit_price,quantity,invoice_date,invoice_time,payment)
    SELECT * FROM read_csv('supermarket_sales.csv',
    delim = ';',
    header = true,
    auto_detect = false,
    columns = {
        'invoice_id': 'varchar',
        'branch': 'varchar',
        'city': 'varchar',
        'customer_type': 'varchar',
        'gender' : 'varchar',
        'product_line': 'varchar',
        'unit_price': 'double',
        'quantity': 'integer',
        'invoice_date': 'date',
        'invoice_time': 'varchar',
        'payment': 'varchar'
    });
    """
    conn.execute(sql)

    conn.close()
