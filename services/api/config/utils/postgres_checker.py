import logging
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

logger = logging.getLogger(__name__)

def create_postgres_db_if_not_exists(db_name, db_user, db_password, db_host, db_port):
    """
    Creates the PostgreSQL database if it doesn't already exist.
    Returns True if database exists or was created, False otherwise.
    """
    try:
        # Connect to default postgres database to check if our database exists
        connection = psycopg2.connect(
            dbname='postgres',
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        cursor = connection.cursor()
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
        exists = cursor.fetchone()
        
        if not exists:
            logger.info(f"Database '{db_name}' does not exist, creating it now")
            try:
                # Create the database
                cursor.execute(f"CREATE DATABASE \"{db_name}\"")
                logger.info(f"Successfully created database '{db_name}'")
            except Exception as e:
                logger.error(f"Failed to create database '{db_name}': {str(e)}")
                connection.close()
                return False
        else:
            logger.info(f"Database '{db_name}' already exists")
            
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        logger.error(f"Error checking/creating database: {str(e)}")
        return False

def check_postgres_connection(db_name, db_user, db_password, db_host, db_port):
    """
    Validates if the PostgreSQL connection is working properly.
    Returns a tuple (bool, str, bool) indicating success, message, and whether db was created
    """
    db_created = False
    
    try:
        # First ensure the database exists
        db_created = create_postgres_db_if_not_exists(db_name, db_user, db_password, db_host, db_port)
        
        # Now try connecting to the database
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()
        
        # Get PostgreSQL version
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        
        cursor.close()
        connection.close()
        
        logger.info(f"PostgreSQL connection successful: {version}")
        return True, f"PostgreSQL connection successful: {version}", db_created
    except Exception as e:
        error_msg = f"PostgreSQL connection failed: {str(e)}"
        logger.error(error_msg)
        return False, error_msg, False

def ensure_database_exists(db_name, db_user, db_password, db_host, db_port):
    """
    Ensures that the configured database exists by attempting to create it if necessary.
    Returns True if database exists or was created successfully, False otherwise.
    """
    return create_postgres_db_if_not_exists(db_name, db_user, db_password, db_host, db_port)
