import random
import time
import requests
import datetime
import omfMsgBuilder as omf

# data= '[{"containerid": "MyCustomContainer","values": [{"Timestamp": \"2021-04-10T10:18:24.9870136Z\","Value": 12345.6789},{"Timestamp": \"2012-04-10T10:18:25.9870136Z\","Value": 12346.6789}]}]'

url= "http://localhost:5590/api/v1/tenants/default/namespaces/default/omf"
headers = {'content-type': 'application/json','producertoken': 'x','omfversion': '1.1', 'action': 'create','messageformat': 'json','messagetype': 'data'}

try:
    while True:
        val= random.uniform(-100,100)
        gauss= random.gauss(50,5)
        triangular= random.triangular(40,60,50)
        uniform= random.uniform(40,60)
        random1= random.random()
        pareto1= random.paretovariate(1)
        now= datetime.datetime.utcnow()
        dt= now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        
        data= omf.simDataMsg(dt,val,gauss,triangular,uniform,random1,pareto1)

        print("Timestamp  =   ",dt)
        print("Custom     =   ",val)
        print("Gauss      =   ",gauss)
        print("Triangular =   ",triangular)
        print("Uniform    =   ",uniform)
        print("Random1    =   ",random1)
        print("Pareto     =   ",pareto1)
        print("--------------------------------------------")       


        #print(data)
        r= requests.post(url=url, data=data, headers=headers )
        #print(r.text)

        time.sleep(10)

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass


