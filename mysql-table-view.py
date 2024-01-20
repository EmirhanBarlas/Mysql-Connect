import tkinter as tk
import mysql.connector
def show_tables():
    # Get user input for database credentials
    host = host_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the MySQL database
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )
        cursor = connection.cursor()

        # Get the list of tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Create a new window to display the tables
        table_window = tk.Toplevel(root)
        table_window.title("Tables in the database")

        # Create a label for each table
        for table in tables:
            table_label = tk.Label(table_window, text=table[0])
            table_label.pack()

        # Close the database connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        error_label.config(text="Error connecting to the database: " + str(error))

# Create the main window
root = tk.Tk()
root.title("MySQL Table Viewer")

# Create input fields for database credentials
host_label = tk.Label(root, text="Host IP address:")
host_label.pack()
host_entry = tk.Entry(root)
host_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to show the tables
show_tables_button = tk.Button(root, text="Show Tables", command=show_tables)
show_tables_button.pack()

# Create a label for displaying errors
error_label = tk.Label(root, fg="red")
error_label.pack()

# Start the main event loop
root.mainloop()
