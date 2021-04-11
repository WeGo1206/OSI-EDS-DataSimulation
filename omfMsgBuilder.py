import json

def simDataMsg(dt,val1,val2,val3,val4,val5,val6):

    msg= [{"containerid":"MyCustomContainer",
                "values":
                    [{"Timestamp": dt,
                    "Value": val1
                    }]
    },{"containerid":"Sim.Gauss.505",
                "values":
                    [{"Timestamp": dt,
                    "Value": val2
                    }]
    },{"containerid":"Sim.Triangular.406050",
                "values":
                    [{"Timestamp": dt,
                    "Value": val3
                    }]
    },{"containerid":"Sim.Uniform.4060",
                "values":
                    [{"Timestamp": dt,
                    "Value": val4
                    }]
    },{"containerid":"Sim.Random.01",
                "values":
                    [{"Timestamp": dt,
                    "Value": val5
                    }]
    },{"containerid":"Sim.Pareto.1",
                "values":
                    [{"Timestamp": dt,
                    "Value": val6
                    }]
    }]
    return(json.dumps(msg))
