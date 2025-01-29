

def query_baseModel_create_table(table,class_BaseModel):
    query = f"CREATE TABLE {table} ("
    result=class_BaseModel.model_json_schema()
    for a in result['required']:
        data = result['properties'][a]
        try : 
            maxLength = data['maxLength']
            match data['type']:
                case 'integer':
                    types = 'int'
                case 'boolean':
                    types = 'bool'
                case 'number':
                    types = 'float'
                case 'string':
                    types = 'varchar'
            if types == 'varchar':
                uint = str(a)+" "+types+"("+data["varchar"]+")"+'('+str(maxLength)+')'
                query = query  + " " + uint + " ,"
            else:
                uint = str(a)+" "+types+'('+str(maxLength)+')'
                query = query  + " " + uint + " ,"
        except :
            match data['type']:
                case 'integer':
                    types = 'int'
                case 'boolean':
                    types = 'bool'
                case 'number':
                    types = 'float'
                case 'string':
                    types = 'varchar'
            uint = str(a)+" "+types +"("+str(data["varchar"])+")"
            query = query  + " " + uint + " ,"
    query = query[:-1]
    query = query + ")"
    return query

def query_create_table(table:str,field:dict):
    query = f"CREATE TABLE {table} ("
    filed_key = list(field.keys())
    for a in filed_key:
        query = query + a + " " + field[a] + " ,"
    query = query[:-1]
    query = query + ")"
    return query



def query_insert_value(table:str,value:dict):
    uery = f"INSERT INTO {table}  ( "
    filed_key = list(value.keys())
    for a in filed_key:
        query = query + " " + a + " " + ","
    query = query[:-1]
    query = query + ")"
    query = query + " VALUES ("
    filed_value = list(value.values())
    for a in filed_value:
        query = query + " '" + str(a) + "' " + ","
    query = query[:-1]
    query = query + ")"
    return query