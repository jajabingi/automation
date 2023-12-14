import MySQLdb


def mysqlconnect():
    # Trying to connect
    try:
        # Open database connection
        db = MySQLdb.connect(host="localhost", user="root", password="", database="YourDatabaseName")
    except:
        print("Can't connect to database")
        return 0

    # If Connection Is Successful
    print("Connected")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Create database if not exists
    create_db_table = """CREATE DATABASE IF NOT EXISTS YourDatabaseName"""
    cursor.execute(create_db_table)

    # Connect to the specific database
    cursor.execute("USE YourDatabaseName")

    # Create tables
    create_table = """-- Users Table
                    CREATE TABLE IF NOT EXISTS Users (
                        UserID INT AUTO_INCREMENT PRIMARY KEY,
                        Username VARCHAR(50) NOT NULL,
                        Email VARCHAR(100) NOT NULL,
                        Password VARCHAR(255) NOT NULL,
                        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );

                    -- Posts Table
                    CREATE TABLE IF NOT EXISTS Posts (
                        PostID INT AUTO_INCREMENT PRIMARY KEY,
                        UserID INT,
                        Title VARCHAR(255) NOT NULL,
                        Content TEXT,
                        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (UserID) REFERENCES Users(UserID)
                    );

                    -- Comments Table
                    CREATE TABLE IF NOT EXISTS Comments (
                        CommentID INT AUTO_INCREMENT PRIMARY KEY,
                        UserID INT,
                        PostID INT,
                        Content TEXT,
                        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (UserID) REFERENCES Users(UserID),
                        FOREIGN KEY (PostID) REFERENCES Posts(PostID)
                    );"""

    cursor.execute(create_table)

    # Create indexes (optional)
    create_index_optional = """CREATE INDEX idx_username ON Users(Username);
                                CREATE INDEX idx_email ON Users(Email);"""
    cursor.execute(create_index_optional)

    # Insert sample data (optional)
    insert_sample_data = """ -- Insert a user
                            INSERT INTO Users (Username, Email, Password) VALUES ('JohnDoe', 'john@example.com', 'hashed_password');

                            -- Insert a post
                            INSERT INTO Posts (UserID, Title, Content) VALUES (1, 'Sample Post', 'This is a sample post content.');

                            -- Insert a comment
                            INSERT INTO Comments (UserID, PostID, Content) VALUES (1, 1, 'This is a sample comment.');
                            """
    cursor.execute(insert_sample_data)

    # Disconnect from the server
    db.close()


mysqlconnect()

