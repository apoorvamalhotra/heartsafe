# HeartSafe
## _Do your part, care for your Heart_
#### [49786] Software Engineering Management
`Apoorva Malhotra`
`Lucas (Xinyu) Hong`
`Maneesh Sharma`

## Problem Statement
Heart failure tops the list of causes of death. Symptoms as simple as sudden shortness of breath, tiredness and excessive smoking can be early indicators of your heart deteriorating and demand immediate attention. Heart Safe is a system where people can do a regular analysis of their heart health and keep a check.

### HeartSafe
Heart Safe is aimed at serving as a self-retrospective questionnaire which can help people identify potential risks about their heart health at an early stage and take actions before it is too late.

## How to run
Run the `app.py` file to execute the program. You can use the command :

```sh
python -m project.app
```

## About the Dataset
Behavioral Risk Factor Surveillance System is a collaborative project between all of the states and participating territories in US and the Centers for Disease Control and Prevention (CDC)
- Published : August 06, 2021
- The dataset consists of 279 attributes
- Shortlisted 14 attributes based on problem statement post consulting Dr. Susan Zhao, MD

Dataset References :
https://www.kaggle.com/datasets/aemreusta/brfss-2020-survey-data
https://www.cdc.gov/brfss/annual_data/2020/pdf/codebook20_llcp-v2-508.pdf

| Parameter Names as per BRFSS dataset | Parameter names used in Heart Safe App |
| ------ | ------ |
| _PHYS14D | PhysicalHealth |
| _MENT14D | Mentalhealth |
| _TOTINDA | PhysicalActivity |
| SEXVAR | Sex |
| _AGE_G | Age |
| _BMI5CAT | BMICategory |
| _SMOKER3 | SmokingStatus |
| _DRNKWK1 | AlcoholConsumption |
| ADDEPEV3 | DepressionHistory |
| DIFFWALK | DifficultyWalking |
| SLEPTIM1 | AverageSleep |
| DIABETE4 | DiabetesHistory |
| ASTHMA3 | AsthmaHistory |
| _MICHD | HeartHealth |
