from flask import Flask, render_template, url_for, request, redirect
import json
import csv
from pathlib import Path
app = Flask(__name__)
# The testing website template is from: https://html5up.net/, and it will not be uploaded to github
# for html: {{This is teamplating for Flask, run python code}}

# For dependencies:
# pip freeze > requirements.txt
# pip install -r requirements.txt

def store_data_json(data):
    # store data in json format
    data_path = Path('./data.json')
    
    if not data_path.exists():
        dat_list = [data]
        with open(data_path, 'w') as data_file:
            file = data_file.write(json.dumps(dat_list, indent=2))
    else:
        with open(data_path, 'r') as read_data:
            try:
                existing_data = json.load(read_data)
                existing_data.append(data)
            except json.decoder.JSONDecodeError:
                existing_data = [data]
            with open(data_path, 'w') as data_file:
                file = data_file.write(json.dumps(existing_data, indent=2))
    return 0


def store_data_csv(data):
    data_path = Path('./data.csv')
    with open(data_path, newline='', mode='a') as data_file:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/')
def get_root():
    return render_template('./index.html')


@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods= ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # transform the form into dictionary
            data = request.form.to_dict()
            store_data_csv(data)
        except:
            return 'Something went wrong with the submission'
        return redirect('/elements.html')
    else:
        return 'something went wrong'
    

# @app.route('/favicon.ico')
# def hello_world():
#     return render_template('./index.html')
