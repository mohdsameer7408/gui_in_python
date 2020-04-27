from tkinter import *
import sqlite3

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')
root.geometry('400x400')

# database

# create table
"""
cursor.execute('''CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zip_code integer 
    )
''')
"""

# submit method for database


def submit():
    # create database or connect to an existing one
    connect = sqlite3.connect('address_book.db')

    # create cursor
    cursor = connect.cursor()

    # insert into table
    cursor.execute('INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zip_code)',
                   {
                       'first_name': first_name.get(),
                       'last_name': last_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zip_code': zip_code.get()
                   }
                   )

    # commit changes
    connect.commit()

    # close connection
    connect.close()

    # clear text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)

# query method


def query():
    # create database or connect to an existing one
    connect = sqlite3.connect('address_book.db')

    # create cursor
    cursor = connect.cursor()

    # query database
    cursor.execute('SELECT oid, * FROM addresses')
    records = cursor.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    connect.commit()

    # close connection
    connect.close()


# create a method to delete a record
def delete():
    # create database or connect to an existing one
    connect = sqlite3.connect('address_book.db')

    # create cursor
    cursor = connect.cursor()

    # delete a record
    cursor.execute('DELETE FROM addresses WHERE oid = ' + delete_box.get())

    # commit changes
    connect.commit()

    # close connection
    connect.close()


# method to save the edited data
def update():
    # create database or connect to an existing one
    connect = sqlite3.connect('address_book.db')

    # create cursor
    cursor = connect.cursor()

    record_id = delete_box.get()
    delete_box.delete(0, END)

    # query database
    cursor.execute('''UPDATE addresses SET 
    first_name = :first,
    last_name = :last,
    address = :add,
    city = :city,
    state = :state,
    zip_code = :zip_code
    
    WHERE oid = :oid
    ''',
                   {
                       'first': first_name_editor.get(),
                       'last': last_name_editor.get(),
                       'add': address_editor.get(),
                       'city': city_editor.get(),
                       'state': state_editor.get(),
                       'zip_code': zip_code_editor.get(),
                       'oid': record_id
                   })

    # commit changes
    connect.commit()

    # close connection
    connect.close()

    editor.destroy()


# create a edit method
def edit():
    global editor
    editor = Tk()
    editor.title("Static")
    editor.iconbitmap('images/logos/my-ic.ico')
    editor.geometry('350x250')

    # create database or connect to an existing one
    connect = sqlite3.connect('address_book.db')

    # create cursor
    cursor = connect.cursor()

    record_id = delete_box.get()
    # query database
    cursor.execute('SELECT * FROM addresses WHERE oid = ' + record_id)
    records = cursor.fetchall()

    # create global variables for text box names
    global first_name_editor, last_name_editor, address_editor, city_editor, state_editor, zip_code_editor
    # create text boxes
    first_name_editor = Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zip_code_editor = Entry(editor, width=30)
    zip_code_editor.grid(row=5, column=1, padx=20)

    # looping through results
    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_code_editor.insert(0, record[5])

    # text box labels
    first_name_label_editor = Label(editor, text='First Name')
    first_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    last_name_label_editor = Label(editor, text='Last Name')
    last_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text='Address')
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text='City')
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text='State')
    state_label_editor.grid(row=4, column=0)

    zip_code_label_editor = Label(editor, text='Zip Code')
    zip_code_label_editor.grid(row=5, column=0)

    # create a save button
    save_button = Button(editor, text='Save Record', command=update)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

    # commit changes
    connect.commit()

    # close connection
    connect.close()


# create text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zip_code = Entry(root, width=30)
zip_code.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# text box labels
first_name_label = Label(root, text='First Name')
first_name_label.grid(row=0, column=0, pady=(10, 0))

last_name_label = Label(root, text='Last Name')
last_name_label.grid(row=1, column=0)

address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)

city_label = Label(root, text='City')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State')
state_label.grid(row=4, column=0)

zip_code_label = Label(root, text='Zip Code')
zip_code_label.grid(row=5, column=0)

delete_box_label = Label(root, text='Select ID')
delete_box_label.grid(row=9, column=0, pady=5)

# a submit button
submit_button = Button(root, text='Add Record To Database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Query button
query_button = Button(root, text='Show Records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button
delete_button = Button(root, text='Delete a Record', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# create a update button
update_button = Button(root, text='Update a Record', command=edit)
update_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)


root.mainloop()
