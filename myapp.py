from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def hello():
	return render_template('index.html')
@app.route('/fb')
def fb():
	return "Welcome to facebook"
if __name__ == '__main__':
	app.run(port = 5002)
