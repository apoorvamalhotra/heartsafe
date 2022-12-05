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
        print(request.json)
        return "success", 200
    else:
        abort(400)


# input_data = {
#     'PhysicalHealth':phy_health,
#     'Mentalhealth':men_health,
#     'PhysicalActivity':phy_activity,
#     'Sex':sex,
#     'Age':age,
#     'height':height,
#     'weight':weight,
#     'SmokingStatus':smoke,
#     'AlcoholConsumption':alcohol,
#     'Depression':depression,
#     'DifficultyWalking':walk,
#     'AverageSleep':avg_sleep,
#     'DiabetesHistory':diabetes,
#     'AsthmaHistory':aasthma
# }

# lr.parse_data(input_data)


if __name__ == "__main__":
    app.run()
