import pymysql.cursors

connection = pymysql.connect(host='',
                             port=3306,
                             user='',
                             password='',
                             db='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        print(connection)
        # connection.cursor().execute("show tables")
        # connection.cursor().execute("DELETE FROM user")
        # print(connection.cursor().execute('CREATE TABLE `user` ( `codeUser`  INT PRIMARY KEY AUTO_INCREMENT, `email` varchar(50) NOT NULL,  `password` varchar(50) NOT NULL);'))
        # connection.cursor().execute('CREATE TABLE `files` (`id` INT AUTO_INCREMENT PRIMARY KEY,`mime` VARCHAR (255) NOT NULL,`data` BLOB NOT NULL);')
        # connection.commit()
        
        print('show database')
        print(cursor.execute("show tables"))
        # insert
        sql = 'INSERT INTO `user` (`email`,`password`) VALUES (%s,%s)'
        cursor.execute(sql, ('srpezo@gmail.com', 'diego'))
        # save
        connection.commit()

    with connection.cursor() as cursor:
        sql = 'SELECT `codeUser`, `password` FROM `user` WHERE `email`=%s'
        cursor.execute(sql, ('srpezo@gmail.com'))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()


def saveImage(mime,data):
    print('save-image')
    try:
        with  connection.cursor() as cursor:
            sql = "INSERT INTO `files` (`mime`,`data`) VALUES (%s,%s)"
            cursor.execute(sql,(mime,data))
            result = cursor.fetchone()
            return result
    finally:
        connection.close()


def readImage():
    print('read-image')
    try:
        with  connection.cursor() as cursor:
            sql = "SELECT * FROM `files`"
            cursor.execute(sql,(mime,data))
            result = cursor.fetchone()
            return result
    finally:
        connection.close()
