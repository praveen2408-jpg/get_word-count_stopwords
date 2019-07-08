from flask_api import FlaskAPI
from flask import request
from nltk.corpus import stopwords
import json

app = FlaskAPI(__name__)


@app.route('/get_word_count_stopwords/', methods=['GET', 'POST'])
def get_word_count_stopwords():
	if request.method == 'GET':
		return 'Invalid Request'

	if request.method == 'POST':
		data =request.get_json()
		output = {}
		if not data:
			output = {'message': 'No Text Received'}
			return output
		for key in data.keys():
			text = data[key]
			text = text.split(' ')
			non_stop_words = []
			en_stops = set(stopwords.words('english'))
			for word in text: 
			    if word not in en_stops:
			    	non_stop_words.append(word)
			output[key] = non_stop_words			
		return json.dumps(output)				
		
   

if __name__ == '__main__':
	app.run()


