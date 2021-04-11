import random
import time
import requests
import datetime

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
        data= '[{\
                "containerid": "MyCustomContainer",\
                "values":\
                    [{"Timestamp": \"-time\",\
                    "Value": -val}]\
                },{\
                "containerid": "Sim.Gauss.505",\
                "values":\
                    [{"Timestamp": \"-time\",\
                    "Value": -gauss}]\
                },{\
                "containerid": "Sim.Triangular.406050",\
                "values":\
                    [{"Timestamp": \"-time\",\
                    "Value": -triangular}]\
                },{\
                "containerid": "Sim.Uniform.4060",\
                "values":\
                    [{"Timestamp": \"-time\",\
                    "Value": -uniform}]\
                },{\
                "containerid": "Sim.Random.01",\
                "values":\
                    [{"Timestamp": \"-time\",\
                    "Value": -random1}]\
                },{\
                "containerid": "Sim.Pareto.1",\
                "values":\
                    [{"Timestamp": \"-time\",\
                    "Value": -pareto1}]\
                }]'
        data= data.replace("-time", dt)
        data= data.replace("-val", str(val))
        data= data.replace("-gauss", str(gauss))
        data= data.replace("-triangular", str(triangular))
        data= data.replace("-uniform", str(uniform))
        data= data.replace("-random1", str(random1))
        data= data.replace("-pareto1", str(pareto1))

        print("Timestamp  =   ",dt)
        print("Custom     =   ",val)
        print("Gauss      =   ",gauss)
        print("Triangular =   ",triangular)
        print("Uniform    =   ",uniform)
        print("Random1    =   ",random1)
        print("Pareto     =   ",pareto1)
        print("--------------------------------------------")       


        print(data)
        r= requests.post(url=url, data=data, headers=headers )

        time.sleep(10)

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass


