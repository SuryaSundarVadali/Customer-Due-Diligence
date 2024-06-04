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


aadhar_number = input("Enter Aadhar Number: ")
pan_number = input("Enter PAN Number: ")
first_name = input("Enter First Name: ")
middle_name = input("Enter Middle Name: ")
last_name = input("Enter Last Name: ")
father_name = input("Enter Father's Name: ")
mother_name = input("Enter Mother's Name: ")
dob = input("Enter Date of Birth (YYYY-MM-DD): ")
profile_image = input("Enter Profile Image Path: ")
address = input("Enter Address: ")

# Insert the data
insertData(aadhar_number, pan_number, first_name, middle_name, last_name, father_name, mother_name, dob, profile_image, address)