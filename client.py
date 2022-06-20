import requests

file = open("transactions.txt","r+")
 
array = file.read()
  
data = {'array':array}

# print(data)

ser =serial.Serial ('COM4',9600)
ser.write('serial Data uploaded')
  
res = requests.post('http://127.0.0.1:5000/upload_data', data) 

returned_data = res.json() 
  
print(returned_data)
response = returned_data['response'] 
print("Reply from Node.js:", response)
file.close();