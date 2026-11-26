import sys
def emp(name, employee_id, department, salary):
    return f"Name: {name}\n, Employee ID: {employee_id}\n, Department: {department}\n, salary: {salary}"
if __name__ == "__main__":
    name = sys.argv[1]
    employee_id = sys.argv[2]
    salary = sys.argv[4]
    print("Employee details")
    print(emp(name, employee_id, department, salary))