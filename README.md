# orm_database
```
from orm_database import PostgreSQL
from pydantic import BaseModel
import asyncio


class user(BaseModel):
    username : str
    password : str
    email : str






async def main():
    db = PostgreSQL(host="127.0.0.1",user="postgres",password="",database="")
    await db.start()
    await db.teble_create("users",{"username":"varchar","password":"varchar","email":"varchar"})
    await db.teble_create_BaseModel(table="users",class_BaseModel=user)


asyncio.run(main())
```

