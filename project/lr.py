import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# from sklearn import metrics
# from sklearn.metrics import accuracy_score, confusion_matrix


def parse_data(input_data):
    bmi = input_data["weight"] / ((input_data["height"] / 100) ** 2)

    if input_data["PhysicalHealth"] == 0:
        phy_health = 1
    elif input_data["PhysicalHealth"] >= 1 and input_data["PhysicalHealth"] <= 13:
        phy_health = 2
    else:
        phy_health = 3
    # elif missing:
    #     phy_health=9

    if input_data["MentalHealth"] == 0:
        men_health = 1
    elif input_data["MentalHealth"] >= 1 and input_data["MentalHealth"] <= 13:
        men_health = 2
    else:
        men_health = 3
    # elif missing:
    #     phy_health=9

    if input_data["PhysicalActivity"] == True:
        phy_activity = 1
    elif input_data["PhysicalActivity"] == False:
        phy_activity = 2
    else:
        phy_activity = 9

    if input_data["Sex"] == "Male":
        sex = 1
    else:
        sex = 2

    if input_data["Age"] >= 18 and input_data["Age"] <= 24:
        age = 1
    elif input_data["Age"] >= 25 and input_data["Age"] <= 34:
        age = 2
    elif input_data["Age"] >= 35 and input_data["Age"] <= 44:
        age = 3
    elif input_data["Age"] >= 45 and input_data["Age"] <= 54:
        age = 4
    elif input_data["Age"] >= 55 and input_data["Age"] <= 64:
        age = 5
    else:
        age = 6

    if bmi <= 18.50:
        bmi = 1
    elif bmi >= 18.50 and bmi < 25:
        bmi = 2
    elif bmi >= 25 and bmi < 30:
        bmi = 3
    else:
        bmi = 4

    if input_data["SmokingStatus"] == True:
        smoke = 2
    elif input_data["SmokingStatus"] == False:
        smoke = 1
    else:
        smoke = 9

    if input_data["Depression"] == True:
        depression = 1
    elif input_data["Depression"] == False:
        depression = 2
    else:
        depression = 7

    if input_data["DifficultyWalking"] == True:
        walk = 1
    elif input_data["DifficultyWalking"] == False:
        walk = 2
    else:
        walk = 7

    if input_data["DiabetesHistory"] == True:
        diabetes = 1
    elif input_data["DiabetesHistory"] == False:
        diabetes = 3
    else:
        diabetes = 7

    if input_data["AsthmaHistory"] == True:
        aasthma = 2
    elif input_data["AsthmaHistory"] == False:
        aasthma = 1
    else:
        aasthma = 9

    model(
        [
            [
                phy_health,
                men_health,
                phy_activity,
                sex,
                age,
                bmi,
                smoke,
                input_data["AlcoholConsumption"],
                depression,
                walk,
                input_data["AverageSleep"],
                diabetes,
                aasthma,
            ]
        ]
    )


def model(user_data):
    df1 = pd.read_csv("project/clean_data.csv")
    X = df1.drop("HeartHealth", axis=1)
    y = df1.HeartHealth

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
    w = {1: 6, 2: 1}
    logistic_regression = LogisticRegression(random_state=13, class_weight=w)

    logistic_regression.fit(X_train, y_train)
    # y_pred = logistic_regression.predict(X_test)
    # print('--------------')
    # print(y_pred)
    # accuracy = metrics.accuracy_score(y_test, y_pred)
    # accuracy_percentage = 100 * accuracy
    # print(accuracy_percentage)
    # cr = metrics.classification_report(y_test, y_pred)
    # print(cr)
    # print(f'Confusion Matrix: \n{confusion_matrix(y_test, y_pred)}')
    samp = logistic_regression.predict_proba(user_data)
    # samp1 = logistic_regression.predict(user_data)
    # print(samp)
    # print(samp1)
    # print(samp.item(0))
    return result(samp.item(0))


def result(val):
    if val * 100 > 9:
        return("unwell")
    else:
        return("well")
