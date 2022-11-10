import mysql.connector  
mydb = mysql.connector.connect(host = 'localhost',user = 'root',passwd = '12345678910',database = 'sql_store'
)
print('server is connected')