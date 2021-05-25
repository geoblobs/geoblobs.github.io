import pandas as pd

names = ["places_gicentre.csv", "places_3_DIVISION__13_Battalion_King's_Liverpool_Regiment.csv", "places_3_DIVISION__10_Battalion_Royal_Welsh_Fusiliers.csv"]

for name in names:
  df = pd.read_csv(name)
  df = df.drop(df[(df.country == "Italy") | (df.country == "IT")].index)
  df = df.drop(df[(df.country == "Switzerland") | (df.country == "CH")].index)
  df = df.drop(df[df.longitude < -10].index)

  df.to_csv("new_{0}".format(name), index=False)