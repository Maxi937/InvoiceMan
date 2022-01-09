# Address to my Database named - "MyDB"

DB_HOST = "localhost"
DB_NAME = "my_db"
DB_USER = "postgres"
DB_PASS = "SrLt1075"

import psycopg2 as psy


# This function will take in ALL data from a table and order in based on the title of the column selected
def get_data(table, column_to_order_by):
    conn = psy.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)
    cur = conn.cursor()

    query_str = ("SELECT * FROM ")
    query_str += "{} ".format(table) 
    query_str += "ORDER BY "
    query_str += "\"{}\";".format(column_to_order_by)
    
    cur.execute(query_str)
    result = cur.fetchall()
    
    return result
    cur.close ()
    conn.close()

# This function should pull the headers of any table pulled into it
def get_column_headers(table):
    conn = psy.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)
    cur = conn.cursor()
    columns = []

    query_str = ("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE ")
    query_str += "table_name = '{}';".format(table) 

    cur.execute(query_str)
    column_names = cur.fetchall()

    for tup in column_names:
        columns += [tup[0]]

    return columns

    cur.close ()
    conn.close()


# get_data("invoice", "Reference")


def write_blob(part_id, path_to_file, file_extension):
    """ insert a BLOB into a table """
    conn = None
    try:
        # read data from a picture
        drawing = open(path_to_file, 'rb').read()
        # read database configuration
        params = psy.config()
        # connect to the PostgresQL database
        conn = psy.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)
        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO Invoice Documents(part_id,file_extension,drawing_data) " +
                    "VALUES(%s,%s,%s)",
                    (part_id, file_extension, psy.Binary(drawing)))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psy.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()