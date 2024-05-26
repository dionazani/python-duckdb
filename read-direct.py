import duckdb

def read_direct():

    # directly read a CSV file from within SQL
    result = duckdb.sql("SELECT * FROM 'supermarket_sales_20240526.csv'")

    return result