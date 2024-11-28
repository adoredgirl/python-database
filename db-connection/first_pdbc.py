import mysql.connector

try:
    connection = mysql.connector.connect(
                                        user ='root',
                                        password ='Mariyashaikh@12345',
                                        host='localhost',
                                        database = 'pythondb1'
                                        )
    
    if connection.is_connected():
        print('Connection created successfully')
except Exception as e:
    print(e)

try:
    create_table ="create table if not exists student(id int primary key, name varchar(50),age int)"
    c = connection.cursor()
    c.execute(create_table)
    connection.commit()
    print('Table created successfully')
except Exception as e:
    print(e)



# try:
#     insert_record = """ insert into student(id,name,age)
#                                     values(1,'Mariya',20),
#                                           (2,'Mustafa',24),
#                                           (3,'Usama',28)"""
    
#     c = connection.cursor()
#     c.execute(insert_record)
#     connection.commit()
#     print('Record is inserted successfully')
# except Exception as e:
#     print(e)


# try:
#     update_table ="update student set name ='arya',age = 21 where id = 2"
#     c = connection.cursor()
#     c.execute(update_table)
#     connection.commit()
#     print('Table recird updated successfully')
# except Exception as e:
#     print(e)



try:
    show_table = "select * from student"
    c = connection.cursor()
    c.execute(show_table)
    records = c.fetchall()
    print('\nRecords from the table are:\n')
    for record in records:
        print(record)   
except Exception as e:
    print(e)



    
# try:
#     delete_table = "delete from student where id = 2"
#     c = connection.cursor()
#     c.execute(delete_table)
#     connection.commit()
#     print('Tables record deleted successfully')
# except Exception as e:
#     print(e)

