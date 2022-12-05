from flask import abort
from flask import Flask
from flask import request

from project import lr

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "Welcome to HeartSafe", 200
    

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        data = request.json['form_response']['answers']
        input_data={}
        for i in data:
        if i['field']['id']=='gEMD8GuvPTCN':
            d['weight'] = i['number']
        elif i['field']['id']=='dDPp3UxDLnFG':
            d['Age'] = i['number']
        elif i['field']['id']=='ZPGfo1iDsBwO':
            d['height'] = i['number']
        elif i['field']['id']=='z6SHNEOtjhEK':
            d['Sex'] = i['choice']['label']
        elif i['field']['id']=='WhJg8Q3OFuJ9':
            d['PhysicalHealth'] = i['number']
        elif i['field']['id']=='FqwRAvDInTu4':
            d['MentalHealth'] = i['number']
        elif i['field']['id']=='HKGhfqjDlWbU':
            d['PhysicalActivity'] = i['boolean']
        elif i['field']['id']=='IA2EVmsVRJ1h':
            d['DifficultyWalking'] = i['boolean']
        elif i['field']['id']=='nQDh7Ibe33LH':
            d['AverageSleep'] = i['number']
        elif i['field']['id']=='LOLMp2JC3qJg':
            d['SmokingStatus'] = i['boolean']
        elif i['field']['id']=='f3YPJzD7Q18B':
            d['DiabetesHistory'] = i['boolean']
        elif i['field']['id']=='Jiyy7Mom0EXG':
            d['AsthmaHistory'] = i['boolean']
        elif i['field']['id']=='xW3NYa9odtnk':
            d['AlcoholConsumption'] = i['number']
        elif i['field']['id']=='l9W1Q0ebw3Qu':
            d['Depression'] = i['boolean']
        result = lr.parse_data(input_data)
        return result, 200
    else:
        abort(400)

   

if __name__ == "__main__":
    app.run()
