from flask import Flask, request, render_template, redirect, url_for, make_response, flash
from datetime import date
import json

from jumbler import make_paragraphs

app = Flask(__name__)
app.secret_key = 'kla;sdkhweh.s,jfa;lkgheoith'

def get_cookie():
	try:
		data = json.loads(request.cookies.get('settings'))
	except TypeError:
		data = {}
	return data

@app.route('/')
def index():
	return render_template('index.html', cookie=get_cookie(), CURRENTYEAR=date.today().year)

@app.route('/text')
def text():
	data = get_cookie()
	num = int(data['paragraphs'])
	ipsum_text = make_paragraphs(num)
	return render_template(
		'text.html',
		cookie=get_cookie(),
		ipsum_text=ipsum_text,
		CURRENTYEAR=date.today().year
	)

@app.route('/save', methods=['POST'])
def save():
	flash("You are my favorite customer!")
	response = make_response(redirect(url_for('text')))
	data = get_cookie()
	data.update(dict(request.form.items()))
	response.set_cookie('settings', json.dumps(dict(request.form.items())))
	return response

# app.run(debug=True, port=8000, host='0.0.0.0')
# app.run(threaded=True, port=5000)
if __name__ == '__main__':
    app.run()