import sys
def emp(name, employee_id, department, salary):
    return f"Name: {name}, Employee ID: {employee_id}, Department: {department}, salary: {salary}"
if __name__ == "__main__":
    name = sys.argv[1]
    employee_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]
    print("Employee details")
    print(emp(name, employee_id, department, salary))