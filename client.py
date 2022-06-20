import requests
import serial

file = open("transactions.txt","r+")
 
array = file.read()
  
data = {'array':array}

# print(data)

# ser =serial.Serial ('COM4',9600)
# ser.write('serial Data uploaded')
  
res = requests.post('https://my-first-heroku-application11.herokuapp.com/upload_data', data) 

returned_data = res.json() 
  
print(returned_data)
response = returned_data['response'] 
print("Reply from Node.js:", response)
file.close();