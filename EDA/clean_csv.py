import csv
import pandas as pd


df = pd.read_csv(
    'B2P_Rwanda_matchedIDs_final_2020-09-24_copy.csv', index_col=0)


# TODO: for some reason you cannot read in data in one stream. fix this.

df.iloc[752, 5:6] = 2309
df.iloc[97, 5:6] = 3704
df.iloc[97, 5:6] = 3704
df.iloc[145, 5:6] = 5204
df.iloc[196, 5:6] = 4515
df.iloc[384, 5:6] = 2307
df.iloc[816, 5:6] = 2305
df.iloc[881, 5:6] = 3111
df.iloc[1040, 5:6] = 2507
df.iloc[1050, 5:6] = 4210
df.iloc[1077, 5:6] = 2607
df.iloc[424, 5:6] = 2607
df.iloc[1109, 5:6] = 3705
df.iloc[1141, 5:6] = 5114
df.iloc[1418, 5:6] = 5503

# TODO: update statement

# Replace nulls with 9999999999
cols = ['sector_id', 'cell_id', 'village_id', 'community_served_1_id', 'community_served_2_id',
        'community_served_3_id', 'community_served_4_id', 'community_served_5_id']  # , 'col_2', 'col_3', 'col_4']
for col in cols:
    df[col] = df[col].apply(lambda x: int(x) if x == x else 9999999999)

# Bad character; alphanumeric value in integer field.
df['project_code'].iloc[534:535] = None
df.to_csv('test.csv', quoting=csv.QUOTE_NONNUMERIC)


# still missing sector IDs:# Rongi-Mataba? # Rambura-Rurembo # Murundi-Nyange # Kigoma-Maraba?
# Kibeho-Muganza # Muhima-Gisozi # Rubona-Nzige # Rubona-Mwurire # Kigoma-Ntongwe
# Gakenke-Minazi # Hindiro-Kageyo # Byimana-Nyarusange # Kibangu-Muhororo # Hindiro-Kageyo
# Matyazo-Ngororero # Muhororo-Ngororero


# with open('B2P_Rwanda_matchedIDs_final_2020-09-24_copy.csv', 'r') as file:
#     reader = csv.reader(file, delimiter = '\t')
#     for row in reader:
#         print(row)
# breakpoint()
