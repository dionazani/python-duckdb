import duckdb

def export_result():

    conn = duckdb.connect("dataset.duckdb")

    #select query
    sql = """
        COPY (SELECT strftime(today(),'%Y-%m-%d') as current, product_line, sum(unit_price * quantity) as total 
        FROM payment_staging group by product_line 
        ORDER BY total DESC) TO output.csv (HEADER, DELIMETER ';')
    """
    conn.execute(sql)

    conn.close()
