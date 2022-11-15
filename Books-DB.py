import sqlite3

# Establish connection with DB and create cursor.
con = sqlite3.connect('DB-Books')
c = con.cursor()


# Function to create a table if it doesn't exist.
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Books (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
              'Title TEXT (100),'
              'Author TEXT (100),'
              'Language TEXT (100),'
              'Read TEXT(100))')


# Function for inserting new books into the table by inputting information.
def insert():
    title = input('Book title: ')
    author = input('Book author: ')
    language = input('Book language: ')
    read = input('Book read: ')
    c.execute(
        'INSERT INTO Books (Title, Author, Language, Read) VALUES (?,?,?,?)', (title, author, language, read))
    con.commit()
    print('\nBook inserted!')


# Function for inserting new books directly.
def insert_direct(title, author, language, read):
    c.execute(
        'INSERT INTO Books (Title, Author, Language, Read) VALUES (?,?,?,?)', (title, author, language, read))
    con.commit()


# Function for selecting all data from the table.
def select_all():
    c.execute('SELECT * FROM Books')
    print('\nHere is all the data from this table.\n')
    for line in c.fetchall():
        print(line)


# Function for selecting all read books.
def select_read():
    c.execute('SELECT * FROM Books WHERE Read = "yes"')
    print('\n Here are all the books you have read.\n')
    for line in c.fetchall():
        print(line)


# Function for selecting all unread books.
def select_unread():
    c.execute('SELECT * FROM Books WHERE Read == "no"')
    print('\nHere are all the books you haven not read.\n')
    for line in c.fetchall():
        print(line)


# Function for selecting a specific column by inputting the column's index.
def select_column():
    option = int(input('\nSelect column: Title(1), Author(2), Language(3)'))
    column = ''
    if option == 1:
        column = 'Title'
        c.execute(f'SELECT DISTINCT {column} FROM Books')
    elif option == 2:
        column = 'Author'
        c.execute(f'SELECT DISTINCT {column} FROM Books')
    elif option == 3:
        column = 'Language'
        c.execute(f'SELECT DISTINCT {column} FROM Books')
    print(f'\nHere are all the book {column}s in this database.\n')
    for line in c.fetchall():
        print(line)


# Function for updating the "Read" status on a book from "no" to "yes" based on Title or ID.
def update_read():
    option = input('\nChoose book by Title(1) or ID(2)?')
    if option == '1':
        book = input('\nWhat book did you read? ')
        c.execute(f'UPDATE Books SET Read = "yes" WHERE Title = "{book}"')
    elif option == '2':
        book = input('\nWhat the ID of the book you read? ')
        c.execute(f'UPDATE Books SET Read = "yes" WHERE ID = "{book}"')
    con.commit()
    print('\nBook "read" status updated!')


# Calling all functions for testing.
create_table()

insert_direct('The Bitcoin Standard', 'Saifedean Ammous', 'Portuguese', 'no')

insert()

select_all()

select_read()

select_unread()

select_column()

update_read()

# Closing connection with DB.
con.commit()
c.close()
con.close()
