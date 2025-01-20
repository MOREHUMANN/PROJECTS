import mysql.connector
import random
x=0
def connector():
     connection = mysql.connector.connect(
         host="localhost",         # Replace with your MySQL host
         user="root",              # Replace with your MySQL username
         password="", # Replace with your MySQL password
         database="master_db"      # Replace with your database name
         )
     cursor = connection.cursor()
     return connection

def SETUP():
    # Step 1: Connect to MySQL Server
    connection = mysql.connector.connect(
        host="localhost",user="root",password="")

    cursor = connection.cursor()

    # Step 2: Create the Master Database
    cursor.execute("CREATE DATABASE IF NOT EXISTS master_db")
    print("Database 'master_db' created successfully!")

    # Use the master database
    cursor.execute("USE master_db")

    # Step 3: Create Tables

    # 1. Employee Data Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EmployeeData (
        EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(100),
        Designation VARCHAR(50),
        Department VARCHAR(50),
        Salary DECIMAL(10, 2),
        Address VARCHAR(255),
        DateOfBirth DATE,
        HireDate DATE,
        ContactNumber VARCHAR(15),
        Email VARCHAR(100),
        Status VARCHAR(20),
        CompanyName VARCHAR(100) ,
        CompanyID VARCHAR(500)
    );
    ''')
    print("Table 'EmployeeData' created successfully!")

    # 2. Business Data Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BusinessData (
        BusinessID INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(100),
        Type VARCHAR(50),
        EstablishedYear INT,
        Location VARCHAR(100),
        Revenue DECIMAL(15, 2),
        OwnerName VARCHAR(100),
        ContactNumber VARCHAR(15),
        Email VARCHAR(100),
        Website VARCHAR(100)
    );
    ''')
    print("Table 'BusinessData' created successfully!")

    # 3. Passwords Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Passwords (
        PasswordID INT PRIMARY KEY AUTO_INCREMENT,
        Username VARCHAR(50),
        Password VARCHAR(100)
    );
    ''')
    print("Table 'Passwords' created successfully!")
   

    def add_new_user():
       # Step 1: Connect to the database
         connection =  connector()
        
         cursor = connection.cursor()
        
        # Step 2: Get the new user's password
         print("CREATING NEW ADMIN")
         username = "admin"  # Default username
         
         response=input("do you want to auto generate your password y/n:")
         if response == "y":
           password=passwdgen()
         else:
           password =input("enter your password:")

         # Step 3: Insert the new user into the Passwords table
         insert_query = "INSERT INTO Passwords (Username, Password) VALUES (%s, %s)"
         cursor.execute(insert_query, (username, password))
         connection.commit()

         print("nNew user added successfully!")
         print('Username:', username)
         print('Password:',password)

         # Step 4: Close the connection
         connection.close()

         # Call the function to add a new user

    add_new_user()


    
    
    
    
    
    

    # 4. Balance Sheet Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BalanceSheet (
        RecordID INT PRIMARY KEY AUTO_INCREMENT,
        AccountName VARCHAR(100),
        Credit DECIMAL(15, 2),
        Debit DECIMAL(15, 2),
        Balance DECIMAL(15, 2),
        Quarter INT,
        Year INT
    );
    ''')
    print("Table 'BalanceSheet' created successfully")

    # Step 4: Close the Connection
    connection.close()
    print("setup completed")


def registration():
    connection =  connector()
        
    cursor = connection.cursor()
    def bussinessdata():
        print("nPlease provide the following details for the business:")

        name = input("Business Name: ")
        type_ = input("Business Type: ")
        established_year = input("Established Year: ")
        location = input("Business Location: ")
        revenue = input("Annual Revenue (e.g., 500000.00): ")
        owner_name = input("Owner's Name: ")
        contact_number = input("Contact Number: ")
        email = input("Email Address: ")
        website = input("Business Website URL: ")

        return (name, type_, established_year, location, revenue, owner_name, contact_number, email, website)
    data=bussinessdata()
    # Function to insert data into the database
    def insert_business_data(data):
        cursor.execute('''
        INSERT INTO BusinessData (Name, Type, EstablishedYear, Location, Revenue, OwnerName, ContactNumber, Email, Website)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', data)
        print("nBusiness data has been saved successfully.")
    insert_business_data(data)
    
    
    username = input("Enter your username: ").strip()
     
    response=input("do you want to auto generate your password y/n:")
    if response == "y":
           password=passwdgen()
    else:
           password =input("enter your password:")

        # Insert the user credentials into the Passwords table
    query2 = "INSERT INTO Passwords (Username, Password) VALUES (%s, %s)"
    cursor.execute(query2, (username, password))
    connection.commit()

    print("User credentials have been successfully added.")                              
    cursor.close()
    connection.close()
    BUSINESS()
    
    
def AVEMPLOYEE():
    
    connection =  connector()
        
    cursor = connection.cursor()
    # Function to display all employee data
    def display_all_employees():
        cursor.execute("SELECT * FROM EmployeeData")
        rows = cursor.fetchall()
        if rows:
            print("nEmployee Data:")
            for row in rows:
                print(f"Employee ID: {row[0]}, Name: {row[1]}, Designation: {row[2]}, Department: {row[3]}, Salary: {row[4]}, Company: {row[10]}")
        else:
            print("nNo employee data found.")
            connection.close()
            AVIEW()
    # Function to get employee data by Company Name and Employee ID
    def get_employee_by_company_and_id(employee_id):
        cursor.execute("SELECT * FROM EmployeeData WHERE  EmployeeID = %s", (employee_id))
        row = cursor.fetchone()
        if row:
            print(f"nEmployee Data for {company_name} (Employee ID: {employee_id}):")
            print(f"Employee ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Designation: {row[2]}")
            print(f"Department: {row[3]}")
            print(f"Salary: {row[4]}")
            print(f"Contact Number: {row[6]}")
            print(f"Email: {row[7]}")
        else:
            print("nNo data found for the given Company Name and Employee ID.")
            connection.close()
            AVIEW()
    # Main program loop
    def Employeemain():
        while True:
            print("n1. View All Employees")
            print("2. View Specific Employee by Company Name and Employee ID")
            print("3. Exit")

            choice = input("nEnter your choice (1/2/3): ")

            if choice == '1':
                display_all_employees()
            elif choice == '2':
                employee_id = int(input("Enter Employee ID: "))
                get_employee_by_company_and_id(employee_id)
            else:
                print("Exiting program.")
              
                AVIEW()
            

    Employeemain()

    connection.close()
    print("---------THANK-YOU---------")

def ABDELETE():
    connection =  connector()
        
    cursor = connection.cursor()
    # Function to delete employees of a specific business
    def delete_employees_of_business(company_name):
        cursor.execute("DELETE FROM EmployeeData WHERE CompanyName = %s", (company_name,))
        connection.commit()
        print(f"nAll employees from {company_name} have been removed.")

    # Function to delete the business from the BusinessData table
    def delete_business(company_id, company_name):
        cursor.execute("DELETE FROM BusinessData WHERE BusinessID = %s AND Name = %s", (company_id, company_name))
        connection.commit()
        print(f"nBusiness '{company_name}' with ID {company_id} has been deleted.")

    # Main program loop
    def deletemain():
        print("Welcome to the Business and Employee Deletion System")

        business_id = int(input("nEnter the Business ID of the business you want to delete: "))
        company_name = input("Enter the Name of the business you want to delete: ")

        confirm = input(f"Are you sure you want to delete the business {company_name} with ID {business_id}? (y/n): ")

        if confirm.lower() == 'y':
            delete_employees_of_business(company_name)
            delete_business(business_id, company_name)
            print("nThe business and associated employees have been deleted successfully.")
            connection.close()
            AEDIT()
        else:
            print("nDeletion aborted.")
            connection.close()
            AEDIT()

    deletemain()

    connection.close()

def AVBUSINESS():
    connection =  connector()
        
    cursor = connection.cursor()
    # Function to display all business data
    def view_all_businesses():
        cursor.execute("SELECT * FROM BusinessData")
        rows = cursor.fetchall()
        if rows:
            print("nAll Business Details:")
            print("-" * 250)
            for row in rows:
               print(
    f"Business ID: {row[0]} \n"
    f"Name: {row[1]} \n"
    f"Type: {row[2]} \n"
    f"Established Year: {row[3]} \n"
    f"Location: {row[4]} \n"
    f"Revenue: {row[5]} \n"
    f"Owner: {row[6]} \n"
    f"Contact: {row[7]} \n"
    f"Email: {row[8]} \n"
    f"Website: {row[9]}"
)

             print("-" * 250)
             
        else:
            print("nNo businesses found in the database.")

     # Function to display a single business by BusinessID
    def view_single_business(business_id):
        cursor.execute("SELECT * FROM BusinessData WHERE BusinessID = %s", (business_id,))
        row = cursor.fetchone()
        if row:
           print("nBusiness Details:")
           print(f"Business ID: {row[0]}")
           print(f"Name: {row[1]}")
           print(f"Type: {row[2]}")
           print(f"Established Year: {row[3]}")
           print(f"Location: {row[4]}")
           print(f"Revenue: {row[5]}")
           print(f"Owner: {row[6]}")
           print(f"Contact: {row[7]}")
           print(f"Email: {row[8]}")
           print(f"Website: {row[9]}")
        else:
           print(f"nNo business found with Business ID {business_id}.")

      # Main function to interact with the user
    def bviewmain():
        while True:
             print("n--- Business Details Viewer ---")
             print("1. View All Businesses")
             print("2. View a Single Business by Business ID")
             print("3. Exit")
        
             choice = input("nEnter your choice (1/2/3): ")
        
             if choice == '1':
                view_all_businesses()
                connection.close()
                AVIEW()
             elif choice == '2':
               try:
                  business_id = int(input("nEnter the Business ID: "))
                  view_single_business(business_id)
                  connection.close()
                  AVBUSINESS()
               except ValueError:
                  print("nPlease enter a valid numeric Business ID.")
                  AVBUSINESS()
             else :
                print("nExiting program. THANK YOU!")
                AVIEW()
             

     # Run the main function
     
    bviewmain()

     # Close the database connection
    connection.close()

    
def AVBALANCESHEET():
    connection =  connector()
        
    cursor = connection.cursor()
    # Function to view all balance sheet records
    def view_all_balance_sheet():
        cursor.execute("SELECT * FROM BalanceSheet")
        rows = cursor.fetchall()
        if rows:
            print("nAll Balance Sheet Records:")
            print("-" * 80)
            for row in rows:
               print(f"Record ID: {row[0]}, \n Account Name: {row[1]},\n Credit: {row[2]},\n Debit: {row[3]},\n Balance: {row[4]}")
            print("-" * 80)
        else:
            print("nNo records found in the balance sheet.")

     # Function to view a single record by RecordID
    def view_single_balance_record(record_id):
       cursor.execute("SELECT * FROM BalanceSheet WHERE RecordID = %s", (record_id,))
       row = cursor.fetchone()
       if row:
           print("nBalance Sheet Record Details:")
           print(f"Record ID: {row[0]}")
           print(f"Account Name: {row[1]}")
           print(f"Credit: {row[2]}")
           print(f"Debit: {row[3]}")
           print(f"Balance: {row[4]}")
       else:
           print(f"nNo record found for Record ID {record_id}.")

     # Main function for user interaction
    def bsheetviewmain():
      while True:
           print("--- Balance Sheet Viewer ---")
           print("1. View All Balance Sheet Records")
           print("2. View a Single Balance Sheet Record by Record ID")
           print("3. Exit")
        
           choice = input("nEnter your choice (1/2/3): ")
        
           if choice == '1':
               view_all_balance_sheet()
               connection.close()
               AVIEW()
           elif choice == '2':
              try:
                  record_id = int(input("nEnter the Record ID: "))
                  view_single_balance_record(record_id)
                  connection.close()
                  AVBALANCESHEET()
              except ValueError:
                  print("nPlease enter a valid numeric Record ID.")
                  connection.close()
                  AVIEW()
           else:
               print("nExiting program. Goodbye!")
               connection.close()
               AVIEW()
 
   # Run the main function

    bsheetviewmain()

   # Close the database connection
    connection.close()

def BEBUSINESS():
  
    connection =  connector()
        
    cursor = connection.cursor()
    def edit_business_details():
      print("n--- Edit Business Details ---")
    try:
        # Ask for Business ID
        business_id = int(input("Enter the Business ID to edit: "))
        
        # Check if the business exists
        cursor.execute("SELECT * FROM BusinessData WHERE BusinessID = %s", (business_id,))
        business = cursor.fetchone()
        
        if not business:
            print(f"nNo business found with Business ID {business_id}.")
            return
        
        # Display current business data
        print("nCurrent Business Details:")
        print(f"1. Name: {business[1]}")
        print(f"2. Type: {business[2]}")
        print(f"3. Established Year: {business[3]}")
        print(f"4. Location: {business[4]}")
        print(f"5. Revenue: {business[5]}")
        print(f"6. Owner Name: {business[6]}")
        print(f"7. Contact Number: {business[7]}")
        print(f"8. Email: {business[8]}")
        print(f"9. Website: {business[9]}")
        
        print("nEnter new values for the fields. Leave blank to keep the current value.n")
        
        # Input new values for each field
        name = input(f"New Name (current: {business[1]}): ").strip() or business[1]
        business_type = input(f"New Type (current: {business[2]}): ").strip() or business[2]
        established_year = input(f"New Established Year (current: {business[3]}): ").strip() or business[3]
        location = input(f"New Location (current: {business[4]}): ").strip() or business[4]
        revenue = input(f"New Revenue (current: {business[5]}): ").strip() or business[5]
        owner_name = input(f"New Owner Name (current: {business[6]}): ").strip() or business[6]
        contact_number = input(f"New Contact Number (current: {business[7]}): ").strip() or business[7]
        email = input(f"New Email (current: {business[8]}): ").strip() or business[8]
        website = input(f"New Website (current: {business[9]}): ").strip() or business[9]
        
        # Update the business record in the database
        update_query = '''
        UPDATE BusinessData
        SET Name = %s, Type = %s, EstablishedYear = %s, Location = %s, Revenue = %s,
            OwnerName = %s, ContactNumber = %s, Email = %s, Website = %s
        WHERE BusinessID = %s
        '''
        cursor.execute(update_query, (name, business_type, established_year, location, revenue,owner_name, contact_number, email, website, business_id))
        connecton.commit()
        
        print("nBusiness details updated successfully!")
    except ValueError:
        print("nInvalid input. Please enter the correct data format.")
        mybusiness_editor()
    except Exception as e:
        print(f"nAn error occurred: {e}")
        mybusiness_editor()

   # Main function
    def main34():
      while True:
        print("n--- Business Management System ---")
        print("1. Edit Business Details")
        print("2. Exit")
        
        choice = input("nEnter your choice (1/2): ")
        
        if choice == '1':
            edit_business_details()
            connection.close()
            BEDIT()
        else:
            print("nExiting program. Goodbye!")
            connection.close()
            BEDIT()
        

   # Run the main function
  
    main34()

   # Close the database connection
    connection.close()
def balancecreate():
    connection =  connector()
        
    cursor = connection.cursor()

    
    cursor.execute('''
    INSERT INTO BalanceSheet (AccountName, Credit, Debit, Balance, Quarter, Year)
    VALUES (NULL, NULL, NULL, NULL, NULL, NULL);
''')
    connection.commit()
    connection.close()

  
def BEEMPLOYEE():
   connection =  connector()
        
   cursor = connection.cursor()

    # Function to recruit a new employee
   def recruit_employee(company_id, company_name):
      print(f"n--- Recruiting a New Employee for {company_name} (ID:     {company_id}) ---")
      try:
        name = input("Enter Employee Name: ").strip()
        designation = input("Enter Designation: ").strip()
        department = input("Enter Department: ").strip()
        salary = float(input("Enter Salary: "))
        
        # Insert employee into EmployeeData table
        insert_query = '''
        INSERT INTO EmployeeData (Name, Designation, Department, Salary)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (name, designation, department, salary, company_id))
        connection.commit()
        
        print("nEmployee recruited successfully!")
      except ValueError:
        print("nInvalid input. Please ensure salary is a number.")
        connection.close()
        BEEMPLOYEE()
      except Exception as e:
        print(f"nAn error occurred: {e}")
        connection.close()
        BEEMPLOYEE()

# Function to terminate an employee
   def terminate_employee(company_id, company_name):
       print(f"n--- Terminating an Employee for {company_name} (ID: {company_id}) ---")
       try:
          emp_id = int(input("Enter Employee ID to terminate: "))
        
        # Check if the employee exists in the company
          cursor.execute("SELECT * FROM EmployeeData WHERE EmployeeID = %s ,(emp_id)"
        )
          employee = cursor.fetchone()
        
          if not employee:
            print(f"nNo employee found with ID {emp_id} in {company_name}.")
            BEEDIT()
        
          # Delete the employee record
          delete_query = "DELETE FROM EmployeeData WHERE EmployeeID = %s"
          cursor.execute(delete_query, (emp_id,))
          connecton.commit()
        
          print("nEmployee terminated successfully!")
       except ValueError:
          print("nInvalid input. Please ensure Employee ID is a number.")
          connection.close()
          BEEMPLOYEE()
       except Exception as e:
          connection.close()
          BEEMPLOYEE()

# Main function
   def main22():
      while True:
        print("n--- Company Employee Management ---")
        company_id = input("Enter Company ID: ").strip()
        company_name = input("Enter Company Name: ").strip()
        
        print("nChoose an action:")
        print("1. Recruit a New Employee")
        print("2. Terminate an Employee")
        print("3. Exit")
        
        choice = input("nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            recruit_employee(company_id, company_name)
            connection.close()
            BEBUSINESS()
        elif choice == '2':
            terminate_employee(company_id, company_name)
            connection.close()
            BEBUSINESS()
        elif choice == '3':
            print("nExiting program. Goodbye!")
            connection.close()
            BEDIT()
          
           
        else:
            print("nInvalid choice. Please try again.")
            connection.close()
            BEDIT()
  # Run the main function
  
   main22()

  # Close the database connection
   connection.close()

    
    
def BEBALANCESHEET():
    connection =  connector()
        
    cursor = connection.cursor()
    # Function to edit a balance sheet record
    def edit_balance_sheet():
       print("n--- Edit Balance Sheet Record ---")
       try:
          # Ask for Record ID
          record_id = int(input("Enter the Record ID to edit: "))
        
          # Check if the record exists
          cursor.execute("SELECT * FROM BalanceSheet WHERE RecordID = %s", (record_id,))
          record = cursor.fetchone()
        
          if not record:
            print(f"nNo record found with Record ID {record_id}.")
            BEDIT()
        
        # Display current record data
          print("nCurrent Balance Sheet Details:")
          print(f"1. Account Name: {record[1]}")
          print(f"2. Credit: {record[2]}")
          print(f"3. Debit: {record[3]}")
          print(f"4. Balance: {record[4]}")
        
          print("nEnter new values for the fields. Leave blank to keep the current value.n")
        
        # Input new values for each field
          account_name = input(f"New Account Name (current: {record[1]}): ").strip() or record[1]
          credit = input(f"New Credit (current: {record[2]}): ").strip() or record[2]
          debit = input(f"New Debit (current: {record[3]}): ").strip() or record[3]
          balance = input(f"New Balance (current: {record[4]}): ").strip() or record[4]
        
        # Update the balance sheet record in the database
          update_query = '''
          UPDATE BalanceSheet
          SET AccountName = %s, Credit = %s, Debit = %s, Balance = %s
          WHERE RecordID = %s
           '''
          cursor.execute(update_query, (account_name, credit, debit, balance, record_id))
          connection.commit()
        
          print("nBalance sheet record updated successfully!")
       except ValueError:
         print("nInvalid input. Please enter the correct data format.")
       except Exception as e:
         print(f"nAn error occurred: {e}")

# Main function
    def main76():
     while True:
        print("n--- Balance Sheet Management ---")
        print("1. Edit Balance Sheet Record")
        print("2. Exit")
        
        choice = input("nEnter your choice (1/2): ")
        
        if choice == '1':
            edit_balance_sheet()
            connection.close()
            BEBALANCESHEET()
        else :
            print("nExiting program. Goodbye!")  
          # Close the database connection
            connection.close()
            BEDIT()
        

   # Run the main function
  
    main76()
 
 
    
   
 


def BVBUSINESS():
    connection =  connector()
        
    cursor = connection.cursor()
    # Function to view specific business details
    def view_business_details():
        print("n--- View Business Details ---")
        try:
           # Ask for Business ID
           business_id = int(input("Enter the Business ID to view details: "))
        
           # Query to retrieve the business details
           cursor.execute("SELECT * FROM BusinessData WHERE BusinessID = %s", (business_id,))
           business = cursor.fetchone()
        
           if not business:
               print(f"nNo business found with Business ID {business_id}.")
               connection.close()
               BVIEW()
        
        # Display business details
           print("n--- Business Details ---")
           print(f"Business ID: {business[0]}")
           print(f"Name: {business[1]}")
           print(f"Type: {business[2]}")
           print(f"Established Year: {business[3]}")
           print(f"Location: {business[4]}")
           print(f"Revenue: {business[5]}")
           print(f"Owner Name: {business[6]}")
           print(f"Contact Number: {business[7]}")
           print(f"Email: {business[8]}")
           print(f"Website: {business[9]}")
        except ValueError:
           print("nInvalid input. Please enter a numeric Business ID.")
        except Exception as e:
           print(f"nAn error occurred: {e}")

    view_business_details()
        

   
    connection.close()
    BVIEW()

def BVBALANCESHEET():

    connection =  connector()
        
    cursor = connection.cursor()
    # Step 2: Get the RecordID from the user
    record_id = int(input("Enter the Record ID of the Balance Sheet you want   to retrieve: "))

    # Step 3: Query the database for the specific record
    query = "SELECT * FROM BalanceSheet WHERE RecordID = %s"
    cursor.execute(query, (record_id,))

    # Step 4: Fetch and display the record
    record = cursor.fetchone()

    if record:
       print("nBalance Sheet Record:")
       print(f"Record ID: {record[0]}")
       print(f"Account Name: {record[1]}")
       print(f"Credit: {record[2]}")
       print(f"Debit: {record[3]}")
       print(f"Balance: {record[4]}")
    else:
       print(f"No record found with Record ID: {record_id}")
       connection.close()
       BVIEW()
    # Step 5: Close the connection
    connection.close()
    BVIEW()
    
def BVEMPLOYEE():
 
    print("Welcome to the Enhanced Employee Viewer!")
    print("Select what you want to do:")
    print("1. View employees of a my company")
    print("2. View a specific employee by ID and company name")
    print("3. exit")
    choice = input("Enter the number corresponding to your choice (1-3): ")

   
    if choice == "1":
        view_employees_by_company()
    elif choice == "2":
        view_employee_by_id_and_company()
    elif choice == "3":
        BVIEW()
    else:
        print("nInvalid choice! Please restart the program and select a valid option.")
        BVIEW()
    

    def view_employees_by_company():
    # Get the company name from the user
       company_name = input("nEnter the company name: ")

    # Connect to the database and fetch employees by company name
       try:
          connection =  connector()
        
          cursor = connection.cursor()
          query = """
            SELECT EmployeeID, EmployeeName, Position, Salary 
            FROM EmployeeData 
            WHERE CompanyName = %s
            """
          cursor.execute(query, (company_name,))
          result = cursor.fetchall()

          if result:
             print(f"nEmployees of {company_name}:")
             for row in result:
                print(f"Employee ID: {row[0]},\n Name: {row[1]},\n Position: {row[2]},\n Salary: {row[3]}")
          else:
                print(f"nNo employees found for the company '{company_name}'.")
                connection.close()
                BVIEW()
       except:
            print("some error occured meet developer")
            connection.close()
            BVIEW()
       finally:
            connection.close()
            BVIEW()

    def view_employee_by_id_and_company():
    # Get the employee ID and company name from the user
        company_name = input("nEnter the company name: ")
        employee_id = input("Enter the employee ID: ")

    # Connect to the database and fetch the specific employee
        try:
           connection =  connector()
        
           cursor = connection.cursor()
        # SQL query to fetch a specific employee by ID and company name
           query = """
           SELECT EmployeeID, EmployeeName, Position, Salary 
           FROM EmployeeData 
           WHERE CompanyName = %s AND EmployeeID = %s
           """
           cursor.execute(query, (company_name, employee_id))
           result = cursor.fetchone()

           if result:
             print("nEmployee Details:")
             print(f"Employee ID: {result[0]},\n Name: {result[1]}, \n Position: {result[2]}, \n Salary: {result[3]}")
           else:
             print(f"nNo employee found with ID '{employee_id}' in the company '{company_name}'.")
             connection.close()
             BVIEW()
        except :
           print(f"Error:")
           connection.close()
           BVIEW()
        finally:
           connection.close()
           BVIEW()
  
def EUPDATE():
    connection =  connector()
        
    cursor = connection.cursor()
    # Step 2: Get the EmployeeID from the user
    employee_id = int(input("Enter your Employee ID: "))

    # Step 3: Check if the EmployeeID exists
    check_query = "SELECT * FROM EmployeeData WHERE EmployeeID = %s"
    cursor.execute(check_query, (employee_id,))
    employee = cursor.fetchone()

    if employee:
        print("nYour current details are:")
        print(f"Name: {employee[1]}")
        print(f"Designation: {employee[2]}")
        print(f"Department: {employee[3]}")
        print(f"Salary: {employee[4]}")
    
        # Step 4: Ask which field they want to update
        print(" would you like to update?")
        print("1. Name")
        print("2. Designation")
        print("3. Department")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))

        # Step 5: Get the new value from the user
        while true:
          if choice == 1:
           new_value = input("Enter your new Name: ")
           update_query = "UPDATE EmployeeData SET Name = %s WHERE EmployeeID = %s"
          elif choice == 2:
           new_value = input("Enter your new Designation: ")
           update_query = "UPDATE EmployeeData SET Designation = %s WHERE EmployeeID = %s"
          elif choice == 3:
            new_value = input("Enter your new Department: ")
            update_query = "UPDATE EmployeeData SET Department = %s WHERE EmployeeID = %s"
          elif choice == 4:
             print("auto exiting:")
             connection.close()
             main()
           
          else:
            print("your input is not btw 1-4")
            print("auto exiting:)")
            connection.close()
            EUPDATE()

    # Step 6: Update the record in the database
    

    
    else :
       print(f"No employee found with Employee ID: {employee_id}")
    print("nYour details have been updated successfully!")
    cursor.execute(update_query, (new_value, employee_id))
    connection.commit()
    # Step 7: Close the connection
    connection.close()

    
def passwdgen():
 

      # Characters to choose from
      letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      digits = "0123456789"
      special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

      # Combine all possible characters
      all_characters = letters + digits + special_chars

      # Initialize the password
      password = ""

      # Generate a 17-character random password
      for i in range(6):
        password += random.choice(all_characters)

       # Display the password
      print("Your password is:", password)
    
    
    
    
    
    
 
  

def authenticate_user():
    connection =  connector()
        
    cursor = connection.cursor()

    # Step 2: Fixed username and input for password
    username = input("Enter your username")  
    password = input("Enter your password: ")

    # Step 3: Check if the username and password match
    query = "SELECT * FROM Passwords WHERE Username = %s AND Password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("nLogin successful! Proceeding to the next step...")
        # Add further logic here for successful login
    else:
        print("nInvalid credentials! Access denied.")
        connection.close()
        # Close connection and exit
        main()

    # Close the database connection
    connection.close()
    
    
    
    
    
def setup_data():
    # Here, you can add code to set up new data (e.g., add new user, business data)
         print("nYou selected 'Setup'. You can add new records to the database.")
    
         print("This section will allow you to add new records to the system.")
         SETUP()
    
    
    
def AEDIT():
    # Here, you can add code for editing existing data in the system
    print("nYou selected 'Edit Mode'. You can edit existing records.")
    # Example: Editing an existing record (you can add actual DB update logic)
    print("This section will allow you to delete existing records in the system.")
    def addition_deletion():
    # Display menu for user to select action
        print("admin edit mode!")
        
        print("1. Delete Business")
    addition_deletion()
    # Get user input
    print("Please select one if to go further")
    choice = input("Enter the number corresponding to your choice (1-2): ")
        
    if choice == "1":
       ilo1()
       ABDELETE()
        
    else:
        print("nInvalid choice! Please restart the program and select a valid option.")
        ADMIN()
      
      
      
      
      
      
def AVIEW()

        print("nYou selected 'View'. You can view existing records.")
    # Example: Viewing existing data (you can add actual DB query logic)
        print("This section will allow you to view existing records in the system.")

    # Display menu for user to select what they want to view
        print("admin viewer mode")
        print("Please select what you want to view:")
        print("1. View Business Data")
        print("2. View Employee Data")
        print("3. View Balance Sheet Data")
        print("4. BACK")
    # Get user input
        choice = input("Enter the number corresponding to your choice (1-3): ")

        if choice == "1":
           ilo1()
           AVBUSINESS()
        elif choice == "2":
           ilo1()
           AVEMPLOYEE()
        elif choice == "3":
           ilo1()
           AVBALANCESHEET()
        elif choice == "4":
           ADMIN()
        else:
           print("nInvalid choice! Please restart the program and select a valid option.")
           AVIEW()
        
        
        
        
        
def ADMIN():
       # Display menu for user to select action
       print("Welcome to admin control!")
       print("Please select one of the following options:")
       print("1. Setup (Add new data)")
       print("2. Edit Mode (Edit existing data)")
       print("3. View (View existing data)")
       print("4. MAIN PAGE")
       # Get user input
       choice = input("Enter the number corresponding to your choice (1-3): ")

       if choice == "1":
          ilo1()
          setup_data()
       elif choice == "2":
          ilo1()
          edit_data()
       elif choice == "3":
          ilo1()
          view_data()
       elif choice == "4":
          main()
       else:
          print("nInvalid choice! Please restart the program and select a valid option.")
          main()
        
        
        
      
      
      
      
      
      

def BEDIT():
        print("n--- Management System ---")
        print("1. Edit Business Details")
        print("2. Edit Employee Details")
        print("3. Edit Balance Sheet")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            ilo1()
            BEBUSINESS()
        elif choice == '2':
            ilo1()
            BEEMPLOYEE()
        elif choice == '3':
            ilo1()
            BEBALANCESHEET()
        elif choice == '4':
            print("Exiting the program.")
            BUSINESS()
        else:
            print("Invalid choice. Please try again.")
            BUSINESS()
            
            
def BVIEW():
    # Display menu for user to select what they want to view
        print("view my business interface!")
        print("Please select what you want to view:")
        print("1. View Business Data")
        print("2. View Employee Data")
        print("3. View Balance Sheet Data")
        print("4. BUSINESS MAIN-----")
    # Get user input
        choice = input("Enter the number corresponding to your choice (1-3): ")

        if choice == "1":
          ilo1()
          BVBUSINESS()
        elif choice == "2":
          ilo1()
          BVEMPLOYEE()
        elif choice == "3":
          ilo1()
          BVBALANCESHEET()
        elif choice == "4":
          BUSINESS()
        else:
            print("nInvalid choice! Please restart the program and select a valid option.")
            BUSINESS()

        
        
        
        
        
def BUSINESS():
    print("Welcome to the Business Management System!")
    print("What would you like to do?")
    print("1. View Business Details")
    print("2. Edit Business Details")
    print("3. MAIN---------")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        ilo1()
        BVIEW()
    elif choice == "2":
        ilo1()
        BEDIT()
    elif choice == "3":
        main()
    else:
        print("nInvalid choice! Please restart the program and select a valid option.")
        BUSINESS()
      


  

    
  
  
  
  
  
def display_design():
    # Title of the system
    title = "WELCOME TO NBDMS"
    subtitle = "National Business Data Management System"
    
    # Print the upper decorative pattern
    for i in range(1, 6):
        print(" " * (6 - i) + "* " * i + " " * (6 - i) + "* " * i)
    
    # Print the title
    print("n" + "*" * 50)
    print(title.center(50))
    print(subtitle.center(50))
    print("*" * 50 + "n")
    
    # Print the lower decorative pattern
    for i in range(5, 0, -1):
        print(" " * (6 - i) + "* " * i + " " * (6 - i) + "* " * i)

    # Call the function to display the design
    
display_design()
def ilo1():
    print("/-/-"*100)



def newuser():
    global x
    print("THIS MASSAGE YOU WILL ONLY ONCE")
    print("/-/-"*16)
    print("MASSAGE FROM DEVELOPER")
    print("Welcome, Admin! You now have full admin control! Use your power wisely to manage everything and keep things running smoothly. ")
    print("If you need assistance, we are here to support you.Enjoy your new role! ")
    x+=1
    SETUP()
    ADMIN()

    
print("/"*60)
def main():
    # Display role options
    print("Welcome to NBDMS!")
    print("Please select your role:")
    print("1. Database Administrator")
    print("2. Business Owner")
    print("3. Employee")
    
    # Get user input
    choice = int(input("Enter the number corresponding to your role (1-3): "))

    # Respond based on the role
    if choice == 1:
            if x==0:
                newuser()
            else:
                authenticate_user()
                ilo1()
                print("nWelcome, Database Administrator!")
                print("You have full access to the system and can manage all databases.")
        
                ADMIN()

        
    
    elif choice == 2:
          response = input("Are you a new user? (yes/no): ")
          if response =="yes":
              registration()
              balancecreate()
          else:
              authenticate_user()
              ilo1()
              print("nWelcome, Business Owner!")
              print("You can manage your company's business data and balance sheets.")
              BUSINESS()
    elif choice == 3:
        print("nWelcome, Employee!")
        print("You can view and update your personal records.")
        updatemyprofile()
    else:
        print("nInvalid choice! Please restart the program and choose a valid role.")

# Call the main function
main()







    

 
