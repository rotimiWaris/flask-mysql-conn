from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'nasecretlol'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # MySQL username
    'password': 'admin',  # MySQL password
    'database': 'Mapoly'
}

def get_db_connection():
    """Create and return a MySQL database connection."""
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    dob = request.form['dob']
    gender = request.form['gender']
    email = request.form['email']
    department = request.form['department']
    phone = request.form['phoneNumber']
    course_title = request.form['courseTitle']

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert data into the Student table
        cursor.execute('''
            INSERT INTO Student (FirstName, LastName, DateOfBirth, Gender, Email, Department, PhoneNumber, CourseTitle)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (first_name, last_name, dob, gender, email, department, phone, course_title))

        # Commit changes
        conn.commit()
        flash('Data saved successfully!', 'success')
    except mysql.connector.Error as err:
        flash(f'Error: {err}', 'error')
    finally:
        # Close the connection
        cursor.close()
        conn.close()

    return redirect(url_for('index'))

@app.route('/students')
def students():
    """Query and display all students."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Student')
    students = cursor.fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/customer_form')
def customer_form():
    return render_template('customer_form.html')

@app.route('/submit_customer', methods=['POST'])
def submit_customer():
    # Get form data
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    email = request.form['email']
    phone_number = request.form['phoneNumber']
    address = request.form['address']
    password = request.form['password']

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert data into the Customer table
        cursor.execute('''
            INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Password)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (first_name, last_name, email, phone_number, address, password))

        # Commit changes
        conn.commit()
        flash('Customer data saved successfully!', 'success')
    except mysql.connector.Error as err:
        flash(f'Error: {err}', 'error')
    finally:
        # Close the connection
        cursor.close()
        conn.close()

    return redirect(url_for('customer_form'))

@app.route('/product_form')
def product_form():
    return render_template('product_form.html')

@app.route('/submit_product', methods=['POST'])
def submit_product():
    # Get form data
    product_name = request.form['productName']
    description = request.form['description']
    price = request.form['price']
    category_id = request.form['categoryID']
    
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert data into the Product table
        cursor.execute('''
            INSERT INTO Product (ProductName, Description, Price, CategoryID)
            VALUES (%s, %s, %s, %s)
        ''', (product_name, description, price, category_id))

        # Commit changes
        conn.commit()
        flash('Product data saved successfully!', 'success')
    except mysql.connector.Error as err:
        flash(f'Error: {err}', 'error')
    finally:
        # Close the connection
        cursor.close()
        conn.close()

    return redirect(url_for('product_form'))

@app.route('/category_form')
def category_form():
    return render_template('category_form.html')

@app.route('/submit_category', methods=['POST'])
def submit_category():
    # Get form data
    category_name = request.form['categoryName']
    description = request.form['description']

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert data into the Category table
        cursor.execute('''
            INSERT INTO Category (CategoryName, Description)
            VALUES (%s, %s)
        ''', (category_name, description))

        # Commit changes
        conn.commit()
        flash('Category data saved successfully!', 'success')
    except mysql.connector.Error as err:
        flash(f'Error: {err}', 'error')
    finally:
        # Close the connection
        cursor.close()
        conn.close()

    return redirect(url_for('category_form'))

if __name__ == '__main__':
    app.run(debug=True)