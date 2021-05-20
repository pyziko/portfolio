from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def my_home():
    return render_template('index.html')  # this will look in a folder called templates


# creating a dynamic route catering for all the endpoints below

@app.route("/<string:page_name>")
def html_page_name(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            # message = request.form['message']  # getting one by one
            # print(message)
            data = request.form.to_dict()  # converting the form data into dictionary
            write_to_file(data)  # writing to file
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["email"]
        message = data["message"]
        database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# @app.route("/work.html")
# def work():
#     return render_template('work.html')
#
#
# @app.route("/works.html")
# def works():
#     return render_template('works.html')
#
#
# @app.route("/components.html")
# def components():
#     return render_template('components.html')
#
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# todo info === CHECK IN quick-start
# flask run
# set FLASK_APP=main.py
# set FLASK_DEV=development ::: live reload
# checkout url-building.
# adding a favicon
# todo search for variable rules::: for url/query parameters
