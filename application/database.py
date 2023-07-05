import sqlite3

# Connect to SQL database or create database if it doesn't exist
connect = sqlite3.connect('data/securespace.db')
cursor = connect.cursor()

# Creation of the 'users' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        name TEXT NOT NULL,
        code TEXT UNIQUE NOT NULL,
        dob INTEGER,
        role_id INTEGER,        
        country_id INTEGER,
        username TEXT UNIQUE,
        password TEXT,     
        phrase TEXT,   
        last_login_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        is_held NUMERIC DEFAULT 1,
        status NUMERIC DEFAULT 0,        
        FOREIGN KEY (role_id) REFERENCES roles (id),
        FOREIGN KEY (country_id) REFERENCES countries (id)
    )
''')

# Creation of the roles table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        name TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Creation of the permissions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS permissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        name TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Creation of the role_has_permissions pivot table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS role_has_permissions (
        role_id INTEGER NOT NULL,
        permission_id INTEGER NOT NULL,
        FOREIGN KEY (role_id) REFERENCES roles (id)   
        FOREIGN KEY (permission_id) REFERENCES permissions (id)        
    )
''')

# Creation of the records table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        user_id INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Creation of the record_items table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS record_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        record_id INTEGER,
        complains TEXT NULL,
        height REAL NULL,
        weight REAL NULL,
        blood_pressure TEXT NULL,      
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (record_id) REFERENCES records (id)
    )
''')



# Creation of the checks table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS checks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        name TEXT NOT NULL       
    )
''')

# Creation of the record_item_has_checks pivot table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS record_item_has_checks (
        record_item_id INTEGER NOT NULL,
        check_id INTEGER NOT NULL,
        FOREIGN KEY (record_item_id) REFERENCES record_items (id)   
        FOREIGN KEY (check_id) REFERENCES checks (id)        
    )
''')

# Creation of the record_items table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        severity TEXT NULL,
        activity TEXT NULL,
        category INTEGER NULL,
        data TEXT NULL,      
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')


# Creation of the countries table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uuid TEXT NOT NULL,
        code TEXT,
        name TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Seed the check table

# checks = [('Temperature',),
#           ('Radiation',)]

# cursor.executemany(''' 
#         INSERT INTO checks(name) 
#         VALUES(?)
# ''', checks)

# Commit changes and close the connection
connect.commit()
connect.close()

print("Database initialised.")