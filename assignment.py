import serial
import requests
message = ''
with open('transactions.txt') as f:
    while True:
        line = f.readline()
        if not line: 
            break
        message += line + "\n"  

formData = {"message": message, "SerialNumber": 45678}
post = requests.post("https://my-first-heroku-application11.herokuapp.com/create", data=formData)

if post.text :
    print("Data uploaded!")

# ser = serial.Serial('COM4', 9600)
# ser.write(b'Data Uploaded')


# r = requests.get("https://my-first-heroku-application11.herokuapp.com/")
# print(r.url)
# print(r.status_code)
# print(r.content)


# ser = serial.Serial(
#         port='COM13', #plz change this according to your port number
#         baudrate=9600,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS,
#         timeout=1
# )
# ser.flush()     

# messageInfo = ser.readline().decode('utf-8').rstrip()
# formData = {"message": messageInfo, "SerialNumber": 1234}
# post = requests.post("https://safe-house-bax`ckend.herokuapp.com/message/create", data=formData)
# print(post.text)