import duckdb
from create_table import create_table
from delete_data import delete_data
from import_csv import import_csv
from export_result import export_result

def main():
    
    create_table()
    delete_data()
    import_csv()
    export_result()

main()