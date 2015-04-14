from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
	if(request.method == "POST"):
		#return request.form.get('buff1',None)+" "+request.form.get('buff2',None)+" "+request.form.get('buff3',None)+" "+request.form.get('vte',None)+" "+request.form.get('voc',None)
		return "Server Working"
	else:
		return "Fail"

if __name__ == '__main__':
    app.run(debug=True)