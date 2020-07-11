from flask import Flask, render_template, request, jsonify
from db import DataBaseSQLite 

app = Flask(__name__)


@app.route('/get_all_books', methods= ['GET'])
def get_book():
	my_db = DataBaseSQLite('books.db')
	query_code = 'SELECT * FROM books'
	data = my_db.query_data(query_code)
	my_db.close()
	clean_data = []
	for row in data:
		book_obj = {
			"ID": row[0],
			"Title": row[1],
			"Genre": row[2],
			"Author": row[3]
		}
		clean_data.append(book_obj)

	respond = {
		'books': clean_data
	}
	respond = jsonify(respond)
	return respond

