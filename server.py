from flask import Flask, render_template,url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/favicon.ico') #if not use redirect then favicon.ico error appear to solve it I use this functioin and favicon.html file
# def fav():
#     return render_template('favicon.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	email=data['email']
	subject=data['subject']
	message=data['message']
	with open('database.txt','a')as database:
		file=database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
	email=data['email']
	subject=data['subject']
	message=data['message']
	with open('database.csv', newline='', mode='a')as database:
		csv_writer=csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
	if request.method=='POST':
		try:
			data=request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'Some thing went wrong.Try Agin!'




