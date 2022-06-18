from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()

root.config(bg='grey')
root.title("Facebook Database")
root.iconbitmap("facebook.ico")
root.maxsize(width=505, height=500)


conn = sqlite3.connect("facebook.db")
c = conn.cursor()

# c.execute('''CREATE TABLE user(
#     first_name text,
#     last_name text,
#     address text,
#     age integer,
#     password text,
#     fathername text,
#     city text,
#     zip_code integer
#     )''')
# print("Table created")


def subm():
    conn = sqlite3.connect("facebook.db")
    c = conn.cursor()

    c.execute("INSERT INTO user VALUES(:f_name, :l_name, :address, :age , :password, :fathername, :city, :zip_code)", {
        "f_name": f_name.get(),
        "l_name": l_name.get(),
        "address": address.get(),
        "age": age.get(),
        "password": password.get(),
        "fathername": fathername.get(),
        "city": city.get(),
        "zip_code": zip_code.get()
    })
    messagebox.showinfo("Users", "Added Sucessfully")
    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    age.delete(0, END)
    password.delete(0, END)
    fathername.delete(0, END)
    city.delete(0, END)
    zip_code.delete(0, END)


def query():
    conn = sqlite3.connect("facebook.db")
    c = conn.cursor()

    c.execute("SELECT *, oid from user")

    records = c.fetchall()
    print(records)

    print_record = ""
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + ' ' + str(record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + ' ' + str(record[7]) \
            + '\t' + str(record[8]) + '\n '

    query_label = Label(root, text=print_record)
    query_label.grid(row=11, column=0, columnspan=2)
    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect("facebook.db")
    c = conn.cursor()
    c.execute("DELETE from user WHERE oid =" + delete_box.get())
    messagebox.showinfo('User', "Deleted Sucessfully")
    delete_box.delete(0, END)
    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect("facebook.db")
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE user SET
    first_name= :first,
    last_name=:last,
    address=:address,
    age=:age,
    password=:password,
    fathername=:fathername,
    city=:city,
    zip_code=:zip_code
    WHERE oid=oid""",
              {'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'age': age_editor.get(),
               'password': password_editor.get(),
               'fathername': fathername_editor.get(),
               'city': city_editor.get(),
               'zip_code': zipcode_editor.get()

               }
              )
    messagebox.showinfo('User', "Updated Sucessfully")
    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor = Toplevel()
    editor.title("Update Data")
    editor.geometry('300x400')
    conn = sqlite3.connect("facebook.db")
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM user WHERE oid=" + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global fathername_editor
    global city_editor
    global zipcode_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=1, column=2)

    f_editor_label = Label(editor, text="First Name")
    f_editor_label.grid(row=1, column=1)

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=2, column=2)

    l_editor_label = Label(editor, text="Last Name")
    l_editor_label.grid(row=2, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=2)

    a_editor_label = Label(editor, text="Address")
    a_editor_label.grid(row=3, column=1)

    age_editor = Entry(editor, width=30)
    age_editor.grid(row=4, column=2)

    ag_editor_label = Label(editor, text="Age")
    ag_editor_label.grid(row=4, column=1)

    password_editor = Entry(editor, width=30, show='*')
    password_editor.grid(row=5, column=2)

    p_editor_label = Label(editor, text="Password")
    p_editor_label.grid(row=5, column=1)

    fathername_editor = Entry(editor, width=30)
    fathername_editor.grid(row=6, column=2)

    fa_editor_label = Label(editor, text="Fathername")
    fa_editor_label.grid(row=6, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=7, column=2)

    c_editor_label = Label(editor, text="City")
    c_editor_label.grid(row=7, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=8, column=2)

    z_editor_label = Label(editor, text="Zip_code")
    z_editor_label.grid(row=8, column=1)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        age_editor.insert(0, record[3])
        password_editor.insert(0, record[4])
        fathername_editor.insert(0, record[5])
        city_editor.insert(0, record[6])
        zipcode_editor.insert(0, record[7])

    save_btn = Button(editor, text="Save", command=update)
    save_btn.grid(row=10, column=1, columnspan=2, pady=10, padx=10, ipadx=100)


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

age = Entry(root, width=30)
age.grid(row=3, column=1)

password = Entry(root, width=30, show='*')
password.grid(row=4, column=1)

fathername = Entry(root, width=30)
fathername.grid(row=5, column=1)

city = Entry(root, width=30)
city.grid(row=6, column=1)

zip_code = Entry(root, width=30)
zip_code.grid(row=7, column=1)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

age_label = Label(root, text="Age")
age_label.grid(row=3, column=0)

password_label = Label(root, text="Password")
password_label.grid(row=4, column=0)

fathername_label = Label(root, text="Fathername")
fathername_label.grid(row=5, column=0)

city_label = Label(root, text="City")
city_label.grid(row=6, column=0)

zip_code_label = Label(root, text="Zipcode")
zip_code_label.grid(row=7, column=0)

delete_box = Entry(root, width=30)
delete_box.grid(row=15, column=1, pady=5)

delete_id = Label(root, text="Existing ID")
delete_id.grid(row=15, column=0, pady=5)

add_btn = Button(root, text="Add Records", command=subm)
add_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=16, column=0, columnspan=3, pady=10, padx=10, ipadx=120)

update_btn = Button(root, text="Update", command=edit)
update_btn.grid(row=17, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


conn.commit()
conn.close()
root.mainloop()
