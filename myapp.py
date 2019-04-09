from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
	return render_template('webpage.htm')
@app.route('/fb')
def fb():
	return "Welcome to facebook"
@app.route('/form', methods =["post"])
def form():
	name=request.form["name"]
	password=request.form["password"]
	Enroll_no=request.form["E_no"]
	print(name)
	print(password)
	print(Enroll_no)
	return render_template("123.htm", name=name, Enroll_no=Enroll_no, password=password)
if __name__ == '__main__':
	app.run(debug = True, port = 5002)
