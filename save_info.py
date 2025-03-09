import tkinter as tk
from tkinter import messagebox
import mysql.connector

def save_data():
    # Get data from the form
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    gender = entry_gender.get()
    email = entry_email.get()
    department = entry_department.get()
    phone_number = entry_phone_number.get()
    course_title = entry_course_title.get()

    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="admin",  # Replace with your MySQL password
        database="Mapoly"
    )
    cursor = conn.cursor()

    try:
        # Insert data into the Student table
        cursor.execute('''
            INSERT INTO Student (FirstName, LastName, DateOfBirth, Gender, Email, Department, PhoneNumber, CourseTitle)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (first_name, last_name, dob, gender, email, department, phone_number, course_title))

        # Commit changes
        conn.commit()
        messagebox.showinfo("Success", "Data saved successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")

# Create form fields
tk.Label(root, text="First Name:").grid(row=0, column=0)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

tk.Label(root, text="Date of Birth (YYYY-MM-DD):").grid(row=2, column=0)
entry_dob = tk.Entry(root)
entry_dob.grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=3, column=1)

tk.Label(root, text="Email:").grid(row=4, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1)

tk.Label(root, text="Department:").grid(row=5, column=0)
entry_department = tk.Entry(root)
entry_department.grid(row=5, column=1)

tk.Label(root, text="Phone Number:").grid(row=6, column=0)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=6, column=1)

tk.Label(root, text="Course Title:").grid(row=7, column=0)
entry_course_title = tk.Entry(root)
entry_course_title.grid(row=7, column=1)

# Create a submit button
tk.Button(root, text="Submit", command=save_data).grid(row=8, column=0, columnspan=2)

# Run the application
root.mainloop()