class Employee:
	num_of_emps = 0
	raise_amount = 1.04
	def __init__(self, first, second,pay):
		self.first = first
		self.second = second
		self.pay = pay
		self.email = first + '.' + second + '@gmail.com'

		Employee.num_of_emps += 1

#regular methods automatically takes the instance as first arg
	def fullname(self): #it's a regular method
		return '{} {}'.format(self.first,self.second)

	def applyRaise(self):
			self.pay = int(self.pay * self.raise_amount)

	@classmethod #altering the functionality of this method
	def set_raise_amt(cls,amount):  #it will take the class as 1st arg 
		cls.raise_amount = amount   #instead of instance

	@classmethod   # class method can be used as alternative 
	def from_string(cls,emp_str):  #construction as this one
		first , last , pay = emp_str.split('-')
		return cls(first,last,pay) # here cls is same as Employee

	@staticmethod #decorator for static method 
	def is_workday(day): #static methods don't pass anything autometically
		if day.weekday() == 5 or day.weekday() == 6 :
			return False
		return True

print(Employee.num_of_emps)

emp_1 = Employee('corey','schafer',20000)
emp_2 = Employee('saikat','mondal',10000)

print(Employee.num_of_emps)

Employee.set_raise_amt(1.09)

emp_str1 = 'john-doe-70000'
emp_str2 = 'steve-smith-60000'
emp_str3 = 'jane-dow-40000'

new_emp1 = Employee.from_string(emp_str1)

print(Employee.num_of_emps)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

import datetime

my_date = datetime.date(2018,9,1)

print(Employee.is_workday(my_date))