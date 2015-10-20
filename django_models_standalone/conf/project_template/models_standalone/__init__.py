from django import db as django_db

# when DEBUG is True we need to reset connection in standalone application, otherwise you will have memory leaks
def reset_db_connection():
	django_db.connection.close()