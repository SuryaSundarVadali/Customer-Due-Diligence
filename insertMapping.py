import mysql.connector

def insertData(address, isVerified):
    print("Inserting data into MySQL")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3306',
                                             user='root',
                                             password='password',
                                             database='test_schema')

        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO mapping_table
                          (address, isVerified) VALUES (%s,%s)"""

        # Convert data into tuple format
        insert_tuple = (address, isVerified)
        result = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print("Data inserted to MySQL successfully", result)

    except mysql.connector.Error as error:
        print("Failed inserting data into MySQL {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertData("0x93f189A1558a979B7D3dC0CF349BD4DD08a87c91", 0)
