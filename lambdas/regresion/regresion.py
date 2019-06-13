import numpy as np
from sklearn.linear_model import LinearRegression
import json

def linear_regresion(event, context): 
    file=event["body"]
    dic=json.loads(file)    
    predecir=dic["predecir"]
    company=dic["company"]
    def js_r():
        with open("data.json") as f_in:
            return(json.load(f_in))

    data=js_r()
    x=[]
    y=[]
    for key,value in data[company].items():
        x.append(int(key))
        y.append(value)

    x = np.array(x).reshape((-1, 1))
    y = np.array(y)
    model=LinearRegression().fit(x,y)
    predictions=[]
    for num in range(13,13+predecir+1):
        y_pred=model.predict(np.array([num]).reshape((-1,1)))
        predictions.append(y_pred.tolist())
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({"response":predictions})
        }

#linear_regresion(4,"nextline")