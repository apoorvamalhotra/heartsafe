import pandas as pd

df = pd.read_csv("project/brfss2020.csv")
df1 = df[
    [
        "_PHYS14D",
        "_MENT14D",
        "_TOTINDA",
        "SEXVAR",
        "_AGE_G",
        "_BMI5CAT",
        "_RFSMOK3",
        "_DRNKWK1",
        "ADDEPEV3",
        "DIFFWALK",
        "SLEPTIM1",
        "DIABETE4",
        "ASTHMA3",
        "_MICHD",
    ]
].copy()
df1 = df1.rename(
    {
        "_PHYS14D": "PhysicalHealth",
        "_MENT14D": "Mentalhealth",
        "_TOTINDA": "PhysicalActivity",
        "SEXVAR": "Sex",
        "_AGE_G": "Age",
        "_BMI5CAT": "BMICategory",
        "_RFSMOK3": "SmokingStatus",
        "_DRNKWK1": "AlcoholConsumption",
        "ADDEPEV3": "DepressionHistory",
        "DIFFWALK": "DifficultyWalking",
        "SLEPTIM1": "AverageSleep",
        "DIABETE4": "DiabetesHistory",
        "ASTHMA3": "AsthmaHistory",
        "_MICHD": "HeartHealth",
    },
    axis="columns",
)
df1.dropna(inplace=True)
df1.to_csv("project/clean_data.csv", index=False)
