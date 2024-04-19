from sqlalchemy import create_engine

DB_USER = 'postgres'
DB_PASSWORD = 'monica'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'postgres'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')