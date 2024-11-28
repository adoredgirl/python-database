from db_operations import create_table, create_user, get_user, update_user, delete_user


while True:
  

    create_table()

    print('''\n1.Insert students info \n2.Update students info \n3.Delete students info \n4.Show students details \n5.Terminate project''')
    choice = input('Enter your choice: ')

    match choice:
        
        case '1':
        
            create_user()


        case '2':
            update_user()
          


        case '3':
            delete_user()
            

        case '4':
            get_user()
            

        case '5':
            print("project terminated")
            break
    
        case _:
            print("Invalid choice.please try again ")



