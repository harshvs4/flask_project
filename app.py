from flask import Flask, render_template, request, redirect

import mysql.connector

app = Flask(__name__)
 
# Configure MySQL database

DATABASE = 'books'
 
def create_table():
    #conn = sqlite3.connect(DATABASE)
    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='harshsharma', database=DATABASE,auth_plugin='mysql_native_password')   
    mycursor = conn.cursor()

 

 

 

    mycursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTO_INCREMENT, title VARCHAR(50))')

 

 

 

    conn.commit()

 

 

 

    conn.close()

 

@app.route('/')

 

 

 

def index():

 

 

 

    create_table()

 

 

 

    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='harshsharma', database=DATABASE,auth_plugin='mysql_native_password')


 

 

    mycursor = conn.cursor()

 

 

 

    mycursor.execute('SELECT * FROM books')

 

 

 

    books = mycursor.fetchall()

 

 

 

    conn.close()

 

 

 

    return render_template('index.html', books=books)

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

@app.route('/add_book', methods=['POST'])

 

 

 

def add_book():

 

 

 

    title = request.form.get('title')

 

 

 

    if title:

 

 

 

        conn = mysql.connector.connect(host='127.0.0.1', user='root', password='harshsharma', database=DATABASE,auth_plugin='mysql_native_password')

 

 

 

        mycursor = conn.cursor()

 

 

 

        insert_statement = 'INSERT INTO books (title) VALUES (%s)'

 

 

 

        mycursor.execute(insert_statement, (title,))

 

 

 

        conn.commit()

 

 

 

        conn.close()

 

 

 

    return redirect('/')

 

 

 

 

 

 

 

    # Comment after having done an initial commit and push

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

@app.route('/delete_book/<int:id>')

 

 

 

def delete_book(id):

 

 

 

    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='harshsharma', database=DATABASE,auth_plugin='mysql_native_password')

 

 

 

    mycursor = conn.cursor()

 

 

 

    delete_statement = 'DELETE FROM books WHERE id = %s'

 

 

 

    mycursor.execute(delete_statement, (id,))

 

 

 

    conn.commit()

 

 

 

    conn.close()

 

 

 

    return redirect('/')

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

@app.route('/update_book/<int:id>', methods=['GET', 'POST'])

 

 

 

def update_book(id):

 

 

 

    conn = mysql.connector.connect(host='127.0.0.1', user='root', password='harshsharma', database=DATABASE,auth_plugin='mysql_native_password')

 

 

 

    mycursor = conn.cursor()

 

 

 

    if request.method == 'POST':

 

 

 

        new_title = request.form.get('new_title')

 

 

 

        if new_title:

 

 

 

            update_statement = 'UPDATE books SET title = %s WHERE id = %s'

 

 

 

            mycursor.execute(update_statement, (new_title, id))

 

 

 

            conn.commit()

 

 

 

            return redirect('/')

 

 

 

    select_statement = 'SELECT * FROM books WHERE id = %s'

 

 

 

    mycursor.execute(select_statement, (id,))

 

 

 

    book = mycursor.fetchone()

 

 

 

    conn.close()

 

 

 

    return render_template('update_book.html', book=book)

 

 

 

 

 

if __name__ == '__main__':

 

 

 

    app.run(port=5003,debug=True)