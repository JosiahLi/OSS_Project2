# %%
import numpy as np
import pandas as pd

df = pd.read_csv("./2019_kbo_for_kaggle_v2.csv")  # read data

# %%
years = list(range(2015, 2019, 1))  # create a consecutive integer list

# %%
rows = ['Top' + str(i) for i in range(1, 11, 1)]  # row names
columns = ['H', 'avg', 'HR', 'OBP']  # column names


# %%
def printTop_by_year(year):
    # get the players whose hits are in Top 10
    top_hits_id = df[df['year'] == year]['H'].nlargest(10).index
    top_hits = df[df['year'] == 2015]['H'].nlargest(10)
    top_hits = df[df['year'] == year]['H'].nlargest(10)
    top_hits_name = df['batter_name'].loc[top_hits_id]
    top_hits_name = top_hits_name.values
    top_hits = top_hits.values
    top_hits = top_hits.astype('int32')
    top_hits = top_hits.astype(str)
    top_hits_name = top_hits_name + '(' + top_hits + ')'

    # get the players whose batting average is in Top 10
    top_avg_id = df[df['year'] == year]['avg'].nlargest(10).index
    top_avg = df[df['year'] == year]['avg'].nlargest(10)
    top_avg_name = df['batter_name'].loc[top_avg_id]
    top_avg_name = top_avg_name.values
    top_avg = top_avg.values
    # top_avg.apply(lambda x: round(x, 3))
    top_avg = np.round(top_avg, 3)
    top_avg = top_avg.astype(str)
    top_avg_name = top_avg_name + '(' + top_avg + ')'

    # get the players whose hometurns are in Top 10
    top_hr_id = df[df['year'] == year]['HR'].nlargest(10).index
    top_hr = df[df['year'] == year]['HR'].nlargest(10)
    top_hr_name = df['batter_name'].loc[top_hr_id]
    top_hr_name = top_hr_name.values
    top_hr = top_hr.values
    top_hr = top_hr.astype('int32')
    top_hr = top_hr.astype(str)
    top_hr_name = top_hr_name + '(' + top_hr + ')'

    # get the players whose on-base percentage is in Top 10
    top_obp_id = df[df['year'] == year]['OBP'].nlargest(10).index
    top_obp = df[df['year'] == year]['OBP'].nlargest(10)
    top_obp_name = df['batter_name'].loc[top_obp_id]
    top_obp_name = top_obp_name.values
    top_obp = top_obp.values
    top_obp = top_obp.round(3)
    top_obp = top_obp.astype(str)
    top_obp_name = top_obp_name + '(' + top_obp + ')'

    res = pd.DataFrame(
        {'H': top_hits_name,
         'avg': top_avg_name,
         'HR': top_hr_name,
         'OBP': top_obp_name},
        index=rows
    )

    print(res)

# Problem 1
print("Problem 1")
# for year in years:
for year in years:
    print(f"Year: {year}")
    printTop_by_year(year)
    print()

# %%
# Problem 2
print("Problem 2")
# get the players whose hits are in Top 10
top_hits_id = df[df['year'] == 2015]['H'].nlargest(10).index
top_hits = df[df['year'] == 2015]['H'].nlargest(10)
top_hits_name = df['batter_name'].loc[top_hits_id]
top_hits_name = top_hits_name.values

t = top_hits.values
t = t.astype('int32')
t = t.astype(str)
# top_hits_name + '(' + t + ')'

# %%
data = df[['batter_name', 'war', 'cp', 'year']]
data = data[data['year'] == 2018]
# data = data.applymap(lambda x: round(x, 3))
# extract the player who has the heighest war
data['war'] = data['war'].apply(lambda x: round(x, 3))
posu = data[data['cp'] == '포수']
posu = posu.drop('year', axis=1)
posu.iloc[posu['war'].values.argmax()].values
res = []
lusu1 = data[data['cp'] == '1루수']
lusu1 = lusu1.drop('year', axis=1)
res.append(lusu1.iloc[lusu1['war'].values.argmax()].values)

lusu2 = data[data['cp'] == '2루수']
lusu2 = lusu2.drop('year', axis=1)
res.append(lusu2.iloc[lusu2['war'].values.argmax()].values)

lusu3 = data[data['cp'] == '3루수']
lusu3 = lusu3.drop('year', axis=1)
res.append(lusu3.iloc[lusu3['war'].values.argmax()].values)

yugyoksu = data[data['cp'] == '유격수']
yugyoksu = yugyoksu.drop('year', axis=1)
res.append(yugyoksu.iloc[yugyoksu['war'].values.argmax()].values)

tsuiksu = data[data['cp'] == '좌익수']
tsuiksu = tsuiksu.drop('year', axis=1)
res.append(tsuiksu.iloc[tsuiksu['war'].values.argmax()].values)

tsonggynksu = data[data['cp'] == '중견수']
tsonggynksu = tsonggynksu.drop('year', axis=1)
res.append(tsonggynksu.iloc[tsonggynksu['war'].values.argmax()].values)

uiksu = data[data['cp'] == '우익수']
uiksu = uiksu.drop('year', axis=1)
res.append(uiksu.iloc[uiksu['war'].values.argmax()].values)
res

res = pd.DataFrame(res)
res.index = res[2].values
res = res.drop(2, axis=1)
# res.columns = ['batter_name', 'war']
res.columns = ['batter_name', 'war']
res.index = 'Best ' + res.index
print(res)
print("")
# %%
# Problem 3
print("Problem 3")
data = df[['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']]
corr = data.corrwith(df['salary'])
print(corr)
print("\n%s has the heighest correlation with salary." % corr.idxmax())

