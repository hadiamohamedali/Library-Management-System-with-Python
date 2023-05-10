def writeBook():
    with open('BookPy.txt' , 'a') as file:
        c = 'y'
        while c == 'y':
            title = input('Enter The Book Title : ')
            auther = input('Enter The Book Auther : ')
            serial = input('Enter The Book Serial Number :')
            date = input('Enter The Book publish Date : ')
            file.write(title+'\t'+auther +'\t'+serial+'\t'+date+'\n')
            c = input('Do You Want To Add Record Again..??(y / n)')
        print('...File Saved Successfully...')

def readBook():
    with open('BookPy.txt' , 'r') as file:
        print('Title\tAuther\tSerialNumber\tdatePublish')
        print('---------------------------------------------------')
        for line in file:
            print(line , end = '')

def searchBook():
    title = input('Enter The Book Title to Search : ')
    with open('BookPy.txt' , 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t')
            if fields[0] == title:
                found = True
                print('Title\tAuther\tSerailNumber\tdatePublish')
                print('-----------------------------------------------------------')
                print(line)
        if not found:
            print('...Book Not Found...')

def updateBook():
    import os
    title = input('Enter The Book Title to Update: ')
    file = open('BookPy.txt' , 'r')
    tempFile = open('TempBook.txt' , 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == title:
           found = True
           serial = input('Enter The New Serial Number For this Book : ')
           line = fields[0] +'\t' + fields[1]+'\t' + serial + '\t' + fields[3]
        tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('BookPy.txt')
    os.rename('TempBook.txt' , 'BookPy.txt')
    if found:
        print('...Book Updated Successfully...')
    else:
        print('...Book Not Found...')

def deleteBook():
    import os
    title = input('Enter The Title Book to Delete : ')
    file = open('BookPy.txt' , 'r')
    tempFile = open('TempBook.txt' , 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == title:
           found = True
        else:
            tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('BookPy.txt')
    os.rename('TempBook.txt' , 'BookPy.txt')
    if not found:
        print('...Book Not Found...')
    else:
        print('...Book Deleted Successfully...')

def writeReader():
    with open('ReaderPy.txt' , 'a') as file:
        c = 'y'
        while c == 'y':
            id = input('Enter The Reader ID : ')
            name = input('Enter The Reader Name : ')
            age = input('Enter The Reader Age : ')
            seat = input('Enter The Number Seat Of Reader : ')
            file.write(id+'\t'+name+'\t'+age+'\t'+seat+'\n')
            c = input('Do You Want To Add Record Again..??(y / n)')
        print('...File Saved Successfully...')

def readReader():
    with open('ReaderPy.txt' , 'r') as file:
        print('ID\tName\tAge\tSeat')
        print('------------------------------------')
        for line in file:
            print(line , end = '')

def searchReader():
    id = input('Enter The ID of Reader To Search : ')
    with open('ReaderPy.txt' , 'r') as file:
        found = False
        for line in file:
            fields = line.split('\t')
            if fields[0] == id:
                found = True
                print('ID\tName\tAge\tSeat')
                print('-------------------------------')
                print(line)
        if not found:
            print('...Reader Not Found...')

def updateReader():
    import os
    id = input('Enter The ID of Reader To Update : ')
    file = open('ReaderPy.txt' , 'r')
    tempFile = open('TempReader.txt' ,'w')
    found =False
    for line in file:
        fields = line.split('\t')
        if fields[0] == id:
            found = True
            seat = input('Enter The New Seat Number for This Reader : ')
            line = fields[0]+'\t'+fields[1]+'\t'+fields[2]+seat
        tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('ReaderPy.txt')
    os.rename('TempReader.txt' , 'ReaderPy.txt')
    if found:
        print('...File Updated Successfully...')
    else:
        print('...Reader Not Found...')

def deleteReader():
    import os
    id = input('Enter The ID of Reader To Delete : ')
    file = open('ReaderPy.txt' , 'r')
    tempFile = open('TempReader.txt' , 'w')
    found = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == id:
            found = True
        else:
            tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('ReaderPy.txt')
    os.rename('TempReader.txt' , 'ReaderPy.txt')
    if not found:
        print('...Reader Not Found...')
    else:
        print('...Reader Deleted Successfully...')

def home():
    c = 'y'
    while c == 'y':
        print('1: To Write Book...')
        print('2: To Read Book...')
        print('3: To Search Book...')
        print('4: To Update Book...')
        print('5: To Delete Book...')
        print('6: To Read Reader...')
        print('7: To Write Reader...')
        print('8: To Search Reader...')
        print('9: To Update Reader...')
        print('10: To Delete Reader...')
        c = input('Your Choise : ')
        if c == '1':
            writeBook()
        elif c == '2':
            readBook()
        elif c == '3':
            searchBook()
        elif c == '4':
            updateBook()
        elif c == '5':
            deleteBook()
        elif c == '6':
            writeReader()
        elif c == '7':
            readReader()
        elif c == '8':
            searchReader()
        elif c == '9':
            updateReader()
        elif c == '10':
            deleteReader()
        c = input('Perform Another Operation (y/n): ')
home()
        
            
        
         
            
            
    
    
    
    
        
            
    
    
    
        
            
    
    
   
        
    
    
    
    
        
    
            
    


    
    
        
   
        
