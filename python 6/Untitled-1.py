# Define a list of employees with their salaries
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Jane", "salary": 60000},
    {"name": "Doe", "salary": 45000},
    {"name": "Smith", "salary": 70000}
]

# Sort the employees by salary
sorted_employees = sorted(employees, key=lambda x: x['salary'])

# Print the sorted list of employees
for employee in sorted_employees:
    print(f"Name: {employee['name']}, Salary: {employee['salary']}")