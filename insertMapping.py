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

insertData("0xB245B4DBEe83064CDd975D31Af9edA5f6a4508A4", 0)
