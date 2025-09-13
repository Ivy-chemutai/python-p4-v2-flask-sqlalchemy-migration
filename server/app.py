# server/app.py

from flask import Flask #type: ignore
from flask_migrate import Migrate  # type: ignore  

from models import db, Employee, Department

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    employees = db.session.execute(db.select(Employee)).scalars().all()
    departments = db.session.execute(db.select(Department)).scalars().all()
    return f'Employees: {len(employees)}, Departments: {len(departments)}'


if __name__ == '__main__':
    app.run(port=5556, debug=True)
