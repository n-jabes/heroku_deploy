import time
import serial
import requests
import os

while True: 
    if os.path.exists("transactions.txt") :
        file_data = ''
        transactions_file = open('transactions.txt')
        while True:
            line = transactions_file.readline()
            if not line: 
                break
            file_data += line + "\n"  

        formData = {"data": file_data}
        response = requests.post("https://my-first-heroku-application11.herokuapp.com/upload_data", data=formData)

        if response.status_code == 200 :
            print("Data uploaded!")

        os.remove("transactions.txt");
        ser = serial.Serial('COM3', 9600)
        ser.write(b'Data Uploaded')

       
        time.sleep(20)
    
    else :
        time.sleep(20)