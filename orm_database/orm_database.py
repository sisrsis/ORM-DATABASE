import motor.motor_asyncio
import asyncpg
import mariadb
import sys
from  orm_database.orm_query import *
class MariaDB:
    def __init__(self, host:str,port:int,user:str,password:str,database:str):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
    

    async def start(self):
        try:
            self.db = mariadb.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database)

        except:
            print("Error connecting maraidb")
            sys.exit(1)


    async  def teble_create_BaseModel(self,table:str , class_BaseModel):
        query = query_baseModel_create_table(table,class_BaseModel)
        cur = self.db.cursor() 
        cur.execute(query)
        self.db.commit()

    async def teble_create(self, table: str, field: dict):
        query = query_create_table(table,field)
        cur = self.db.cursor() 
        cur.execute(query)
        self.db.commit()

    async def insert_value(self, table: str, value: dict):
        query = query_insert_value(table,value)
        cur = self.db.cursor() 
        print(query)
        cur.execute(query)
        self.db.commit()


    async def insert_values(self, table: str, values: list):
        cur = self.db.cursor() 
        for value in values:
            query = query_insert_values(table=table,value=value)
            cur.execute(query)
        self.db.commit()


    async def select_all(self, table: str, filed: list, all: bool = False):
        cur = self.db.cursor()
        query = query_select(table=table,filed=filed,all=all)
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        data = {}
        data_row = []
        for a in result:
            print(a)
            conter = 0
            for b in a:
                data[filed[conter]] = b
                conter += 1
            data_row.append(dict(data))
        return data_row


    async def select_columns(self, table: str, filed: dict):
        cur = self.db.cursor()
        query = select_columns(table=table,filed=filed)
        fileds = list(filed.keys())
        try:
            
            cur.execute(query,(filed[fileds[0]],))
            row = cur.fetchone()
            return row
        except:
            return None



class PostgreSQL:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    async def start(self):
        self.db = await asyncpg.connect(host=self.host, user=self.user, password=self.password, database=self.database)


    async  def teble_create_BaseModel(self,table:str , class_BaseModel):
        query=query_baseModel_create_table(table,class_BaseModel)
        await self.db.execute(query)
        await self.db.close()


    async def teble_create(self, table: str, field: dict):
        query=query_create_table(table,field)
        await self.db.execute(query)
        await self.db.close()


    async def insert_value(self, table: str, value: dict):
        query = query_insert_value(table,value)
        await self.db.execute(query)
        await self.db.close()


    async def insert_values(self, table: str, values: list):
        for value in values:
            query = query_insert_values(table=table,value=value)
            await self.db.execute(query)
        await self.db.close()

    async def select_all(self, table: str, filed: list, all: bool = False):
        if all == True:
            query = "SELECT * FROM " + table
        if all == False:
            query = "SELECT "
            for a in filed:
                query = query + a + ","
            query = query[:-1]
            query = query + " FROM " + table

        print(query)
        stmt = await self.db.prepare(query)
        # for a in stmt:
        result = list(await stmt.fetch())
        data = {}
        data_row = []
        for a in result:
            conter = 0
            for b in a:
                data[filed[conter]] = b
                conter += 1
            data_row.append(dict(data))
        await self.db.close()
        print(data_row)
        return data_row


    async def select_columns(self, table: str, filed: dict):
        query = "SELECT * "
        query = query + " FROM "
        query = query + table + " WHERE "
        fileds = list(filed.keys())
        query = query + fileds[0]+"="+"$1"
        try:
            row = dict(await self.db.fetchrow(query, filed[fileds[0]]))
            return row
        except:
            return None


class Mongodb:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    async def start(self):
        self.clint = motor.motor_asyncio.AsyncIOMotorClient(self.url)
        self.database = self.clint[str(self.name)]

    async def insert_one(self, data: dict, collection: str):
        coll = self.database[collection]
        await coll.insert_one(data)
        return data

    async def find_one(self, data: dict, collection: str):
        coll = self.database[collection]
        result = await coll.find_one(data)
        if (result == None):
            return result
        else:
            result['_id'] = str(result["_id"])
            return result

    async def find(self, data: dict, collection: str):
        coll = self.database[collection]
        result = coll.find(data)
        arraydata = []
        async for a in result:
            a['_id'] = str(a['_id'])
            arraydata.append(a)
        return arraydata

    async def read_collection(self, collection: str):
        coll = self.database[collection]
        data = coll.find({})
        arraydata = []
        async for a in data:
            a['_id'] = str(a['_id'])
            arraydata.append(a)
        return arraydata

    async def replace_one(self, find_data: dict, replace_data: dict, collection: str):
        coll = self.database[collection]
        data = await coll.replace_one(find_data, replace_data)
        if data == None:
            return None
        else:
            return data

    async def update_one(self, find_data: dict, replace_data: dict, collection: str):
        coll = self.database[collection]
        data = await coll.update_one(find_data, {'$set': replace_data})
        if data == None:
            return None
        else:
            return data


    async def edit_one(self,find_data:dict,edit_data:dict,collection:str):
        coll = self.database[collection]
        result = await coll.find_one(find_data)
        if (result == None):
            return False
        else:
            result['_id'] = str(result["_id"])
            result.update(edit_data)
            data = await coll.replace_one(find_data, edit_data)
            return True
            

    async def delete_one(self, find: dict, collection: str):
        coll = self.database[collection]
        result = coll.delete_one(find)
        print(result)