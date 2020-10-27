import csv
import pandas as pd
import scipy.spatial.distance as scidist


df = pd.read_csv(
    'B2P_Rwanda_matchedIDs_final_2020-09-24_copy.csv', index_col=0)

df_project_coord = df[['project_code', 'lat', 'long']]
df_population = pd.read_csv('population_rwa_2018-10-01.csv')

# manual fix for R127 line # 534
df_project_coord.iloc[534]['project_code'] = 88888

# distances
distances = scidist.cdist(
    df_population[:100000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.to_csv('closest01.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[100000:200000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(100000, 100000 + len(df_closest))
df_closest.to_csv('closest02.csv')

del closest
del df_closest


# #####

distances = scidist.cdist(
    df_population[200000:300000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(200000, 200000 + len(df_closest))
df_closest.to_csv('closest03.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[300000:400000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(300000, 300000 + len(df_closest))
df_closest.to_csv('closest04.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[400000:500000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(400000, 400000 + len(df_closest))
df_closest.to_csv('closest05.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[500000:600000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(500000, 500000 + len(df_closest))
df_closest.to_csv('closest06.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[600000:700000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(600000, 600000 + len(df_closest))
df_closest.to_csv('closest07.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[700000:800000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(700000, 700000 + len(df_closest))
df_closest.to_csv('closest08.csv')

del closest
del df_closest

# #####


distances = scidist.cdist(
    df_population[800000:900000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(800000, 800000 + len(df_closest))
df_closest.to_csv('closest09.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[900000:1000000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(900000, 900000 + len(df_closest))
df_closest.to_csv('closest10.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[1000000:1100000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(1000000, 1000000 + len(df_closest))
df_closest.to_csv('closest11.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[1100000:1200000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(1100000, 1100000 + len(df_closest))
df_closest.to_csv('closest12.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[1200000:1300000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(1200000, 1200000 + len(df_closest))
df_closest.to_csv('closest13.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[1300000:1400000].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(1300000, 1300000 + len(df_closest))
df_closest.to_csv('closest14.csv')

del closest
del df_closest

# #####

distances = scidist.cdist(
    df_population[1400000:].iloc[:, 0:2], df_project_coord.iloc[:, 1:], 'euclidean')

closest = []
for k, v in enumerate(distances):
    closest.append(v.argmin(axis=0))

df_closest = pd.DataFrame(closest)
df_closest.index = pd.RangeIndex(1400000, 1400000 + len(df_closest))
df_closest.to_csv('closest15.csv')

del closest
del df_closest
