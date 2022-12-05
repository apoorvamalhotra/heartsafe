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
                input_data['weight'] = i['number']
            elif i['field']['id']=='dDPp3UxDLnFG':
                input_data['Age'] = i['number']
            elif i['field']['id']=='ZPGfo1iDsBwO':
                input_data['height'] = i['number']
            elif i['field']['id']=='z6SHNEOtjhEK':
                input_data['Sex'] = i['choice']['label']
            elif i['field']['id']=='WhJg8Q3OFuJ9':
                input_data['PhysicalHealth'] = i['number']
            elif i['field']['id']=='FqwRAvDInTu4':
                input_data['MentalHealth'] = i['number']
            elif i['field']['id']=='HKGhfqjDlWbU':
                input_data['PhysicalActivity'] = i['boolean']
            elif i['field']['id']=='IA2EVmsVRJ1h':
                input_data['DifficultyWalking'] = i['boolean']
            elif i['field']['id']=='nQDh7Ibe33LH':
                input_data['AverageSleep'] = i['number']
            elif i['field']['id']=='LOLMp2JC3qJg':
                input_data['SmokingStatus'] = i['boolean']
            elif i['field']['id']=='f3YPJzD7Q18B':
                input_data['DiabetesHistory'] = i['boolean']
            elif i['field']['id']=='Jiyy7Mom0EXG':
                input_data['AsthmaHistory'] = i['boolean']
            elif i['field']['id']=='xW3NYa9odtnk':
                input_data['AlcoholConsumption'] = i['number']
            elif i['field']['id']=='l9W1Q0ebw3Qu':
                input_data['Depression'] = i['boolean']
        result = lr.parse_data(input_data)
        return result, 200
    else:
        abort(400)

   

if __name__ == "__main__":
    app.run()
