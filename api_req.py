import requests 

# Making a GET request 
r = requests.get('http://127.0.0.1:105/hello') 

# check status code for response received 
# success code - 200 
print(r) 

# print content of request 
print(r.content) 

