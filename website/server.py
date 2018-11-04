from flask import Flask, request, url_for, render_template
#from training import up_or_down


app = Flask(__name__)

#mat = up_or_down('google')
#a = {'google':mat}

posts = [{'hello': 'world'}]

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', posts=posts)

if __name__ == '__main__':
	app.run(debug=True)