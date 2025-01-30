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



## insert value 

```python
from orm_database import MariaDB
import asyncio
from pydantic import BaseModel , Field


db = MariaDB(host="127.0.0.1",database="login",password="12341234",port=3306,user="root")

class users(BaseModel):
    user_rt : str = Field(varchar=20)
    password_rt : str = Field(varchar=20)
    email_rt : str = Field(varchar=20)


async def main():
    data = {"user_rt":"test1","password_rt":"12341","email_rt":"test1@mail.com"}
    await db.start()
    await db.teble_create_BaseModel("tes",users)
    await db.insert_values("tes",data)



asyncio.run(main())
```






## insert value list 


```python
from orm_database import MariaDB
import asyncio
from pydantic import BaseModel , Field


db = MariaDB(host="127.0.0.1",database="login",password="12341234",port=3306,user="root")

class users(BaseModel):
    user_rt : str = Field(varchar=20)
    password_rt : str = Field(varchar=20)
    email_rt : str = Field(varchar=20)


async def main():
    data = [{"user_rt":"test1","password_rt":"12341","email_rt":"test1@mail.com"},{"user_rt":"test2","password_rt":"12342","email_rt":"test2@mail.com"},{"user_rt":"test3","password_rt":"12343","email_rt":"test3@mail.com"}]
    await db.start()
    await db.teble_create_BaseModel("tes",users)
    await db.insert_values("tes",data)



asyncio.run(main())

```





# select database 
| user_rt | password_rt |    email_rt    |
| -----   | -----       | -------------- |
| test1   |    12341    | test1@mail.com |
| test2   |    12342    | test2@mail.com |
| test3   |    12343    | test3@mail.com |

```python
from orm_database import MariaDB
import asyncio
from pydantic import BaseModel , Field


db = MariaDB(host="127.0.0.1",database="login",password="12341234",port=3306,user="root")

class users(BaseModel):
    user_rt : str = Field(varchar=20)
    password_rt : str = Field(varchar=20)
    email_rt : str = Field(varchar=20)


async def main():

    await db.start()
    test = await db.select_all("tes",["user_rt","password_rt","email_rt"])
    print(test)




asyncio.run(main())



```
# output 
```json
[
{'user_rt': 'test1', 'password_rt': '12341', 'email_rt': 'test1@mail.com'},
{'user_rt': 'test2', 'password_rt': '12342', 'email_rt': 'test2@mail.com'},
{'user_rt': 'test3', 'password_rt': '12343', 'email_rt': 'test3@mail.com'}
 ]
 ```


SELECT ONE ROW

```python
from orm_database import MariaDB
import asyncio
from pydantic import BaseModel , Field


db = MariaDB(host="127.0.0.1",database="login",password="12341234",port=3306,user="root")

class users(BaseModel):
    user_rt : str = Field(varchar=20)
    password_rt : str = Field(varchar=20)
    email_rt : str = Field(varchar=20)


async def main():

    await db.start()
    test = await db.select_columns("tes",{"user_rt":"test1"})
    print(test)




asyncio.run(main())

```

output

```
('test1', '12341', 'test1@mail.com')
```