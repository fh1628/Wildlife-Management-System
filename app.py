from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import request

app = Flask(__name__)

# Configure the application to use MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/Testing_DB'

# Create a SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Define the User model class
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Use the Flask app context to execute database operations
with app.app_context():
    # Create the database tables (if they don't exist)
    db.create_all()

    # Create a new user and add it to the database



@app.route('/insertUser', methods=['POST'])
def insertUser():
    new_username = request.json["username"]
    new_password = request.json["password"]
    # new_username = "Joe"
    # new_password = "Pass"
    new_user = User(username = new_username, password = new_password)
    db.session.add(new_user)
    db.session.commit()

    user = {
            'username': new_username,
            'email': new_password
    }

    return jsonify(user)



# # Define a route for the GET request
# @app.route('/users/<username>', methods=['GET'])
# def get_user(username):
#     # Query the database for a user with the specified username
#     query = text("SELECT * FROM users WHERE username=:username")
#     result = db.session.execute(query, {'username': username})
#     row = result.fetchone()

#     # If a matching user was found, return its information as a JSON response
#     if row is not None:
#         user = {
#             'id': row[0],
#             'username': row[1],
#             'email': row[2]
#         }
#         return jsonify(user)
#     # If no matching user was found, return a 404 error
#     else:
#         return 'User not found', 404
