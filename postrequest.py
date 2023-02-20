import requests
import json

if __name__ == "__main__":

    # url = 'http://127.0.0.1:5000/postrequest'
    # myobj = {'message_key': 'message_val'}
    # url = 'http://10.71.160.33:5001/postrequest'
    # myobj = {'Name': 'Wanita'}
    url = 'http://10.51.160.50:5001/postrequest'
    myobj = {'Name': 'Wanita'}
    # myobj = {'Jrukruuuuuuuu'}
    

    x = requests.post(url, data = json.dumps(myobj))

    print(x.text) 

