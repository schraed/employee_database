from datetime import date
import sys
today = date.today()
    
class Employees:
    
    def __init__(self,employees_list, ID_list, address_list, data_list):
        self.employees_list = employees_list
        self.ID_list = ID_list
        self.address_list = address_list
        self.data_list = data_list
        
    def show_avaliable_employees(self):
        if len(self.employees_list) > 0:
            print('\nEmployees are: ')
            for employee, ID, address, data in zip(self.employees_list, self.ID_list, self.address_list, self.data_list):
                print(f'Name: {employee}, ID: {ID}, address: {address}, date added to list: {data}')
                print(80*'-')
        else:
            print('Employee list is empty.')
            
    def add_employees(self):
        self.employee_name = input('Type the name of a new employee:>>> ').lower().capitalize()
        while True:
            self.ID_number = input('Type the ID number of a new employee:>>> ')
            if self.ID_number.isdigit():
                if self.ID_number not in self.ID_list:
                    self.employees_list.append(self.employee_name)
                    self.ID_list.append(self.ID_number)
                    break
                else:
                    print(f'{self.employee_name} has same ID number as another employee!')
                    continue
            else:
                print('ID number must be a number.')
            
        self.employee_address = input('Type employee address:>>> ').lower().title()
        self.address_list.append(self.employee_address)
        self.added_date = today.strftime("%d/%m/%Y")
        self.data_list.append(self.added_date)
    
    def delete_employees(self):
        if len(self.employees_list) > 0:
            self.ID_number = input('Type the ID number of employee who you would like to delete:>>> ')
            if self.ID_number in self.ID_list:
                employee_index = self.ID_list.index(self.ID_number)
                self.ID_list.remove(self.ID_number)
                del self.employees_list[employee_index]
                del self.address_list[employee_index]
                del self.data_list[employee_index]
                 
            else:
                print(f'Employee withe the ID: {self.numer_ID} is not on the list.')
        else:
            print('\nThere is no employees on the list.')
            
    def edit_employee(self):
        self.ID_number = input('Type the ID number of employee who you would like to edit:>>> ')
        if self.ID_number in self.ID_list:
            print('''\nType which atribute you would like to edit:\n
                  1 - Name
                  2 - ID
                  3 - address
                  ''')
        
            what_to_edit = int(input())
            if what_to_edit == 1:
                self.new_name = input('Type new name:>>>  ')
                self.employees_list[self.ID_list.index(self.ID_number)] = self.new_name
            elif what_to_edit == 2:
                while True:
                    self.new_ID = input('Type new ID:>>> ')
                    if self.new_ID.isdigit():
                        if self.new_ID not in ID_list:
                            self.ID_list[self.ID_list.index(self.ID_number)] = self.new_ID
                            break
                        else:
                           print('Another employee has such ID number.\n')
                           continue
                    else:
                        print('ID number must be a number.')
            elif what_to_edit == 3:
                self.new_address = input('Type new address:>>> ')
                self.address_list[self.ID_list.index(self.ID_number)] = self.new_address
        else:
            print('There is no employee with this ID number\n')
            
            

name_list = []
ID_list = []
address_list = []
data_list = []

employees = Employees(name_list, ID_list, address_list, data_list)
number_of_employees = int(input('There is no employees on the list, type as a number how many employees you would like to add:>>> '))

for i in range(1, number_of_employees+1):
    employee = input(f'Type the name of the {i} employee:>>> ').lower().capitalize()
    name_list += [employee]
    
    while True:
        employee_ID = input((f'Type the ID number of the {i} employee:>>> '))
        if  employee_ID.isdigit():
            if  employee_ID not in ID_list:
                ID_list.append(employee_ID)
                break
            else:
                print('Entered ID number is already on the list.')
                continue
        else:
            print('ID number must be a number.')
            
    employee_address = input((f'Type an address of the {i} employee:>>> ')).lower().title()
    address_list += [employee_address]
            
    added_date = today.strftime("%d/%m/%Y")
    data_list += [added_date]

while True:

   print('''\nChoose the operation you would like to make:\n
         1 - to show employee list
         2 - to add employee
         3 - to delete employee
         4 - to edit employee
         5 - to exit the program
         ''')
   user_choice = int(input(">>> "))
   
   if user_choice == 1:
       employees.show_avaliable_employees()
   elif user_choice == 2:
       employees.add_employees()
   elif user_choice == 3:
       employees.delete_employees()
   elif user_choice == 4:
       employees. edit_employee()
   elif user_choice == 5:
       sys.exit()

       
       
       
       

       
            
            



