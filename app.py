import os
def create_file(filename):
    try:
        with open(filename,'x')as f:
            print(f"File Name{filename}: Created Successfully")
            
    except FileExistError:
        print(f"File Name already exist")
        
    except Exception as E:
        print('An error occurred')            
        
def view_all_files():
    files = os.listdir()
    if not files:
        print("no file found")
    else:
        print("Files in directory")
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully')
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occurred")
        
def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()  
            print(f"Content of '{filename}' :\n{content}")   
    except FileNotFoundError:
        print(f"{filename} does not found") 
        
    except Exception as e:
        print("an error occurred")    
        
        
def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f :
            content=input('enter data to add')
            f.write(content+ "\n")
            print("content added to {filename} Successfully")
    except FileNotFoundError:
        print(f"{filename} does not found")
        
    except Exception as e:
        print("an error occurred") 
        
def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: Create file')         
        print('2: view all files')         
        print('3: delete file')         
        print('4: read file')         
        print('5: edit file')         
        print('6: exit file')         
        
        choice=input("enter ur choice(1-6)")
        if choice == '1':
            filename= input("Enter the file-name to create ")
            create_file(filename)
               
        elif choice =='2':
            view_all_files()
            
        elif choice == '3':
            filename = input('enter the name of the file u want to delete')
            delete_file(filename)
            
        elif choice =='4':
            filename=input('enter the file name to read')
            read_file(filename)
        elif choice =='5':
             filename=input('enter the file name to edit')
             edit_file(filename)
        elif choice =='6' :
            print('closing the app....')
            break
        else:
            print("invalid syntax thank you")    
            
if __name__ =="__main__":
    main()            
            
                                      
                   
