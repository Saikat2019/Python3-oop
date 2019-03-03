class Employee:
	num_of_emps = 0
"""
num_of_emps and raise_amont are class variable , diff b/w class and 
instance variable are that class variables are shared among all the
 instances
"""
	raise_amount = 1.04
	def __init__(self, first, second,pay):
		self.first = first
		self.second = second
		self.pay = pay
		self.email = first + '.' + second + '@gmail.com'

		Employee.num_of_emps += 1


	def fullname(self):
		return '{} {}'.format(self.first,self.second)

	def applyRaise(self):
			self.pay = int(self.pay * self.raise_amount)
			# instead of Employee.raise_amount use self.raise_amount
			# as it would effect if any emp has diff raise_amount than
			# the Employee class 

emp_1 = Employee('corey','schafer',20000)
emp_2 = Employee('saikat','mondal',10000)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

Employee.raise_amount = 1.05 #changes raise_amount for all instances
emp_1.raise_amount=1.06 #changes only for emp_1 class instance

print(Employee.__dict__)# prints the class attributes in dict format / namespace
			#Employee which is a class blue print will have the 
			#class variable in the dict where as the class instances will not
Employee.applyRaise(emp_1)