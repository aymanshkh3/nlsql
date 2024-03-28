import sqlite3

try:
    # Connect to SQLite
    connection = sqlite3.connect("storedb")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Create SALES table
    sales_table_info = """
    CREATE TABLE IF NOT EXISTS SALES (
        SaleID INTEGER PRIMARY KEY,
        Date DATE,
        CustomerID INTEGER,
        EmployeeID INTEGER,
        TotalAmount NUMERIC(10, 2)
    );
    """
    cursor.execute(sales_table_info)

    # Insert data into SALES table
    sales_data = [
        (1, '2024-02-25', 1, 1, 100.00),
        (2, '2024-02-26', 2, 2, 150.00),
        (3, '2024-02-27', 3, 3, 200.00),
        (4, '2024-02-28', 4, 4, 120.00),
        (5, '2024-02-29', 5, 5, 80.00),
        (6, '2024-01-01', 6, 6, 180.00),
        (7, '2024-01-02', 7, 7, 220.00),
        (8, '2024-01-03', 8, 8, 90.00),
        (9, '2024-01-04', 9, 9, 130.00),
        (10, '2024-01-05', 10, 10, 170.00)
    ]
    cursor.executemany('''INSERT INTO SALES (SaleID, Date, CustomerID, EmployeeID, TotalAmount) VALUES (?, ?, ?, ?, ?)''', sales_data)

    # Create Products table
    products_table_info = """
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY,
        ProductName VARCHAR(255),
        Description TEXT,
        UnitPrice NUMERIC(10, 2),
        QuantityInStock INTEGER
    );
    """
    cursor.execute(products_table_info)

    # Insert data into Products table
    products_data = [
        (1, 'Product 1', 'Description of Product 1', 10.99, 100),
        (2, 'Product 2', 'Description of Product 2', 15.49, 150),
        (3, 'Product 3', 'Description of Product 3', 22.99, 200),
        (4, 'Product 4', 'Description of Product 4', 18.79, 120),
        (5, 'Product 5', 'Description of Product 5', 30.99, 80),
        (6, 'Product 6', 'Description of Product 6', 12.59, 180),
        (7, 'Product 7', 'Description of Product 7', 25.99, 220),
        (8, 'Product 8', 'Description of Product 8', 8.99, 90),
        (9, 'Product 9', 'Description of Product 9', 16.49, 130),
        (10, 'Product 10', 'Description of Product 10', 20.99, 170)
    ]
    cursor.executemany('''INSERT INTO Products (ProductID, ProductName, Description, UnitPrice, QuantityInStock) VALUES (?, ?, ?, ?, ?)''', products_data)

    # Commit changes and close connection
    connection.commit()
    print("Database successfully created and populated.")
except sqlite3.Error as error:
    print("Error:", error)
finally:
    connection.close()
