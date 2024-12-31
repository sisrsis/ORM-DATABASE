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
    
    # ایجاد جدول
    await db.table_create("users", {"username": "varchar", "password": "varchar", "email": "varchar"})
    
    # ایجاد مدل پایه
    await db.table_create_BaseModel(table="users", class_BaseModel=User)


if __name__ == "__main__":
    asyncio.run(main())
```