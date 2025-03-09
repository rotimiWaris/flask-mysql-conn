import mysql.connector

def query_all_students():
    """Query all students in the database."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="admin",  # Replace with your MySQL password
        database="Mapoly"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Student')
    students = cursor.fetchall()
    conn.close()
    return students

def query_students_by_department(department):
    """Query students by department."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="admin",  # Replace with your MySQL password
        database="Mapoly"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Student WHERE Department = %s', (department,))
    students = cursor.fetchall()
    conn.close()
    return students

def query_student_by_email(email):
    """Query a student by email."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="admin",  # Replace with your MySQL password
        database="Mapoly"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Student WHERE Email = %s', (email,))
    student = cursor.fetchone()
    conn.close()
    return student

def query_students_with_birth_year(year):
    """Query students born in a specific year."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="admin",  # Replace with your MySQL password
        database="Mapoly"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Student WHERE YEAR(DateOfBirth) = %s', (year,))
    students = cursor.fetchall()
    conn.close()
    return students

# Example usage
if __name__ == '__main__':
    print("All Students:")
    print(query_all_students())

    print("\nStudents in Computer Science:")
    print(query_students_by_department('Computer Science'))

    print("\nStudent with email 'john.doe@example.com':")
    print(query_student_by_email('john.doe@example.com'))

    print("\nStudents born in 2000:")
    print(query_students_with_birth_year(2000))