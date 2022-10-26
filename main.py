import mysql.connector as connector
from datetime import date
import math, random
import face_recognition
import cv2
import numpy as np
import os, sys, glob
import matplotlib.pyplot as plt

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

def remove_img():
    os.remove('storage\\temp_image.png')
    os.removedirs('storage')

def verify_img():
    # Fetch Image
    img_bgr = face_recognition.load_image_file('storage\\temp_image.png')
    img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    face = face_recognition.face_locations(img_rgb)[0]
    face_encode = face_recognition.face_encodings(img_rgb, model='cnn')[0]
    # Capture Image using OpenCV
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    rgb_small_frame = small_frame[:, :, ::-1]
    while( len(face_recognition.face_encodings(rgb_small_frame))<1):
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        rgb_small_frame = small_frame[:, :, ::-1]
    test_encode = face_recognition.face_encodings(rgb_small_frame)[0]
    print('Image is captured')
    # Verify stored image with present image using OpenCV
    print(face_recognition.compare_faces([face_encode],test_encode))
    cv2.rectangle(img_bgr,(face[3],face[0]),(face[1],face[2]),(255,0,255),1)
    cv2.imshow("a",test_encode)
    cv2.waitKey(1)
    if face_recognition.compare_faces([face_encode],test_encode) != [True]:
        remove_img()
        sys.exit("Issue matching the face")


user_aadhar = input("Enter Aadhar number: ").lower()
query = 'select * from new_table where aadhar_number = {}'.format(user_aadhar)
cur = con.cursor()
cur.execute(query)
data = []
for row in cur:
    data = [row[0], row[1], row[2], row[3],
            row[4], row[5], row[6], row[7], row[8], row[9]]

# Store the file temporaily
file_name = "storage\\temp_image.png"
write_file(row[8], file_name)

questions = ["What is your first name?", "What is your last name?", "What is the last 4 characters of your Aadhar?", "What is the last 4 characters of your PAN?", "What is the year of your birth?", "What is the month of your birth?", "What is the day of your birth?",
             "What is your father's first name?", "What is your mother's first name?"]

score = 0

if age(data[7])>=18:
    
    # Verify image captured
    verify_img()
      
    user_pan = input("Enter PAN number: ").upper()
    if data[1]==user_pan:
        for i in range(3):
            check_rand()

            # Print question
            print(questions[rand])
            # Capture and verify picture
            verify_img()
            # Input answer
            answer = input().lower()
            # Capture and verify picture
            verify_img()
            
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
            remove_img()
            print("KYC Verified")
        else:
            remove_img() 
            print("KYC Not Verified")
    else:
        remove_img()
        print("User not found")
else:
    remove_img()
    print("Age must be above 18")