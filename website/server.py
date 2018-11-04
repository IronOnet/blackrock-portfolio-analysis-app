from flask import Flask, request, url_for, render_template
from training import up_or_down


app = Flask(__name__)

companies = [
        'google',
        'apple',
        'applied materials',
        'adobe',
        'amazon',
        'cisco',
        'citrix',
        'expedia',
        'facebook',
        'intel',
        'microsoft',
        'netflix',
        'nvidia',
        'paypal',
        'qualcomm',
        'starbucks',
        ]

posts = []
for company in companies:
	posts.append({'name': company, 'trend' : up_or_down(company)})

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', posts=posts)

if __name__ == '__main__':
	app.run(debug=True)