from db_config import create_connection

def create_table():

    try:
        connection = create_connection()
        create_table = "create table if not exists student(id int primary key, name varchar(50), age int)"
        c = connection.cursor()
        c.execute(create_table)
        connection.commit()
        c.close()
        connection.close()
    except Exception as e:
          print(e)


def create_user():
    try:    
        connection = create_connection()
        insert_record = """insert into student(id, name, age) 
                                        values(%s, %s, %s)"""
        id = int(input('Enter id(int): '))
        name = str(input('Enter name(string): '))
        age = int(input('Enter age(int): '))
        
        c = connection.cursor()
        c.execute(insert_record,(id, name, age))
        connection.commit()
        print('Records inserted successfully')
        c.close()
        connection.close()
    except Exception as e:
        print(e)


def get_user():
        try:
            connection = create_connection()
            show_table = "select * from student"
            c = connection.cursor()
            c.execute(show_table)
            records = c.fetchall()
            print('\nRecords from the table are:\n')
            for record in records:
                print(record) 
            c.close()
            connection.close()  
        except Exception as e:
            print(e)


def update_user():
        
        try:
            connection = create_connection()
            update_table = "update student set name = %s, age = %s where id = %s"
            
            id = int(input('Enter id(int): '))
            name = str(input('Enter name(string): '))
            age = int(input('Enter age(int): '))
            
            c = connection.cursor()
            c.execute(update_table,(name, age, id))
            connection.commit()
            print('Tables record updated successfully')
            c.close()
            connection.close()
        except Exception as e:
            print(e)


def delete_user():
      
        try:
            connection = create_connection()
            delete_table = "delete from student where id = %s"
            
            id = int(input('Enter id to delete record(int): '))
            
            c = connection.cursor()
            c.execute(delete_table,(id,))
            connection.commit()
            print('Tables record deleted successfully')
            c.close()
            connection.close()
        except Exception as e:
            print(e)
