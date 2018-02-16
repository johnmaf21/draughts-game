conn = mysql.connector.connect(user='root', password='?',host='?',database='?')

cursor = conn.cursor
def onClcick(username,passwaord):
    sqlQuery="SELECT * from tablename where username="


    cursor.execute(tmp_query)



conn.close()
