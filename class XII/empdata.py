emp = [['Rajnish', 36, 'Testing', 45000], ['Amrita', 45, 'HR', 50000]]

def add_emp(empdata):
    emp.append(empdata)

def show_employee(emp):
    print("Name\tAge\tDepartment\tSalary")
    for e in emp:
        print("\t".join(map(str, e)))

new_emp_data = ['John', 30, 'Marketing', 60000]
add_emp(new_emp_data)
show_employee(emp)
