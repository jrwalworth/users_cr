
from flask import Flask, render_template, request, redirect
from app.models.user import User

app = Flask(__name__)

#home - landing page
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users = users)

#create user method to add to DB
@app.route('/users/new', methods=["POST"])
def create_user():
    data = {
        "fname" : request.form["fname"], 
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    User.save(data)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
