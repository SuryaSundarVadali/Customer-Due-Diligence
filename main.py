import mysql.connector as connector
from datetime import date
import math, random

con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='password',
                        database='test_schema')

def write_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def rand_num_generator():
    global rand
    rand = random.randrange(len(questions))-1

def check_rand():
    rand_arr = []
    rand_num_generator()
    if rand not in rand_arr:
        rand_arr.append(rand)
    else:
        check_rand()


user_aadhar = input("Enter Aadhar number: ").lower()
query = 'select * from new_table where aadhar_number = {}'.format(user_aadhar)
cur = con.cursor()
cur.execute(query)
data = []
for row in cur:
    data = [row[0], row[1], row[2], row[3],
            row[4], row[5], row[6], row[7], row[8], row[9]]

file_name = "D:\Projects\Advanced Identity Verification\storage\image.png"
write_file(row[8], file_name)
print(data)

questions = ["What is your first name?", "What is your last name?", "What is the last 4 characters of your Aadhar?", "What is the last 4 characters of your PAN?", "What is the year of your birth?", "What is the month of your birth?", "What is the day of your birth?",
             "What is your father's first name?", "What is your mother's first name?"]

score = 0

if age(data[7])>=18:
    
    # Fetch Image and store it
    # Capture Image using OpenCV
    # Verify stored image with present image using OpenCV and AI
    
    user_pan = input("Enter PAN number: ").upper()
    if data[1]==user_pan:
        for i in range(3):
            check_rand()

            print(questions[rand])
            # Capture and verify picture
            answer = input().lower()
            # Capture and verify picture
            
            if rand == 0:
                if(answer == data[2].lower()):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            elif rand == 1:
                if(answer == data[4].lower()):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            elif rand == 2:
                if(answer == data[0][-4:]):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            elif rand == 3:
                if(answer == data[1][-4:].lower() or answer == data[1][-4:].upper()):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            elif rand == 4:
                if(int(answer) == data[7].year):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            elif rand == 5:
                if(int(answer) == data[7].month):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            elif rand == 6:
                if(int(answer) == data[7].day):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            elif rand == 7:
                if(answer == data[5].lower()):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
            else:
                if(answer == data[6].lower()):
                    score+=1
                    print("Next")
                else:
                    print("Retry")
                    break
        if score>=3:
            address = row[9]
            query = 'INSERT INTO mapping_table(isVerified) VALUES (1) where address = {}'.format(address)
            print("KYC Verified")
        else:
            print("KYC Not Verified")   
    else:
        print("User not found")
else:
    print("Age must be above 18")