import mysql.connector

# Convert digital data to binary format
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertData(aadhar_number, pan_number, first_name, middle_name, last_name, father_name, mother_name, dob, profile_image, address):
    print("Inserting data into MySQL")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3306',
                                             user='root',
                                             password='password',
                                             database='test_schema')

        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO new_table
                          (aadhar_number, pan_number, first_name, middle_name, last_name, father_name, mother_name, dob, profile_image, address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        profileImage = convertToBinaryData(profile_image)
        # Convert data into tuple format
        insert_tuple = (aadhar_number, pan_number, first_name, middle_name,
                        last_name, father_name, mother_name, dob, profileImage, address)
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


insertData("123456781234", "ABC1234", "Surya", "Sundar", "vadali", "pratap", "srivani", "2004-09-9", 'D:\Surya\College\Blockchain\KYC\Customer-Due-Diligence\photo.jpg', "0x93f189A1558a979B7D3dC0CF349BD4DD08a87c91")
