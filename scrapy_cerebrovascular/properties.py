# pg数据库连接
DIALECT = 'postgresql'
DRIVER = 'psycopg2'
USERNAME = 'postgres'
PASSWORD = '969696'
HOST = '127.0.0.1'
PORT = '5432'
DATABASE = 'postgres'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
BIT_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, '192.168.3.200', PORT, DATABASE)

