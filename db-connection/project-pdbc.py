import mysql.connector
import sys
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

while True:
    
    print('''\n1.Insert students info \n2.Update students info \n3.Delete students info \n4.Show students details \n5.Terminate project''')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        try:    
            insert_record = """insert into student(id, name, age) 
                                            values(%s, %s, %s)"""
            id = int(input('Enter id(int): '))
            name = str(input('Enter name(string): '))
            age = int(input('Enter age(int): '))
            
            c = connection.cursor()
            c.execute(insert_record,(id, name, age))
            connection.commit()
            print('Records inserted successfully')
        except Exception as e:
            print(e)

    elif choice == 2:
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

    elif choice == 3:
        try:
            delete_table = "delete from student where id = %s"
            
            id = int(input('Enter id to delete record(int): '))
            
            c = connection.cursor()
            c.execute(delete_table,(id,))
            connection.commit()
            print('Tables record deleted successfully')
        except Exception as e:
            print(e)

    elif choice == 4: 
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

    elif choice == 5:
        print('Project Terminated')
        sys.exit(0)
        
    else :
        print('Select choice from 1 to 5. Since invalid choice')