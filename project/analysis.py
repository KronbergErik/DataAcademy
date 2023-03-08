import pandas as pd

df_wind = pd.read_json(r'/Users/erik.kronberg/Desktop/dataAcademy/wind.json')

df_consumption = pd.read_json(r'/Users/erik.kronberg/Desktop/dataAcademy/consumption.json')

#print(dfTotElec)
#print(dfWind)

#Added a comment for git
ElecByWind = df_wind['value']

totElec = df_consumption['value']

#Merge together
df_merged = df_wind.merge(df_consumption,on=['start_time','end_time'])

df_merged.rename(columns = {'value_x':'Wind', 'value_y':'Consumption'}, inplace = True)

df_merged['WindElec/TotElec'] = df_merged['Wind']/df_merged['Consumption']

print(df_merged)


totElecbyWind = ElecByWind.sum()/totElec.sum()

print(totElecbyWind)