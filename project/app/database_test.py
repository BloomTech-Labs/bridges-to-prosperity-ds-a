from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extensions import register_adapter, AsIs
import pandas as pd
# import json

# Load environment variables from .env
load_dotenv()


class PostgreSQL:
    def __init__(self):

        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_HOST")

        self.connection = psycopg2.connect(
            dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, host=self.DB_HOST, port='5432')

    def adapters(*args):
        for adapter in args:
            register_adapter(adapter, psycopg2._psycopg.AsIs)

    def cursor(self):
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)

    def close(self):
        self.connection.close()

    def fetch_query_records(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def fetch_query_given_project(self, project_code: int):
        cursor = self.connection.cursor()
        query = f"""SELECT * FROM public."Bridges" where project_code={project_code} """
        cursor.execute(query)
        result = cursor.fetchall()
        # df = pd.DataFrame(result, columns=columns)
        columns = ['ID', 'country', 'province', 'district', 'district_id', 'sector', 'sector_id', 'cell', 'cell_id', 'village', 'village_id', 'name', 'project_code', 'type', 'stage', 'sub_stage', 'individuals_directly_served', 'span', 'lat', 'long', 'community_served_1', 'community_served_1_id',
                   'community_served_2', 'community_served_2_id', 'community_served_3', 'community_served_3_id', 'community_served_4', 'community_served_4_id', 'community_served_5', 'community_served_5_id', 'form', 'case_safe_id', 'opportunity_id', 'inc_income', 'inc_income_rwf', 'inc_income_usd', 'bridge_image']
        df = pd.DataFrame(result, columns=columns)
        jsonified = df.to_json(orient='records')

        # breakpoint()
        return df.to_json(orient='records')
        # return result

    def fetch_query_given_project_and_columns(self, project_code: int, columns: []):
        cursor = self.connection.cursor()
        # breakpoint()
        query = f"""SELECT {str(columns).strip("[").strip("]")} FROM public."Bridges" where project_code={project_code} """
        cursor.execute(query)
        result = cursor.fetchall()
        # df = pd.DataFrame(result, columns=columns)
        # columns = ['ID', 'country', 'province', 'district', 'district_id', 'sector', 'sector_id', 'cell', 'cell_id', 'village', 'village_id', 'name', 'project_code', 'type', 'stage', 'sub_stage', 'individuals_directly_served', 'span', 'lat', 'long', 'community_served_1', 'community_served_1_id',
        #            'community_served_2', 'community_served_2_id', 'community_served_3', 'community_served_3_id', 'community_served_4', 'community_served_4_id', 'community_served_5', 'community_served_5_id', 'form', 'case_safe_id', 'opportunity_id', 'inc_income', 'inc_income_rwf', 'inc_income_usd', 'bridge_image']
        df = pd.DataFrame(result, columns=columns)
        df_json = df.to_json(orient='records')
        parsed = json.loads(df_json)
        return parsed

    def fetch_query(self, query: str, columns: list):
        self.fetch_query_records(query)
        df = pd.DataFrame(response, columns=columns)
        return df.to_json(orient=records)


query = 'SELECT * FROM public."Bridges" limit 5'
pg = PostgreSQL()
# print(pg.fetch_query_records(query))
print(pg.fetch_query_given_project(1007651))
# print(pg.fetch_query_given_project_and_columns(1007651, ['ID', 'country']))
