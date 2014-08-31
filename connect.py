import cql


def _insert_f1(cursor,prepared,array,parm):
    for elem in array:
        cursor.execute_prepared(prepared, {"param":param,"elem0":elem[0],"elem1":elem[1]},consistency_level='QUORUM')


def _get_f2(cursor,prepared,param):
    cursor.execute_prepared(prepared, {"param": param},consistency_level='QUORUM')
    return(cursor)




date='2012-05-24'

array=[[1,2]]

param=date 

#######################################################################
con1=cql.connect('mac1.sub.dom.com', cql_version="3.0.0")

cursor1 = con1.cursor()

cursor1.execute("use \"keyspace\"")

prepared1 = cursor1.prepare_query("""
     INSERT INTO "table_name" (param,elem0,elem1)
     VALUES (:param, :elem0, :elem1)
""")

_insert_f1(cursor1,prepared1,array,parm)
#######################################################################


#######################################################################
con2=cql.connect('mac1.sub.dom.com', cql_version="3.0.0")

cursor2 = con2.cursor()

cursor2.execute("use \"keyspace\"")

            
prepared_statement2 = cursor2.prepare_query("""
                  SELECT param,elem0,elem1
                  FROM table_name
                  WHERE param=:param
                  """)

cursor2=_get_f2(cursor2,prepared2,param)


for elem in cursor2:
    print elem           #Prints the elements of array returned

#cursor1.fetchone()   # returns  a single row

#cursor1.fetchall()   # returns  all rows
##########################################################################

cursor1.close()
con1.close()

cursor2.close()
con2.close()
