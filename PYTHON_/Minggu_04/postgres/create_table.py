import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE accounts (
	        user_id serial PRIMARY KEY,
	        username VARCHAR ( 50 ) UNIQUE NOT NULL,
	        password VARCHAR ( 50 ) NOT NULL,
	        email VARCHAR ( 255 ) UNIQUE NOT NULL,
	        created_on TIMESTAMP NOT NULL,
                last_login TIMESTAMP 
        )
        """,
        """
        CREATE TABLE roles(
        role_id serial PRIMARY KEY,
        role_name VARCHAR (255) UNIQUE NOT NULL
        )
        """, 
        """
        CREATE TABLE account_roles (
        user_id INT NOT NULL,
        role_id INT NOT NULL,
        grant_date TIMESTAMP,
        PRIMARY KEY (user_id, role_id),
        FOREIGN KEY (role_id)
        REFERENCES roles (role_id),
        FOREIGN KEY (user_id)
        REFERENCES accounts (user_id)
        )
        """)

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()

