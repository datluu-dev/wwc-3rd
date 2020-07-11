import sqlite3

class DataBaseSQLite():
	def __init__(self, database_file):
		self.conn = None
		self.cursor = None 

		if database_file:
			self.open(database_file)

	def open(self, database_file):
		try:
			self.conn = sqlite3.connect(database_file)
			self.cursor = self.conn.cursor()
		except sqlite3.Error as e:
			print("Connect to database failed")

	def close(self):
		if self.conn:
			self.conn.commit()
			self.cursor.close()
			self.conn.close()

	def query_data(self, querry_code):
		self.cursor.execute(querry_code)
		return self.cursor.fetchall()