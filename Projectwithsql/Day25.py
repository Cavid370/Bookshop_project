from xmlrpc.client import boolean
import pymysql.cursors
import sys
requ = sys.argv


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345',
                             database='Day25',
                             cursorclass=pymysql.cursors.DictCursor)


def create_table():
    with connection.cursor() as cursor:

        sql = """
            CREATE TABLE `Book_info` (
            `ID` int(11) NOT NULL AUTO_INCREMENT,
            `Title` varchar(255) NOT NULL,
            `Author` varchar(255) NOT NULL,
            `Published_at` date DEFAULT NULL,
            `Is_active` bit(1) NOT NULL DEFAULT b'1',
            `Genre` varchar(255) DEFAULT NULL,
            `Price` decimal(10,2) DEFAULT '10.00',
            PRIMARY KEY (`ID`)
            ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
    connection.commit()


def create_book(title, author, published, active, genre, price):
    with connection.cursor() as cursor:
        sql = """
            insert into Book_info (Title, Author, Published_at, Is_active, Genre, Price) values (%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(
            sql, (title, author, published, active, genre, price))
    connection.commit()

def show_all():
    with connection.cursor() as cursor:
        sql = """
           select * from book_info;
        """
        cursor.execute(sql)
        results = cursor.fetchall()
    print(results)

def show_book(id):
    with connection.cursor() as cursor:
        sql = """
           select * from book_info where id=%s;
        """
        cursor.execute(sql, id)
        results = cursor.fetchone()
    print(results)

def change_status(book_info_id):
    with connection.cursor() as cursor:
        sql = """
            UPDATE Book_info
            SET is_active = if(is_active=1, 0, 1)
            WHERE ID = %s;
        """
        cursor.execute(sql, (book_info_id))
    connection.commit()

def change_price(new_price,book_info_id):
    with connection.cursor() as cursor:
        sql = """
            UPDATE Book_info
            SET price=%s
            WHERE id = %s;
        """
        cursor.execute(sql, (new_price,book_info_id))
    connection.commit()

def remove_book(book_info_id):
    with connection.cursor() as cursor:
        sql = """
            DELETE FROM book_info WHERE id=%s
        """
        cursor.execute(sql, (book_info_id))
    connection.commit()

def search_author_title(searching,searching2):
    with connection.cursor() as cursor:
        sql = """
           select * from book_info where title=%s or author=%s  ;
        """
        cursor.execute(sql, (searching,searching2))
        results = cursor.fetchall()
    print(results)
    
if 'add' in requ and "table" in requ:
    create_table()

elif "add" in requ and "book" in requ:
    a = input("Kitabın adını qeyd edin:")
    b = input("Müəllifin adı:")
    c = input("Çap olunma tarixi:")
    f = boolean(input("Kitab mövcuddurmu?True/False:"))
    d = input("Kitabın janrı:")
    e = float(input("Qiymətini qeyd edin:"))
    create_book(a, b, c, f, d, e)


elif 'show' in requ and 'all' in requ:
    show_all()

elif 'show' in requ and 'book' in requ:
    Id = int(input("Göstərilməsini istədiyiniz kitabın İD -ni qeyd edin:"))
    show_book(Id)

elif "change" in requ and "status" in requ:
    id = int(input("Mövcudluğunu dəyişmək istədiyiniz kitabın İD -ni qeyd edin:"))
    change_status(id)

elif "change" in requ and "price" in requ:
    id = int(input("Qiymətini dəyişmək istədiyiniz kitabın İD -ni qeyd edin:"))
    new_price=int(input("Kitabın yeni qiyəti:"))
    change_price(new_price,id)

elif "remove" in requ:
    id = int(input("Silmək istədiyiniz kitabın İD -ni qeyd edin:"))
    remove_book(id)

elif "search" in requ:
    searching = (input("Axtarmaq istədiyiniz sözü qeyd edin:"))
    searching2=searching
    search_author_title(searching,searching2)

else:
    print("Wrong input")
