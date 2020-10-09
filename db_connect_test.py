import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2

load_dotenv()


# # reference environment variable
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_HOST")


# connection = psycopg2.connect(database = DB_NAME, user=DB_USER, password = DB_PASSWORD, host = DB_HOST, port = '5432')
connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port='5432')
# connection = psycopg2.connect(database = DB_NAME, user=DB_USER, password = DB_PASSWORD, host = DB_HOST)

print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

# select all records from Bridges table
cursor.execute('SELECT * FROM public."Bridges" ORDER BY "ID" ASC ;')

# statement = f"""INSERT INTO "Bridges" ("ID", "country", "province", "district", "district_id", "sector", "sector_id", "cell", "cell_id", "village", "village_id", "name", "project_code", "type", "stage", "sub_stage", "individuals_directly_served", "span", "lat", "long", "community_served_1", "community_served_1_id", "community_served_2", "community_served_2_id", "community_served_3", "community_served_3_id", "community_served_4", "community_served_4_id", "community_served_5", "community_served_5_id", "form", "case_safe_id", "opportunity_id") VALUES
# (1, 'Rwanda', 'Western Province', 'Rusizi', 36, 'Giheke', 3605, 'Gakomeye', 360502, 'Buzi', 36050201, 'Buzi', 1014107, 'Suspended', 'Rejected', 'Technical', 0, 0, -2.42056, 28.9662, 'Buzi', 36050201, 'Kabuga', 36050203, 'Kagarama', 36050204, 'Gacyamo', 36050202, 'Gasheke', null, 'Project Assessment - 2018.10.29', 'a1if1000002e51bAAA', '006f100000d1fk1')"""

cursor.execute(statement)

result = cursor.fetchall()
print("RESULT:", type(result))
print(result)
# Result: [(0, 'Rwanda', 'Western Province', 'Rusizi', 36, 'Giheke', 3605, 'Gakomeye', 360502, 'Buzi', 36050201, 'Buzi', 1014107, 'Suspended', 'Rejected', 'Technical', 0, 0, -2.42056, 28.9662, 'Buzi', 36050201, 'Kabuga', 36050203, 'Kagarama', 36050204, 'Gacyamo', 36050202, 'Gasheke', None, 'Project Assessment - 2018.10.29', 'a1if1000002e51bAAA', '006f100000d1fk1')]
