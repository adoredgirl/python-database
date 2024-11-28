import mysql.connector

try:
    connection = mysql.connector.connect(
                                        user = 'root',
                                        password = 'Mariyashaikh@12345',
                                        host = 'localhost',
                                        database = 'pythondb1'
                                    )
    if connection.is_connected():
        print('Connection created successfully')
except Exception as e:
    print(e)

try:
    create_table = "create table if not exists student(id int primary key, name varchar(50), age int)"
    c = connection.cursor()
    c.execute(create_table)
    connection.commit()
    print('Table created successfully')
except Exception as e:
    print(e)

# try:    
#     insert_record = """insert into student(id, name, age) 
#                                     values(%s, %s, %s)"""
#     id = int(input('Enter id(int): '))
#     name = str(input('Enter name(string): '))
#     age = int(input('Enter age(int): '))
    
#     c = connection.cursor()
#     c.execute(insert_record,(id, name, age))
#     connection.commit()
#     print('Records inserted successfully')
# except Exception as e:
#     print(e)

try:
    update_table = "update student set name = %s, age = %s where id = %s"
    
    id = int(input('Enter id(int): '))
    name = str(input('Enter name(string): '))
    age = int(input('Enter age(int): '))
    
    c = connection.cursor()
    c.execute(update_table,(name, age, id))
    connection.commit()
    print('Tables record updated successfully')
except Exception as e:
    print(e)


# try:
#     delete_table = "delete from student where id = %s"
    
#     id = int(input('Enter id to delete record(int): '))
    
#     c = connection.cursor()
#     c.execute(delete_table,(id,))
#     connection.commit()
#     print('Tables record deleted successfully')
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