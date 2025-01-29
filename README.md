# Create table

```python
from orm_database import PostgreSQL
from pydantic import BaseModel
import asyncio


class User(BaseModel):
    username: str
    password: str
    email: str


async def main():
    db = PostgreSQL(host="127.0.0.1", user="postgres", password="", database="your_database_name")
    await db.start()
    
    await db.table_create("users", {"username": "varchar", "password": "varchar", "email": "varchar"})
    
    await db.table_create_BaseModel(table="users", class_BaseModel=User)


if __name__ == "__main__":
    asyncio.run(main())
```

## create table mariadb baseModel


```python
from orm_database import MariaDB
import asyncio
from pydantic import BaseModel , Field


db = MariaDB(host="127.0.0.1",database="login",password="",port=3306,user="root")

class users(BaseModel):
    user_rt : str = Field(varchar=20)
    password_rt : str = Field(varchar=20)
    email_rt : str = Field(varchar=20)


async def main():
    await db.start()
    await db.teble_create_BaseModel("tes",users)


asyncio.run(main())

```

## create table mariadb



```python
from orm_database import MariaDB
import asyncio


db = MariaDB(host="127.0.0.1",database="",password="",port=3306,user="root")




async def main():
    await db.start()
    await db.teble_create("test",{"username":"varchar(250)","email":"varchar(250)","old":"int"})


asyncio.run(main())
```

`test` name table

| name     |   field     |
| -------- | ----------- |
| username | varchar(250)|
| email    | varchar(250)|
| old      |    int      |





