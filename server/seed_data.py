from app import app
from models import db, Employee, Department

def seed_data():
    with app.app_context():
        # Add employees
        employees = [
            Employee(name="Kai Uri", salary=89000),
            Employee(name="Alena Lee", salary=125000),
            Employee(name="John Smith", salary=75000),
            Employee(name="Sarah Johnson", salary=95000)
        ]
        
        # Add departments
        departments = [
            Department(name="Payroll", address="Building A, 4th Floor"),
            Department(name="Human Resources", address="Building C, 1st Floor"),
            Department(name="Engineering", address="Building B, 2nd Floor"),
            Department(name="Marketing", address="Building A, 3rd Floor")
        ]
        
        # Add to database
        for employee in employees:
            db.session.add(employee)
        
        for department in departments:
            db.session.add(department)
        
        db.session.commit()
        print("Sample data added successfully!")

if __name__ == "__main__":
    seed_data()