def query_baseModel_create_table(table,class_BaseModel):
    query = f"CREATE TABLE {table} ("
    result=class_BaseModel.model_json_schema()
    list_keys = result['properties']
    list_keys = list(list_keys.keys())
    type=""
    for a in list_keys:
        data = result['properties'][a]
        if len(data.keys()) == 2:
            match data["type"]:
                case "string":
                    type = "varchar"
                case "number":
                    type = "float"
                case "integer":
                    type = "int" 
                case "boolean":
                    type = "bool"
            query = query + a + " " + type + ","
        else :
            try:
                type = data["default"]
                query = query + a + " " + type + "," 
            except:    
                match data["type"]:
                    case "string":
                        type = f"varchar({data['varchar']})"
                    case "number":
                        type = "float"
                    case "integer":
                        type = "int" 
                    case "boolean":
                        type = "bool"
                
                query = query + a + " " + type + "," 
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
    query = f"INSERT INTO {table}  ( "
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

def query_insert_values(table:str,value:dict):
    query = f"INSERT INTO {table}  ( "
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



def query_insert_values_truple(table:str,key:dict):
    query = f"INSERT INTO {table}  ( "
    filed_key = list(key.keys())
    for a in filed_key:
        query = query + " " + a + " " + ","
    query = query[:-1]
    query = query + ")"
    query = query + " VALUES ("

    filed_value = list(key.values())
    namber = 1
    for a in filed_value:
        
        query = query + " " + "$" + str(namber) + " " + ","
        namber = namber + 1
    query = query[:-1]
    query = query + ")"
    return query

# print output SELECT * FROM tes
# print output SELECT user_rt FROM tes
def  query_select(table:str,filed:list,all:bool=False):
    if all == True:
        query = "SELECT * FROM " + table
    if all == False:
        query = "SELECT "
        for a in filed:
            query = query + a + ","
        query = query[:-1]
        query = query + " FROM " + table
        return query
    



def select_columns(table:str,filed:dict):
    query = "SELECT * "
    query = query + " FROM "
    query = query + table + " WHERE "
    fileds = list(filed.keys())
    query = query + fileds[0]+"="+"%s"
    return query


# DELETE FROM pending_order WHERE users='s1';
def query_delete_one(table:str,filed:dict):
    query = f"DELETE FROM {table} WHERE"
    key = filed.keys()
    key = list(key)
    key = key[0]
    query = query + " " +  str(key) + "="+ str(filed[key])
    return query



def query_update_one(table:str,find:dict,value:dict):
    query = f"UPDATE  {table} SET"
    key = find.keys()
    key = list(key)
    key = key[0]
    key_v = value.keys()
    key_v = list(key_v)
    key_v = key_v[0]
    query = query+ " " +  str(key_v)+ "='" + str(value[key_v]) + "' " +"WHERE" + " " +  str(key) + "="+ str(find[key]) 
    return query



def query_find_list(table:str,find:dict):
    query =  f"SELECT * FROM {table} WHERE"
    key =  list(find.keys())
    key = key[0]
    query = f"{query} {key}='{find[key]}'"
    return query