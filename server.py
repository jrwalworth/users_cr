
from flask import render_template, request, redirect
from app.models.user import User

from app import app

#home - landing page
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users=users)

##route page to add new user
@app.route('/users/new')
def new():
    return render_template('new.html')

#Add user method to add to DB
@app.route('/users/add', methods=["POST"])
def add_user():
    data = {
        "fname" : request.form["fname"], 
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
